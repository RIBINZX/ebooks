
# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("shop_details/<int:id>/", views.shop_details, name="shop_details"),
    path("", views.shop, name="shop"),
    path("signup", views.signup, name="signup"),
    path("login", views.login_1, name="login"),

]