#from django.views.generic.edit import CreateView
from quiz.models.quiz import Quiz
from quiz.models.categories import Category
from quiz.models.questions import Question

from django.forms import ModelForm
from django.shortcuts import *


"""class CreateTest(CreateView):
    model = Quiz

    fields = '__all__'

    template_name = 'test/create-test.html'


class CreateQs(CreateView):
    model = Question

    fields = '__all__'

    template_name = 'test/create-qs.html'


class CreateCategory(CreateView):
    model = Category

    fields = '__all__'

    template_name = 'test/create-category.html'"""


class QuizForm(ModelForm):

	required_css_class = 'required'
	class Meta:
		model = Quiz
		fields = ('__all__')


class QuestionForm(ModelForm):

	required_css_class = 'required'
	class Meta:
		model = Question
		fields = ('__all__')
		

class CategoryForm(ModelForm):

	required_css_class = 'required'
	class Meta:
		model = Category
		fields = ('__all__')
		


def create_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = CategoryForm()

	return render(
		request, 'test/create-category.html',
        {
            'form' : form,
            'title': 'Создание категориии'
        }
    )


def create_test(request):
	if request.method == 'POST':
		form = QuizForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = QuizForm()

	return render(
		request, 'test/create-test.html',
        {
            'form' : form,
            'title': 'Создание викторины'
        }
    )


def create_qs(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = QuestionForm()

	return render(
		request, 'test/create-qs.html',
        {
            'form' : form,
            'title': 'Создание вопроса викторины'
        }
    )