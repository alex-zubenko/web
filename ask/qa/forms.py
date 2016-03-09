from django import ModelForm

class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(ModelForm):
	class Meta:
		model = AnswerForm
		fields = ['text', 'question']