from django.urls import path
from . import views

app_name = 'experiences'
urlpatterns = [
    path('<slug:slug>/', views.PostDV.as_view(), name='post'),                      # exp/<slug>/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_list'),     # exp/tag/<tag>/
]