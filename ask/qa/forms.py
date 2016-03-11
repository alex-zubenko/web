from django import forms
from django.forms import ModelForm
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class UserForm( forms.ModelForm ):
  email = forms.EmailField(required = True)
  class Meta:
  	model = User
  	fields = ('username', 'email', 'password')
