from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.projectlistview.as_view(),name='projects_list' ),
    path('project/create', views.projectCreateview.as_view(), name= 'project_create' )

]