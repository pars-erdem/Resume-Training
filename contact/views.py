from django.http import JsonResponse
from django.shortcuts import render
from core.models import Document

def contact_form(req):
    context = {'success': True,
               'message': 'Hello World!'}
    return JsonResponse(context)
def contact(req):

    return render(req,'contact.html')
