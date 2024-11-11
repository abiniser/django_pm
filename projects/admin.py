from django.contrib import admin
from . import models
from django.db.models import Count
# Register your models here.
# this for adding things into the admin page
admin.site.register(models.category)

#this for add ing new row into one of category
@admin.register(models.projects)
class projectadmin(admin.ModelAdmin):
    list_display=['title','status','user','category','created_at','tasks_count']
    list_per_page=20
    list_editable = ['status']
#this for avoid to many sql 
    list_select_related = ['user','category']

    def tasks_count(self,obj):
        #return obj.task_set.count()
        return obj.tasks_count
    #this for avoid sql in every task count
    def get_queryset(self, request):
        query =  super().get_queryset(request)
        query = query.annotate(task_count=Count('task'))
        return query



@admin.register(models.task)
class projectadmin(admin.ModelAdmin):
    list_display=['id','description','is_complete','project']
    list_per_page=20
    list_editable = ['is_complete']
#this for avoid to many sql 

