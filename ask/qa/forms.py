from django import forms
from django.forms import ModelForm
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']

class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

