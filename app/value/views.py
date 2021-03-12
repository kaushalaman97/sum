from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.core.exceptions import *

def add(request):
    if request.method == "POST":
        input_1 = request.POST.get('input_1')
        input_2 = request.POST.get('input_2')

        if request.POST.get('add'):
            result=int(input_1)+int(input_2)
            result={
                "result":result
            }
            print(result)
            return render(request, "base.html",result)

        if request.POST.get('Sub'):
            result=int(input_1)-int(input_2)
            result={
                "result":result
            }
            print(result)
            return render(request, "base.html",result)


        if request.POST.get('Mul'):
            result=int(input_1) *int(input_2)
            result={
                "result":result
            }
            print(result)
            return render(request, "base.html",result)



        if request.POST.get('Div'):
            result=int(input_1)/int(input_2)
            result={
                "result":result
            }
            print(result)
            return render(request, "base.html",result)

    return render(request, "base.html")