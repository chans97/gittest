from django.contrib import admin
from .models import Content

# admin.site.register(Content)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass
