from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),                 # int:后面不能有空格
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('new/', views.new, name='new'),
]