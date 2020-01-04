"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (RegistrationAPIView, UserRetrieveUpdateAPIView,
                    VerifyAPIView, LoginAPIView,UsersRetrieveSearchViewSet,
                    PassResetEmailAPIView)

urlpatterns = [
    path('signup', RegistrationAPIView.as_view(), name='user-registration'),
    path('login', LoginAPIView.as_view(), name='user-login'),
    path('verify/<str:token>', VerifyAPIView.as_view(), name='user-verify'),
    path('profile', UserRetrieveUpdateAPIView.as_view(),
        name='user-retrieve-update'),
    path('retrieve', UsersRetrieveSearchViewSet.as_view(
        {'get': 'search'}), name='users-retrieve-search'),
    path('password-reset', PassResetEmailAPIView.as_view(),
         name='user-reset-password'),
]
