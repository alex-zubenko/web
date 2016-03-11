from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.http import HttpResponseRedirect
from qa.forms import AskForm, AnswerForm, RegisterForm, LoginForm
from django.contrib.auth.models import User


#def test(request, *args, **kwargs):
#	return HttpResponse('OK')

def home(request):
	posts = Question.objects.order_by("-id")
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, limit)
	paginator.baseUrl = '/?page='
	page = paginator.page(page)
	return render(request, 'home.html', {
		'posts':	page.object_list,
		'paginator':	paginator, 'page': page,
	})


def popular(request, *args, **kwargs):
	posts = Question.objects.order_by("-rating")
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, limit)
	paginator.baseUrl = '/?page='
	page = paginator.page(page)
	return render(request, 'home.html', {
		'posts':	page.object_list,
		'paginator':	paginator, 'page': page,
	})



def add_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
        	post = form.save()
        	url = post.get_url()
        	return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'add_question.html', {'form': form})

def add_answer(request):
    if request.method == "POST":
            form = AnswerForm(request.POST)
            if form.is_valid():
            	post = form.save()
            	question = Question.objects.get(id=post.question.id)
            	url = question.get_url()
            	return HttpResponseRedirect(url)
    else:
            form = AnswerForm()
    return render(request, 'add_answer.html', {'form': form})

#@require_GET
def question(request, id):
	post = get_object_or_404(Question, id=id)
	answers = Answer.objects.filter(question=id)
	return render(request, 'question.html', {
		'post':	post,
		'answers': answers,
	})

from django.contrib import auth

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/")
	else:
		return render(request, 'login.html', {})



from django import forms
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/books/")
    else:
        data, errors = {}, {}

    return render(request, "register.html", {
        'form' : form
    })