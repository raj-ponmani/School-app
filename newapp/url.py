from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index, name='index'),
    path('form.html',views.form, name='form'),
    path('result',views.result, name ='result')

]
urlpatterns += staticfiles_urlpatterns()