from django import forms
from models import Question,Answers,User,Post,Likes,Comments

class PollsRegistrations(forms.ModelForm):

	class Meta:
		model = User
		fields = "__all__" 


class PostCreation(forms.ModelForm):

	class Meta:
		model = Post
		fields = "__all__"