from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer, myUser
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





def login(request, *args, **kwargs):
	return HttpResponse('OK')

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            sessid = do_login(user.username,user.password)
            if sessid:
            	response = HttpResponseRedirect('/')
            	response.set_cookie('sessid',sessid,
            		domain="site.com", httponly=True,
            		expires=datetime.now()+timedelta(days=5))
            return response
        else:
            print user_form.errors
    else:
        user_form = RegisterForm()
    return render( request, 'register.html', {'form': user_form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
    	#form = LoginForm()
        return render(request, 'login.html', {})