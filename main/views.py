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

def delete_todo(reguest, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(reguest, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(reguest, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(reguest, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)