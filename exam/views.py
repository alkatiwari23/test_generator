from django.shortcuts import render
#from . forms import *
from django.http import *
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.db.models import Q
from .models import Questions
# Create your views here.
class ExamTemplateView(TemplateView):
    template_name = 'first.html'

class ExamListView(ListView):
    model = Questions
    template_name = 'home.html'

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match= Questions.objects.filter(Q(tag__icontains=srch))

            if match:
                return render(request, 'search.html',{'sr':match})
            else:
                messages.error(request, 'No result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search.html')

class ExamDetailView(DetailView):
    model = Questions
    template_name = 'post_detail.html'
    #context_object_name = 'anything_you_want'

class ExamCreateView(CreateView):
    model = Questions
    template_name = 'post_new.html'
    fields = '__all__'