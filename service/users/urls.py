from django.urls import path, re_path
from rest_framework import routers

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView

from .views import CustomUserViewSet

router = routers.DefaultRouter()
router.register('user', CustomUserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]

urlpatterns += router.urls