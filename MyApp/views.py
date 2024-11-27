from django.shortcuts import render,redirect
from MyApp.models import Task
# Create your views here.
def add_task(request):
    return render(request,"add_task.html")

def save_task(request):
    if request.method == "POST":
        a = request.POST.get('student')
        b = request.POST.get('batch')
        c = request.POST.get('tutor')
        d = request.POST.get('task')
        e = request.POST.get('desc')

        obj = Task(Student=a,Batch=b,Tutor=c,Task_title=d,Description=e)
        obj.save()
        return redirect(add_task)

def display_task(request):
        data = Task.objects.all

        return render(request,"display_task.html",{'data':data})

def edit_task(request,task_id):
    task = Task.objects.get(id=task_id)
    return render(request,"edit_task.html",{'task':task})

def update_task(request,task_id):
    if request.method == "POST":
            a = request.POST.get('student')
            b = request.POST.get('batch')
            c = request.POST.get('tutor')
            d = request.POST.get('task')
            e = request.POST.get('desc')

    Task.objects.filter(id=task_id).update(Student=a,Batch=b,Tutor=c,Task_title=d,Description=e)
    return redirect(display_task)

def delete_task(request,task_id):
    dlt = Task.objects.filter(id=task_id)
    dlt.delete()
    return redirect(display_task)

