from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(null=True)
	rating = models.IntegerField(null=True)
	author = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING, related_name="question_author")
	likes = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name="question_likes")
	def __unicode_(self):
		return self.title

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(null=True)
	text = models.TextField()
	question = models.ForeignKey(Question, null=False,on_delete=models.DO_NOTHING, related_name="question_ref")
	author = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
