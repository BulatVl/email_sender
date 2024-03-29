from django.contrib import admin
from django.urls import path, include, re_path
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),

    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<slug:uidb64>/<slug:token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    re_path(r'^account/', include('allauth.urls')),
]
