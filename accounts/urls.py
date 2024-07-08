from django.urls import path
from . import views



app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashborad/', views.dashborad, name='dashborad'),
]
