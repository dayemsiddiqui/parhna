from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category
from .forms import PostForm

from newsletter.models import SignUp
from newsletter.forms import SignUpForm

# Create your views here.


def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list,5) #show 5 posts per page
    categories = Category.objects.all()[:5]

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    title = "Parhna is coming soon subscribe to our newsletter"

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        subscriber = SignUp(email=form.cleaned_data['email'], full_name=form.cleaned_data['name'])
        subscriber.save()
        print "New subscriber added"

    context = {
        "template_title": title,
        "form": form,
        "object_list": posts,
        "categories": categories
    }
    return render(request, "post_index.html", context)


def post_detail(request, id=None):
    post_instance = get_object_or_404(Post, id=id)
    context = {
        "title": post_instance.title,
        "instance": post_instance
    }
    return render(request, "post-view.html", context)


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, "post_create.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Updated")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, "post_create.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:list")


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_list = Post.objects.filter(category=category)
    paginator = Paginator(posts_list,5) #show 5 posts per page
    categories = Category.objects.all()[:5]

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    title = "Parhna is coming soon subscribe to our newsletter"

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        subscriber = SignUp(email=form.cleaned_data['email'], full_name=form.cleaned_data['name'])
        subscriber.save()
        print "New subscriber added"



    context = {
        "template_title": title,
        "form": form,
        "categories": categories,
        "category": category,
        "object_list": posts
    }
    return render(request, "post_index.html", context)
