from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo

def homepage(reguests):
    return render(reguests, "index.html")

def test(reguests):
    todo_list = ToDo.objects.all()
    return render(reguests, "test.html", {"todo_list": todo_list})

def second(reguest):
    return HttpResponse("test 2 page")

def third(reguest):
    return HttpResponse("test 3 page")

def add_todo(reguest):
    form = reguest.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)