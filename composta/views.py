from django.shortcuts import render
def inicio (request):
    return render (request, 'composta/inicio.html')
def que_es (request):
    return render(request,'composta/que_es.html')
def como_hacer (request):
    return render(request,'composta/como_hacer.html')
