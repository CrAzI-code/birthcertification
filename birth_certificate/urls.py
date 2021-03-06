from django.urls import path
from . import views

app_name = "birth_certificate"
urlpatterns = [
    path('', views.index, name= "index"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),    
    path('register/', views.register, name="register"),
    path('user_data/', views.user_data, name='user_data'),
    path('login/', views.login, name="login"),
    path('generate_certificate/', views.generate, name="generate"),
    path('logout/', views.logout, name="logout")
    ]