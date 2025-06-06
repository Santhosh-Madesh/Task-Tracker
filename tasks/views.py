from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

def index(request):
    t = TaskModel.objects.all()
    if t:
        context=[]
        for field in t:
            if field.completed ==None:
                if field.is_overdue():
                    context.append(
                        {
                            'title':field.title,
                            'content':field.content,
                            'deadline':field.deadline,
                            'pk':field.pk,
                            'overdue':'Overdue',
                        })
                else:
                    context.append(
                        {
                            'title':field.title,
                            'content':field.content,
                            'deadline':field.deadline,
                            'pk':field.pk,
                            }
                            )
        return render(request,"tasks/index.html",{'context':context})
    return render(request,"tasks/index.html")

def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            deadline = form.cleaned_data['deadline']
            t = TaskModel(title=title,content=content,deadline=deadline)
            t.save()
            return redirect('index')
    form = TaskForm()
    return render(request,"tasks/create.html",{'form':form})

def about(request):
    return render(request,"tasks/about.html")

def update(request,pk):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            deadline = form.cleaned_data['deadline']
            t = TaskModel.objects.get(pk=pk)
            t.delete()
            t = TaskModel(title=title,content=content,deadline=deadline)
            t.save()
            return redirect('index')
    t = TaskModel.objects.get(pk=pk)
    title = t.title
    content = t.content
    deadline = t.deadline
    form = TaskForm(initial={"title":title,"content":content,"deadline":deadline})
    return render(request,"tasks/update.html",{'form':form,"pk":pk})

def delete(request,pk):
    t = TaskModel.objects.get(pk=pk)
    t.delete()
    return redirect('index')

def complete(request,pk):
    t = TaskModel.objects.get(pk=pk)
    t.completed=True
    t.save()    
    return redirect('index')

def completed_list(request):
    cl = TaskModel.objects.filter(completed=True)
    if cl:
        context = []
        for data in cl:
            context.append(
                {
                    'title':data.title,
                    'content':data.content,
                }
            )

        return render(request,"tasks/completed.html",{'context':context})
