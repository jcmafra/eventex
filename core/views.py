# Create your views here.


from django.http import HttpResponse                                            

from django.template import loader, Context                                     


from django.shortcuts import render_to_response                                 
                                   
 

def homepage(request):
    from django.conf import settings
    contex = {'MEDIA_URL': settings.MEDIA_URL}
    
    return render_to_response('index.html', contex)