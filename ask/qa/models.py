from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(null=True)
	rating = models.IntegerField(null=True)
	author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name="question_author")
	likes = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name="question_likes")
	def __unicode__(self):
		return self.title
	def get_url(self):
		return '/question/%d/' % self.id

class Answer(models.Model):
	added_at = models.DateField(null=True)
	text = models.TextField()
	question = models.ForeignKey(Question, null=False,on_delete=models.DO_NOTHING)
	author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
	def __unicode__(self):
		return self.text
