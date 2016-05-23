from django import forms
from models import Answers,Question,User

class PollsRegistrations(forms.ModelForm):

	class Meta:
		model = User
		