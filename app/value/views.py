from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.core.exceptions import *
from value.models import sum
def add(request):
    result=[]
    if request.method == "POST":
        input_1 = request.POST.get('input_1')
        input_2 = request.POST.get('input_2')

        if not request.POST.get('input_1'):
            return render(request, "base.html")

        if not request.POST.get('input_2'):
            return render(request, "base.html")

        if request.POST.get('add'):
            result.append(int(input_1)+int(input_2))


        if request.POST.get('Sub'):
            result.append(int(input_1)-int(input_2))


        if request.POST.get('Mul'):
            result.append(int(input_1) *int(input_2))


        if request.POST.get('Div'):
            result.append(int(input_1)/int(input_2))
        else:
            result.append("")

        data=sum.objects.create(input1=input_1,input2=input_2,result=result[0])
        data.save()
        result={ "result":result[0]}


        return render(request, "base.html",result)

    return render(request, "base.html")