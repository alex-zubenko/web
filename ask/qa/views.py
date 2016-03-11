from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.http import HttpResponseRedirect
from qa.forms import AskForm, AnswerForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

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
        	post = form.save(commit=False)
        	post.author = request.user
        	post.save()
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


def do_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			return render(request, 'login.html', {})
	else:
		return render(request, 'login.html', {})

def register( request ):
  user = User()
  if request.method == "POST":
    userForm = UserForm( request.POST )
    if userForm.is_valid():
      userData = userForm.cleaned_data
      user.username = userData['username']
      user.email = userData['email']
      user.set_password( userData['password'] )
      user.save()
      user = authenticate( username = userData['username'], password = userData['password'] )
      login(request, user)
      return HttpResponseRedirect( "/" )
  else:
    userForm = UserForm()
  return render( request, "register.html", { "user": user, "form": userForm } )