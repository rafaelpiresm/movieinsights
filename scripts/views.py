# -*- coding: utf-8 -*-
from django.http import HttpResponse
from scripts.models import Script
from django.shortcuts import render_to_response
from django.template.context import RequestContext



def details(request, script_id):
    script = Script()
    script = script.getScriptByid(script_id)    
    script.content.replace('\n', '<b>')
    return render_to_response('details.html', {'script' : script },
                              context_instance=RequestContext(request)) 
    
def full_search(request):
    val_fulltext = request.POST['fulltext']
    script = Script()
    return HttpResponse(script.getDensidadeTermos(val_fulltext))
    
def search(request):
    if request.method == 'POST':
        val_search = request.POST['search']
        val_type = request.POST['type']
        script = Script()
        scripts = []
        if val_type == 'title':
            scripts = script.getTitles(val_search)        
        else:
            scripts = script.getAuthors(val_search)
        return render_to_response('scripts.html', {'scripts' : scripts },
                              context_instance=RequestContext(request)) 


def index(request):    
    return render_to_response('scripts.html',
                              context_instance=RequestContext(request))
