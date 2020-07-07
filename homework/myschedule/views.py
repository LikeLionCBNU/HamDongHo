from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def home(request):
    schedule = Schedule.objects
    return render(request, 'schedule/home.html', {'sch':schedule})

def detail(request, post_id):
    post_detail = get_object_or_404(Schedule, pk=post_id)
    return render(request, 'schedule/detail.html', {'post':post_detail})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
         form = PostForm()
    return render(request, 'schedule/post_new.html', {'form':form})

def post_edit(request, post_id):
    post= get_object_or_404(Schedule, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'schedule/post_edit.html', {'form':form})

def post_delete(request, post_id):
    post= get_object_or_404(Schedule, pk=post_id)
    post.delete()
    return redirect('home')