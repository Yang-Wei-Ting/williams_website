from django.contrib import admin

from .models import HomeCaption


class HomeCaptionAdmin(admin.ModelAdmin):
    list_display = ("purpose", "text")


admin.site.register(HomeCaption, HomeCaptionAdmin)
