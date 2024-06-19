from django.contrib import admin
from core.models import *
# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','parameter','updated_date', 'created_date']
    search_fields = ['name', 'description']
    list_editable = ['description','parameter']
@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description']
    list_editable = ['description', 'file']
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'order','percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'percentage']