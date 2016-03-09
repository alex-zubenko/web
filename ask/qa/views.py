from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question

def test(request, *args, **kwargs):
	return HttpResponse('OK')

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

def question(request, *args, **kwargs):
	post = Qestion.objects.filter(id=request.GET.get('id'))
	return render(request, 'home.html', {
		'post':	post,
	})
