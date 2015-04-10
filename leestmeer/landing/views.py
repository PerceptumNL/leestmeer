from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.db.models import Avg, Count
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Block

def home(request):
    blocks = Block.objects.all().select_subclasses()
    
    return render(request, 'landing/index.html', {
        'blocks': blocks,
    })
