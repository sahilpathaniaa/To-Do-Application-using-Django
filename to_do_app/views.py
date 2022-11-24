from django.shortcuts import render, redirect
from .forms import *
from .models import Tag, Task

# Create your views here.
def homePage(request):
    form = TaskCreate()
    tags = Tag.objects.all()
    task= Task.objects.all().order_by('-created_at')

    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        dueDate=request.POST.get('dueDate')
        status=request.POST.get('status')
        all_tags=[x.name for x in Tag.objects.all()]
        tag_id=[]
        for x in all_tags:
            if request.POST.get(x):
                tag_id.append(int(request.POST.get(x)))
        task=Task.objects.create(title=title,description=description,dueDate=dueDate, status=status)
        for x in tag_id:
            task.tag.add(Tag.objects.get(id=x))
        task.save()
        return redirect('/')    
        

    context={'form':form, 'task':task, 'tags':tags}
    return render(request, 'home.html',context)


def updatePost(request, pk):
    task = Task.objects.get(id=pk)
    tags = Tag.objects.all()
    form = TaskCreate(instance=task)
    if request.method=='POST':
        form = TaskCreate(request.POST, instance=task)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            all_tags=[x.name for x in Tag.objects.all()]
            tag_id=[]
            for x in all_tags:
                if request.POST.get(x):
                    tag_id.append(int(request.POST.get(x)))
            for x in tags:
                instance.tag.remove(Tag.objects.get(id=x.id))
            instance.save()
            for x in tag_id:
                instance.tag.add(Tag.objects.get(id=x))
            instance.save()
            return redirect('/')

    context={'form':form, 'task':task, 'tags':tags}
    return render(request, 'update.html', context)


def addTag(request):
    tags = Tag.objects.all()
    if request.method=='POST':
        tags = request.POST.get('tags')
        if not Tag.objects.filter(name=tags).exists():
            tag=Tag(name=tags)
            tag.save()
            return redirect('/')
    context = {'tags':tags}
    return render(request, 'addTag.html',context)

def deleteTags(request, pk):
    tags=Tag.objects.get(id=pk)
    tags.delete()
    return redirect('/')

def deletePost(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')