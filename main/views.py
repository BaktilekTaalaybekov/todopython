from django.shortcuts import render, HttpResponse

def homepage(reguests):
    return render(reguests, "index.html")

def test(reguests):
    return render(reguests, "test.html")

def second(reguest):
    return HttpResponse("test 2 page")

def third(reguest):
    return HttpResponse("test 3 page")