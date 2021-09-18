from django.conf.urls import url
from templetes_app import views

#TEMPLATE TAGGING :- global name for url name access app_name:url_name
app_name = 'app'

urlpatterns = [

    url(r'^index/', views.IndexView.as_view(), name = 'index'),
    url(r'^other/',views.other,name = 'other'),
    url(r'^relative/',views.relative,name = 'relative'),
]
