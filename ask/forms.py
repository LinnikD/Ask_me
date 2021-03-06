from django.contrib.auth.forms import UserCreationForm
from ask.models import *
from django import forms
from datetime import datetime, date, time

class MyRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
    def save(self, commit=True):
        user = super(MyRegForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            r = Rate(user = user)
            r.save()
        return user

class AskForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'Type your title here...' }))
    content = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'class': 'input-block-level','placeholder': 'Type your question here...','rows':'8'}))

    def save(self, request):
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        date = datetime.now() 
        q = Question(header=title,content=content,author=request.user,rating = 0, creation_date=date)
        q.save()
        return q.id
        
class AnswerForm(forms.Form):
    content = forms.CharField(required=False, max_length=150, widget=forms.Textarea(attrs={'class': 'input-block-level','placeholder': 'Type your answer here...','rows':'5'}))

    def save(self, request, qid):
        content = self.cleaned_data['content']
        date = datetime.now() 
        A = Answer(question_id=qid, content=content, author=request.user, rating=0, creation_date=date)
        if A.content != "" :
            A.save()

class VoteFormQ(forms.Form):
    q_id = forms.IntegerField()
    u_id = forms.IntegerField()
    ve = forms.IntegerField()
    def save(self, request):
        q_id = self.cleaned_data['q_id']
        u_id = self.cleaned_data['u_id']
        ve = self.cleaned_data['ve']
        Vot = VoteQuestion(autor_id = u_id, vot = ve, ques_id = q_id)
        Vot.save()
        q = Question.objects.all().get(id = Vot.ques_id)
        u = Rate.objects.all().get(user = q.author)
        if Vot.vot == 100:
            q.rating += 1
            q.save()
            u.rating += 1
            u.save()
        else:
            q.rating -= 1
            q.save()
            u.rating -= 1
            u.save()
              

class VoteFormA(forms.Form):
    a_id = forms.IntegerField()
    u_id = forms.IntegerField()
    ve = forms.IntegerField()
    def save(self, request):
        a_id = self.cleaned_data['a_id']
        u_id = self.cleaned_data['u_id']
        ve = self.cleaned_data['ve']
        Vot = VoteAnswer(autor_id = u_id, vot = ve, ans_id = a_id)
        Vot.save()
        q = Answer.objects.all().get(id = Vot.ans_id)
        u = Rate.objects.all().get(user = q.author)
        if Vot.vot == 100:
            q.rating += 1
            q.save()
            u.rating += 1
            u.save()
        else:
            q.rating -= 1
            q.save()
            u.rating -= 1
            u.save()


