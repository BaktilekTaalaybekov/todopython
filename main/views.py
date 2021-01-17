from django.shortcuts import render, HttpResponse

def homepage(reguests):
    return HttpResponse("hello world")

def test(reguests):
    return render(reguests, "test.html")

