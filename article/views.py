from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from .models import Article, Comment, Newsletter, newsletter_File
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from projects.models import Project
from events.models import Event
from products.models import Product

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        newsletters = Newsletter.objects.filter(title__contains=keyword)
        return render(request, "Newsletter.html", {"newsletters": newsletters})
    newsletters = Newsletter.objects.all()

    return render(request, "articles.html", {"newsletters": newsletters})

def newsletters(request):
    keyword = request.GET.get("keyword")

    if keyword:
        newsletters = Newsletter.objects.filter(title__contains=keyword)
        return render(request, "newsletters.html", {"newsletters": newsletters})
    newsletters = Newsletter.objects.all()

    return render(request, "newsletters.html", {"newsletters": newsletters})


@login_required(login_url="user:login")
def dashboard(request):
    projects = Project.objects.filter(author=request.user)
    events = Event.objects.filter(author=request.user)
    articles = Article.objects.filter(author=request.user)
    products = Product.objects.filter(author=request.user)
    context = {
        "projects": projects,
        "article": articles,
        "events": events,
        "products": products
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Article Created Successfully!!!")
        return redirect("article:dashboard")
    return render(request, "addarticle.html", {"form": form})


def detail(request, id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)

    comments = article.comments.all()
    return render(request, "detail.html", {"article": article, "comments": comments})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Article Successfully Updated")
        return redirect("article:dashboard")

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)

    article.delete()

    messages.success(request, "Article Successfully Deleted")

    return redirect("article:dashboard")


def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail", kwargs={"id": id}))



def index(request):
    return render(request, "index.html")

def register(request):
    return(request, "register.html")

def about(request):
    return render(request, "about.html")

def events(request):
    return(request, "events.html")

def IPD(request):
    return render(request, "IPD.html")

def Publications(request):
    return render(request, "Publications.html")

def Collaborators(request):
    return render(request, "Collaborators.html")

def Conferences(request):
    return render(request, "Conferences.html")

def members(request):
    return render(request, "members.html")

