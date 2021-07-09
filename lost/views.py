from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from .models import LostItem
from .forms import LostForm

# Create your views here.
def index(request):
    try:
        items = (LostItem.objects.filter(status=0) | LostItem.objects.filter(status=1)).order_by('-pub_date')
    except:
        raise Http404('Some error happened. Please try after sometime.')
    else:
        context = {
            'items': items, 
            'header': 'Lost items',
        }
        return render(request, 'lost/index.html', context)

def details(request, item_id):
    item = get_object_or_404(LostItem, pk=item_id)
    return render(request, 'lost/details.html', {
        'item': item, 
    })

def report(request):
    if request.method == 'POST':
        form = LostForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                item = LostItem(
                    title=form.cleaned_data['title'], 
                    description=form.cleaned_data['description'], 
                    email_id=form.cleaned_data['email_id'], 
                    pub_date=timezone.now(), 
                    picture = form.cleaned_data['picture'], 
                )
            except:
                raise Http404('Some error happened')
            else:
                item.save()
                messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(reverse('lost:index'))
        else:
            return render(request, 'lost/form.html', {
                'form': form, 
            })
    return render(request, 'lost/form.html', {
        'form': LostForm(), 
    })

def handler404(request, exception):
    context = {
        'status_code': 404, 
        'status': 'Page not found'
    }
    return render(request, 'lost/handler.html', context, status=404, )

def handler500(request):
    context = {
        'status_code': 500, 
        'status': 'Internal server error'
    }
    return render(request, 'lost/handler.html', context, status=500, )