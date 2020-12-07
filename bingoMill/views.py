from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Bingo


def edit(request):
    return render(request, 'bingoMill/edit.html')


def museum(request):
    bingo_list = Bingo.objects.all()
    print(list(bingo_list)[0].id)
    # rows = json.dumps(list(bingo_list), cls=DjangoJSONEncoder)
    context = {'bingo_list': list(bingo_list)}

    return render(request, 'bingoMill/museum.html', context)


def detail(request, bingo_id):
    bingo = get_object_or_404(Bingo, pk=bingo_id)
    return render(request, 'bingoMill/detail.html', {"bingo_id": bingo_id})


def index(request):
    # latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'bingoMill/index.html')


@csrf_exempt
def upload(request):
    post_dict = request.POST.dict()
    bingo_instance = Bingo()
    bingo_instance.title = post_dict.get("title")
    bingo_instance.username = post_dict.get("username")
    bingo_instance.password = post_dict.get("password")
    bingo_instance.words = post_dict.get("words")
    bingo_instance.words_size = post_dict.get("words_size")
    bingo_instance.save()
    return render(request, 'bingoMill/edit.html')

# Create your views here.
