from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('detail/<str:usrn>/', views.userDetail, name="details"),
    path('finder/', views.finderPage, name='univ_finder'),

]
