from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request,pk='Hello Fucktards'):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk): #pk is getting passed through the <a href "{% 
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':        #request.POST holds the POST data from the html
        form = PostForm(request.POST) 
        
        if form.is_valid():
            post = form.save(commit=False) #commit=False means that we don't want to save the Post model yet
            post.author = request.user
            post.published_date = timezone.now()
            post.save() #then we save it
            return redirect('post_detail', pk=post.pk) # to pass through urls
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})
 

