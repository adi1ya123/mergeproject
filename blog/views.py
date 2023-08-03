from django.shortcuts import render
from django.utils import timezone
from .models import Post, User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm, UserForm, LoginForm, ProfileForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .forms import ProfileEditForm
from .models import Category
from .models import Tag
# from .forms import ReplyForm
from .models import Comment


def post_list(request):
   posts = Post.objects.all()
   return render(request,'blog/post_list.html',{'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    new_comment = None
    parent=None

    if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
            try:
                parent = request.POST.get('comment_id')
                parent = Comment.objects.filter(id=parent).last()
            except:
                parent=None

            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.parent = parent
            new_comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form, 'parent':parent})

def post_new(request):
    if request.method == "POST":
       form = PostForm(request.POST, request.FILES)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.tag.set(form.cleaned_data.get('tag'))
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if  form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.password = make_password(passworCommentsd)
            user=form.save()
            login(request, user)
            return redirect('blog:login')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if  form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
               login(request, user)
            return redirect('blog:post_list')
            
        else:
            form = 'Invalid username or password'  
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


@login_required
def profile(request):
    user = User.objects.filter(id=request.user.id).last()
    return render(request, 'blog/profile.html', {'user':user})

@login_required
def profile_edit(request):
    user = User.objects.filter(id=request.user.id)
    if  request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES ,instance=request.user)
        if form.is_valid():
           form.save()
        return redirect('blog:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/profile_edit.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('blog:login')

def post_Category(request, id):
    posts = Post.objects.filter(category_id=id)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_Tag(request, id):
    posts = Post.objects.filter(tag__id=id)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_author(request, id):
    posts = Post.objects.filter(author__id=id)
    return render(request, 'blog/post_list.html', {'posts':posts})

# def post_Published_date(request, slug):
#     published = Post.objects.filter(published_date=slug).last()
#     posts = Post.objects.filter(published_date=published).all()
#     return render(request, 'blog/postdatefil.html', {'posts':posts})
        


        
