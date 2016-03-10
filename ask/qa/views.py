from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.http import HttpResponseRedirect
from qa.forms import AskForm, AnswerForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

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

@require_GET
def question(request, id):
	post = get_object_or_404(Question, id=id)
	answers = Answer.objects.filter(question=id)
	return render(request, 'question.html', {
		'post':	post,
		'answers': answers,
	})

def add_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.added_at = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('question', args=(post.id,)))
    else:
        form = AskForm()
    return render(request, 'add_question.html', {'form': form})

def add_answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.added_at = timezone.now()
            post.save()
            return redirect('/question/', pk=post.question)
    else:
        form = AnswerForm()
    return render(request, 'add_answer.html', {'form': form})