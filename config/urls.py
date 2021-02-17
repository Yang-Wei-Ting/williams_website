from django.contrib import admin
from django.urls import path, include

from accounts.views import signup_view
from home.views import home_view


urlpatterns = [
    path('admin/',           admin.site.urls),
    path('accounts/',        include('django.contrib.auth.urls')),

    path('accounts/signup/', signup_view, name='signup'),

    path('',                 home_view,   name='home'),
    path('shop/',            include('shop.urls')),
    path('api/',             include('api.urls')),
]
