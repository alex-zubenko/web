from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import Page
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
		posts:	page,
		paginator:	paginator, page: page,
	})


def popular(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, *args, **kwargs):
	return HttpResponse('OK')
