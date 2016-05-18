from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Question,Answers


def index(request):
	question_list = Question.objects.order_by('-pub_date')[:3]
	template = loader.get_template('polls/index.html')
	context={
		'question_list' : question_list,	
	}
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)


def detail(request,question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question is not exist")
	return render(request, 'polls/detail.html',{'question':question})

def results(request,question_id):
	res = "result for %s is "
	return HttpResponse(res % question_id)

def poll(request,question_id):
 	res = "question : %s"
 	return HttpResponse(res % question_id)
# Create your views here.

def login(request):
	c ={}
	c.update(csrf(request))
	return render_to_response('polls/login.html', c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')

def loggedin(request):
	return render_to_response('polls/loggedin.html',{'fullname': request.user.username})

def invalid(request):
	return render_to_response('polls/invalid.html')

def logout(request):
	auth.logout(request)
	return render_to_response('polls/logout.html')