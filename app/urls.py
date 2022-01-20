from django.urls import path
from .views import kavsar,duo,mulk,rohman,salovat,bosh,new,admin


urlpatterns=[
    path('admin/',admin.as_view(),name='ad'),
    path('new/',new.as_view(),name='n'),
    path('',bosh.as_view(),name='b'),
    path('kavsar/',kavsar.as_view(),name='ka'),
    path('duo/',duo.as_view(),name='du'),
    path('taborak/',mulk.as_view(),name='mu'),
    path('rohman/',rohman.as_view(),name='ro'),
    path('salovat/',salovat.as_view(),name='sa'),

]