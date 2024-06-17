from django.shortcuts import render
from core.models import GeneralSetting
# Create your views here.
def index(req):
    site_title=GeneralSetting.objects.get(name='site_title').parameter
    home_banner_name=GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title=GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description=GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_welcome=GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer=GeneralSetting.objects.get(name='about_myself_footer').parameter
    context={
    'site_title':site_title,
    'home_banner_name':home_banner_name,
    'home_banner_title':home_banner_title,
    'home_banner_description':home_banner_description,
    'about_myself_welcome':about_myself_welcome,
    'about_myself_footer':about_myself_footer
    }
    return render(req,'index.html',context)
