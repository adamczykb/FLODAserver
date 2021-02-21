from django.urls import path, include
import data_server.mobile_views

urlpatterns = [
    path('login', data_server.mobile_views.get_session_token),
    path('basic', data_server.mobile_views.get_user_info)

]