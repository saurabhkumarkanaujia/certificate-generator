from django.urls import path
from.import views
urlpatterns=[
    path('',views.user_details,name='user_details'),
    path('add_new/',views.add_new,name='add_new'),
]   
