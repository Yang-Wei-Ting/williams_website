from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Home
    path('',          include('home.urls')),

    # Shop
    path('shop/',     include('shop.urls')),

    # API
    path('api/v1/',   include('api.urls')),

    # Admin and Auth
    path('admin/',    admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

handler404 = 'home.views.page_not_found_view'
