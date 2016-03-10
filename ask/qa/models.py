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


class myUser(User):
	def do_login(login, password):
		try:
			user = User.objects.get(login=login)
		except User.DoesNotExist:
			return None
		hashed_pass = salt_and_hash(password)
		if user.password != hashed_pass:
			return None
		session = Session()
		session.key = generate_longradom_key()
		session.user = user
		session.expires = datetime.now() + timedelta(days = 5)
		session.save()
		return session.key