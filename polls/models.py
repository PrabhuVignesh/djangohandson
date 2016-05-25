from __future__ import unicode_literals
import uuid
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
	def __str__(self):
		return self.question_text

	def recent_questions(self):
		return self.pub_date >= timezone.now() - datetime.timedelta	(days =1)
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


@python_2_unicode_compatible
class Answers(models.Model):
	def __str__(self):
		return self.answer_text

	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer_text = models.CharField(max_length=200)
	poles = models.IntegerField(default=0)

@python_2_unicode_compatible
class User(models.Model):
	def __str__(self):
		return self.user_name

	user_name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	token = models.CharField(max_length=200)

@python_2_unicode_compatible
class Post(models.Model):
	def __str__(self):
		return self.title

	title = models.CharField(max_length=200)
	content = models.TextField(max_length=500)
	pub_date = models.DateTimeField('date published')

@python_2_unicode_compatible
class Likes(models.Model):
	def __str__(self):
		return self.post.title

	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)

@python_2_unicode_compatible
class Comments(models.Model):
	def __str__(self):
		return self.post.title
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	comment_cnt = models.TextField()