from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    global final_amt
    lst = []
    final_amt = 0
    lst.append(request.POST.get('name'))
    lst.append(request.POST.get('name1'))
    lst.append(request.POST.get('name2'))
    lst.append(request.POST.get('name3'))
    lst.append(request.POST.get('name4'))
    lst.append(request.POST.get('name5'))
    lst.append(request.POST.get('name6'))
    lst.append(request.POST.get('name7'))
    for i in lst:
        if type(i) == int or type(i) == str:
            final_amt += int(i)
    print(lst)
    print(final_amt)
    # first_name = request.POST.get('name')
    # last_name = request.POST.get('value')
    # email = request.POST.get('value')
    # print(request.POST)
    # print(first_name)
    return render(request, "survey/base.html", {})


def home(request):
    data = request.POST.get('name')
    print(data)

def button(request):
    return (request, 'home.html', {'string': 'TESTING'})
def output(request):
    # data = "Hello, this is the output from your button!"
    # print(data)
    # data = data
    global data
    if final_amt == 8:
        data = "You appear to have minimal symptoms of depression."
    elif final_amt <= 18 and final_amt > 8:
        data = "You may be experiencing mild symptoms of depression. Consider seeking support."
    elif final_amt <= 38 and final_amt > 18:
        data = "Your depression symptoms are moderate. It's advisable to consult a healthcare professional."
    elif final_amt > 39:
        data = "Your depression symptoms are severe. Please seek immediate help."
    print(data)
    data = data
    return render(request, 'survey/base.html', {'data':data})

    # data = "Hello, this is the output from your button!"
    # print(data)
    # data = data
    # return render(request, 'survey/base.html', {'data': data})