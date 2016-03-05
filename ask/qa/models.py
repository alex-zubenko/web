from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = CharField(max_length=255)
	text = TextField()
	added_at = DateField()
	rating = IntegerField()
	author = models.ForeignKey(User, null=False, on_delete=models.NO_ACTION)
	likes = models.OneToManyField(User)
	def __unicode__:
		return self.title

class Answer(models.Model):
	text = TextField()
	added_at = DateField()
	question = TextField()
	author = models.ForeignKey(User, null=False, on_delete=models.NO_ACTION)