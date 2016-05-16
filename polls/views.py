from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question,Answers


def index(request):
	question_list = Question.objects.order_by('-pub_date')[:3]
	template = loader.get_template('polls/index.html')
	context={
		'question_list' : question_list,	
	}
	return HttpResponse(template.render(context, request))


def detail(request,question_id):
	return HttpResponse("this is question:  %s." % question_id)

def results(request,question_id):
	res = "result for %s is "
	return HttpResponse(res % question_id)

def poll(request,question_id):
 	res = "question : %s"
 	return HttpResponse(res % question_id)
# Create your views here.
