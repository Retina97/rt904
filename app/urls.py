from django.urls import path

from . import views

app_name="app"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('candidates/', views.get_candidates, name='get_candidates'),
    path('vote/', views.vote, name='vote'),
    path('results/', views.get_votes, name='get_votes'),
]
