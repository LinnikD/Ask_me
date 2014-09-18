# Create your views here.

from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.http import Http404
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from ask.models import *
from ask.forms import *

def votea(request):
    if request.method == 'POST':
        formq = VoteFormA(request.POST)
        if formq.is_valid():
            formq.save(request)
    else:
        formq = VoteFormA()
    return formq


def voteq(request):
    if request.method == 'POST':
        formq = VoteFormQ(request.POST)
        if formq.is_valid():
            formq.save(request)
    else:
        formq = VoteFormQ()
    return formq


def new(request):
    last_reg = User.objects.all().order_by('-id')[:10]
    voters_qs = VoteQuestion.objects.all().filter(autor_id = request.user.id)
    next = request.get_full_path
    q_list = Question.objects.order_by('-id')
    paginator = Paginator(q_list, 20) 
    page = request.GET.get('page')
    try:
        ques = paginator.page(page)
    except PageNotAnInteger:
        ques = paginator.page(1)
    except EmptyPage:
        ques = paginator.page(paginator.num_pages)

    form = voteq(request)

    i = 0
    A=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for q in q_list[ (ques.number-1)*20 : ques.number*20 ]:
        if voters_qs.filter(ques_id = q.id) :
            A[i] = 1
        else:
            A[i] = 0
        i+=1

    cont = {"ques": ques, "voters_qs" : voters_qs,
            "A": A, "last_reg": last_reg,
            "form": form, "next": next  }
    return render(request, 'ask/new.html', cont)


def popular(request):
    last_reg = User.objects.all().order_by('-id')[:10]

    voters_qs = VoteQuestion.objects.all().filter(autor_id = request.user.id)

    next = request.get_full_path

    q_list = Question.objects.order_by('-rating')
    paginator = Paginator(q_list, 20) 
    page = request.GET.get('page')
    try:
        ques = paginator.page(page)
    except PageNotAnInteger:
        ques = paginator.page(1)
    except EmptyPage:
        ques = paginator.page(paginator.num_pages)

    form = voteq(request)

    i = 0
    A=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for q in q_list[ (ques.number-1)*20 : ques.number*20 ]:
        if voters_qs.filter(ques_id = q.id) :
            A[i] = 1
        else:
            A[i] = 0
        i+=1

    cont = {"ques": ques, "voters_qs" : voters_qs,
            "A": A, "last_reg": last_reg,
            "form": form, "next": next  }
    return render(request, 'ask/new.html', cont)


def index(request):
    last_reg = User.objects.all().order_by('-id')[:10]
    cont = {'last_reg':last_reg}
    return render(request, 'ask/cont.html',cont)

def ind(request):
    last_reg = User.objects.all().order_by('-id')[:10]
    cont = {'last_reg':last_reg}
    return render(request, 'ask/ind.html',cont)

def ask(request):
    last_reg = User.objects.all().order_by('-id')[:10]
    form = AskForm()
    next = "/ask_me/new"
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            qid = form.save(request)
            return HttpResponseRedirect(next)
    else:
        form = AskForm()
    return render(request, "ask/ask.html", {
        'form': form,
        'next': next,
        'last_reg':last_reg
    })



def answer(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST,question_id)
        if form.is_valid():
            form.save(request, question_id)
            form = AnswerForm()
    else:
        form = AnswerForm()
    return form



def question(request, question_id): 
    last_reg = User.objects.all().order_by('-id')[:10]
    formq = voteq(request)
    qwe = Question.objects.filter(id = question_id).update(views = F('views') + 1)
    next = request.get_full_path
    form = answer(request, question_id)
    try:
        Ques = Question.objects.get(id=question_id)
        Ans = Answer.objects.filter(question_id=question_id).order_by('creation_date')
    except (ValueError, Question.DoesNotExist):
        raise Http404
    voters_qs = VoteAnswer.objects.filter(autor_id = request.user.id)

    forma = votea(request)
    C = 1
    r = VoteQuestion.objects.filter(autor_id = request.user.id ).filter(ques_id = question_id)

    if r :
        C = 0
    i = 0
    B=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for q in Ans:
        if voters_qs.filter(ans_id = q.id) :
            B[i] = 1
        else:
            B[i] = 0
        i+=1
    return render(request, 'ask/q_page.html', {'form': form, 'Question': Ques, 
                                            'Answers' : Ans, 'next': next
                                           , 'forma' : forma , 'B': B,
                                             'formq': formq , 'C':C , 'last_reg': last_reg
                                           })



def register(request):
    last_reg = User.objects.all().order_by('-id')[:10]
    next = "/ask_me/new/"
    if request.method == 'POST':
        form = MyRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                raise Http404
            rate = Rate(user_id = user.id)
            rate.save()
    else:
        form = MyRegForm()
    return render(request, "registration/register.html", {
        'form': form,
        'next': next,
        'last_reg':last_reg

    })



def user(request, u_id):
    r = Rate.objects.get(user = u_id)
    q = Question.objects.filter(author = u_id)
    a = Answer.objects.filter(author = u_id)
    last_reg = User.objects.all().order_by('-id')[:10]
    next = 'user/' + u_id
    try:
        user = get_object_or_404(User, id=u_id)
    except (ValueError, User.DoesNotExist):
        raise Http404
    return render(request, 'ask/user.html', {'user': user, 'next': next ,'last_reg': last_reg, 'r': r, 'q':q, 'a':a
                                           })




