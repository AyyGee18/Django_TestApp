from django.urls import path
from my_app import views

# TEMPLATE URLS!
app_name = "my_app"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="user_login")
]