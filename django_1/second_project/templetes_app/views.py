from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.

def index(request):
    cont_dict = {'text':'hello world','num':100}
    return render(request,'app/index.html',cont_dict)

def other(request):
    return render(request,'app/other.html')

def relative(request):
    return render(request,'app/relative_url_templates.html')

class CBView(View):

    def get(self,request):
        return HttpResponse("Class based views are cool!")

class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = 'hello world'
        return context
