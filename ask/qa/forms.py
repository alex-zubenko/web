from django import forms
from django.forms import ModelForm
from qa.models import Question, Answer

class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']

class RegisterForm(ModelForm):
	class Meta:
		model = User
		#fields = ['name', 'email', 'password']

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['name', 'password']

