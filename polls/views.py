from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Question,Answers,User
from django.contrib.auth.forms import UserCreationForm
from forms import PollsRegistrations


def index(request):
	name = 'prabhu'
	session_name = 'prabhu'

	if 'name' in request.COOKIES:
		name = request.COOKIES['name']

	if 'name' in request.session:
		session_name = request.session['name']

	question_list = Question.objects.order_by('-pub_date')[:3]
	template = loader.get_template('polls/index.html')
	context={
		'question_list' : question_list,
		'name' : name,
		'session_name' :session_name,	
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
	flag = "register"
	return render_to_response('polls/login.html',c)

def auth_view(request):

	username = request.POST.get('username','')
	password = request.POST.get('password','')
	token = request.POST.get('csrfmiddlewaretoken','')
	user_obj = User.objects.filter(email=request.POST.get('username',''))[0]
	if user_obj is not None:
		user_obj.token = token
		user_obj.save()
		response = HttpResponseRedirect('/polls/loggedin')
		response.set_cookie('user_id',user_obj.id)	
		request.session['user_id'] = user_obj.id
		return response
	else:
		return HttpResponseRedirect('/polls/invalid')

def loggedin(request):
	if request.session['user_id'] != "logout":
		user = User.objects.get(pk=request.session['user_id']).user_name
		return render_to_response('polls/loggedin.html',{'fullname':user })	
	else:
		user = 'logout'
		return render_to_response('polls/logout.html',{'fullname':user })
	
def invalid(request):
	return render_to_response('polls/invalid.html')

def logout(request):
	#response.set_cookie('user_id',user_obj.id)	
	#del request.session['user_id']
	request.session['user_id'] = "logout"
	return render_to_response('polls/logout.html')


def name(request, name='prabhu'):
	response = HttpResponse("Name ==== %s " % name)
	response.set_cookie('name',name)
	
	response.session['name'] = name
	return response

def register(request):
	if request.method == 'POST':
		# email = request.POST.get('email','')
		# user_name = request.POST.get('email','').split('@')[0]
		# password = request.POST.get('password','')
		# user_obj = User(email=email, user_name=user_name, password=password)
		# if user_obj.save():
		# 	return HttpResponseRedirect('polls/register_ack')			

		form = PollsRegistrations(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('polls/register_ack')	
	else:
		form = PollsRegistrations()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('polls/login.html',args)

def register_ack(request):
	return render_to_response('register_ack.html')