from django.contrib import admin
from django.urls import path, include

from accounts.views import signup_view
from home.views import home_view


urlpatterns = [
    # Home
    path('',                 home_view, name='home'),

    # Shop
    path('shop/',            include('shop.urls')),

    # API
    path('api/v1/',          include('api.urls')),

    # Admin and Auth
    path('admin/',           admin.site.urls),
    path('accounts/',        include('django.contrib.auth.urls')),
    path('accounts/signup/', signup_view, name='signup'),
    path('api-auth/',        include('rest_framework.urls')),
]
