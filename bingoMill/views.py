from django.shortcuts import render


def edit(request):
    return render(request, 'bingoMill/edit.html')


def museum(request):
    return render(request, 'bingoMill/museum.html')

def detail(request, bingo_id):
    return render(request, 'bingoMill/detail.html',{"bingo_id":bingo_id})

def index(request):
    # latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'bingoMill/index.html')


# Create your views here.
