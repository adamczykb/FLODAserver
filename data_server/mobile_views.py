import string
import random

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from data_server.models import MobileTokenSession


@csrf_exempt
def get_session_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    response = dict({'Token': '0'})

    if user is not None:
        new_token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(50))
        MobileTokenSession.objects.create(token=new_token, user_account=user)
        response = dict({'Token': new_token})
        return HttpResponse(json.dumps(response))
    else:
        return HttpResponse(response)


@csrf_exempt
def get_user_info(request):
    mobile_token = request.POST.get('Token')
    user_info = MobileTokenSession.objects.get(token=mobile_token).user_account
    if user_info is not None:
        if user_info.is_active:
            response = dict(
                {'username': user_info.username, "email": user_info.email, "superuser": user_info.is_superuser,
                 "error": False})
            return HttpResponse(json.dumps(response))
    else:
        return HttpResponse(json.dumps(dict({"error": True})))
