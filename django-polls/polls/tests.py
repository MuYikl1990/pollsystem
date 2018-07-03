from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.
class QuestionTests(TestCase):
    def test_was_published_recently_with_f_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        f_question = Question(pub_date=time)
        self.assertIs(f_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):                                                      #快捷函数，封装代码
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question>'])

    def test_future_question(self):
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future question', days=10)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(reverse(url))
        self.assertQuerysetEqual(response.status_code, 404)

