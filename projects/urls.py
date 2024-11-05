from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.projectlistview.as_view(),name='project_list' ),
    path('project/create', views.projectCreateview.as_view(), name= 'project_create' ),
    path('project/edit/<int:pk>', views.projectUpdateview.as_view(), name= 'project_update'),
    path('project/delete/<int:pk>', views.ProjectDeleteview.as_view(), name= 'project_delete' ),
    path('task/create', views.TaskCreateview.as_view(), name= 'Task_create' ),
    path('task/edit/<int:pk>', views.TaskUpdateview.as_view(), name= 'Task_update' ),
    path('task/delete/<int:pk>', views.TaskDeleteview.as_view(), name= 'Task_delete' ),


]