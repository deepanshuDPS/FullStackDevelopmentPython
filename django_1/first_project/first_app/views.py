from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

# def index(request):
#     return HttpResponse("<em>Hello World!</em>")
from first_app.models import AccessRecord, Topic, Webpage


def index(request):
    my_dict = {'insert_me': "Hello I am from first_app View.py"}
    #return render(request, 'first_app/index.html', context=my_dict)
    # request,template_file_name,dictionary or data to render
    return render(request, 'first_app/home_page.html', context=my_dict)


def index2(request):
    my_dict = {'insert_me': "Now learn about Models in Django"}
    return render(request, 'first_app/index2.html', context=my_dict)


def mtv(request):
    access_records = AccessRecord.objects.order_by('date')
    dict = {'access_records': access_records}
    return render(request, 'first_app/mtvfile.html', context=dict)


def mtv_all_data(request):
    topics = Topic.objects.all()
    dict = {}
    for i in topics:
        webpage = Webpage.objects.filter(topic=i)
        dict.update({i.top_name: webpage})
    data = {'all_records': dict}
    return render(request, 'first_app/mtvfile_all.html', context=data)


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':  # get request type
        form = forms.FormName(request.POST)  # set data to form

        if form.is_valid():  # form data is valid or not
            print('validation success')
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text:' + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})


def users(request):
    form = forms.NewUser()

    if request.method == 'POST':
        form = forms.NewUser(request.POST)
        # this is how we get validated data and save to corresponding models
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('Error Form Invalid')
    return render(request, 'first_app/sign_up.html', {'form': form})