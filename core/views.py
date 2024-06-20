from django.shortcuts import render, redirect,get_object_or_404

from core.models import GeneralSetting, ImageSetting, Skill, SocialMedia,Document


# Create your views here.
def layout(req):
    documents = Document.objects.all()
    links = SocialMedia.objects.all()
    context = {
        'documents': documents,
        'links': links,

    }
    return context
def index(req):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter
    ##Image
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file

    ##SKILLS
    skills = Skill.objects.all()
    ##links

    #Documents
    documents = Document.objects.all()
    context = {
        'site_title': site_title,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'home_banner_image': home_banner_image,
        'skills': skills,
    }
    return render(req, 'index.html', context)
def redirect_url(request,slug):
    doc=get_object_or_404(Document,slug=slug)
    if doc:
        return redirect(doc.file.url)
    else:
        return redirect('index')
