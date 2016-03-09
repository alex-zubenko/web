from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer

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

@require_GET
def question(request, id):
	post = get_object_or_404(Question, id=id)
	answers = Answer.question_set.all()
	return render(request, 'question.html', {
		'post':	post,
		'answers': answers,
	})
