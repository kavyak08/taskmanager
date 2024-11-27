from django.urls import path
from MyApp import views

urlpatterns = [
    path('add_task/',views.add_task,name="add_task"),
    path('save_task/',views.save_task,name="save_task"),
    path('display_task/',views.display_task,name="display_task"),
    path('edit_task/<int:task_id>/',views.edit_task,name="edit_task"),
    path('update_task/<int:task_id>/',views.update_task,name="update_task"),
    path('delete_task/<int:task_id>/',views.delete_task,name="delete_task"),
]