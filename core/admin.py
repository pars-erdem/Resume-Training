from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description']
    list_editable = ['description', 'parameter']


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description']
    list_editable = ['description', 'file']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'order', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'percentage']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'icon', 'updated_date', 'created_date']
    search_fields = ['link']
    list_editable = ['link']
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['slug', 'file', 'button_text','updated_date', 'created_date']
    search_fields = ['slug','button_text']
    list_editable = [ 'file', 'button_text']