
from django.conf.urls import url
from first_app import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^index2',views.index2,name = 'index2'),
    url(r'^mtv/',views.mtv,name= 'mtv'),
    url(r'^mtv_all/',views.mtv_all_data,name="all_data"),
    url(r'^form_view/',views.form_name_view,name = "form_name"),
    url(r'^sign_up/',views.users,name="sign_up")

]
