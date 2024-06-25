from django.http import JsonResponse
from django.shortcuts import render
from core.models import Document
from contact.models import Message
from contact.forms import ContactForm
def contact_form(request):
    contact_form=ContactForm(request.POST or None)
    if request.POST:
        if contact_form.is_valid():
            name=request.POST.get('name')
            mail=request.POST.get('mail')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            Message.objects.create(
                name=name, mail=mail, subject=subject, message=message,
            )
            success=True
            message='Bağlandı'
        else:
            success=False
            message='Error'
    else:
        success=False
        message='Post istegi degil.'
    context = {'success': success,
               'message': message}
    return JsonResponse(context)
def contact(req):
    contact_form=ContactForm()
    context={'contact_form':contact_form}
    return render(req,'contact.html',context)
