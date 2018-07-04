=====
  Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each question, visitors can shoose between a fixed number of answers.

Quick start
--------------

1. Add "polls" to your INSTALLED_APPS setting like this::
    INSTALLED_APPS = [
            ...
            'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::
    path('polls/', include('polls.url')),

3. Run 'python manage.py makemigrations polls' and  'python manage.py migrate' to create the polls models and database.

4.Start the development server via "python manage.py runserver" and visit http://127.0.0.1:8000/ to create a poll.

5.Visit http://127.0.0.1:8000/detail to join in this poll.
