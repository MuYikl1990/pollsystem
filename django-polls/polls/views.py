from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .form import QuestionForm, ChoiceForm

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def get_queryset(self):                                   #该函数返回一个需要的对象列表
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:4]

class DetailView(generic.DetailView):           #通用视图是类
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        error_message = "You didn't select a choice"
        context ={'question': question, 'error_message': error_message}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def new(request):
    if request.method != 'POST':
        q_form = QuestionForm()
        c1_form = ChoiceForm()
        c2_form = ChoiceForm()
        c3_form = ChoiceForm()
    else:
        q_form = QuestionForm(request.POST)
        c1_form = ChoiceForm(request.POST)
        c2_form = ChoiceForm(request.POST)
        c3_form = ChoiceForm(request.POST)
        if q_form.is_valid() and c1_form.is_valid() and c2_form :
            q = q_form.save(commit=False)
            q.save()
            c1 = c1_form.save(commit=False)
            c1.save()
            c2 = c2_form.save(commit=False)
            c2.save()
            c3 = c3_form.save(commit=False)
            c3.save()
            q.choice_set.add(c1,c2,c3)
            c1.save()
            c2.save()
            c3.save()

            return HttpResponseRedirect(reverse('polls:index'))

    context ={'q_form': q_form, 'c1_form': c1_form, 'c2_form': c2_form, 'c3_form': c3_form}
    return render(request, 'polls/new.html', context)

'''
def get_context_data():
    pass

def get_object():
    pass
'''
