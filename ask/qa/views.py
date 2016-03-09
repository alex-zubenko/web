from django.shortcuts import render

from django.http import HttpResponse
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
	return HttpResponse('OK')
"""
def home(request):
	return HttpResponse('OK')
	posts = Question.objects.filter()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, limit)
	paginator.baseUrl = '/?page='
	page = paginator.page(page)
	return render(request, 'qa/home_list.html', {
		posts:			page.object_list,
		paginator:	paginator,
		page:				page,
	})

def popular(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, *args, **kwargs):
	return HttpResponse('OK')
"""