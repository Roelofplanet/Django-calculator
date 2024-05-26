from django.shortcuts import render
import math


# Homepage
def home(request):
    return render(request, 'home.html')


# Basis Calculator
def count(request):
    return render(request, 'count.html')

def result(request):
    num1 = float(request.GET.get('number1'))
    num2 = float(request.GET.get('number2'))

    
    if request.GET.get('add') == "":
        ans = num1 + num2

    elif request.GET.get('subtract') == "":    
        ans = num1 - num2

    elif request.GET.get('multiply') == "":    
        ans = num1 * num2

    else:
        ans = num1 / num2

    return render(request, 'result.html', {'ans': ans})


# Kwadraat en wortel trekken
def kwadraat(request):
    return render(request, 'kwadraat.html')

def result_kwadraat(request):
    num1 = float(request.GET.get('number1'))

    
    if request.GET.get('kwadraat') == "":
        ans = num1**2

    else:
        ans = math.sqrt(num1)

    return render(request, 'result_kwadraat.html', {'ans': ans})


# Circel omtrek
def circel_omtrek(request):
    return render(request, 'circel_omtrek.html')

def result_circel_omtrek(request):
    num1 = float(request.GET.get('number1'))

    if request.GET.get('circel_omtrek') == "":
        ans = math.pi*(num1)

    return render(request, 'result_circel_omtrek.html', {'ans': ans})


# Circel Oppervlakte
def circel_oppervlakte(request):
    return render(request, 'circel_oppervlakte.html')

def result_circel_oppervlakte(request):
    num1 = float(request.GET.get('number1'))

    if request.GET.get('circel_oppervlakte') == "":
        ans = math.pi*(num1)**2

    return render(request, 'result_circel_oppervlakte.html', {'ans': ans})


# Modulo
def modulo(request):
    return render(request, 'modulo.html')

def result_modulo(request):
    num1 = float(request.GET.get('number1'))
    num2 = float(request.GET.get('number2'))

    if request.GET.get('modulo') == "":
        ans = num1 % num2

    return render(request, 'result_modulo.html', {'ans': ans})


# Relativiteitstheorie
def relativiteitstheorie(request):
    return render(request, 'relativiteitstheorie.html')

def result_relativiteitstheorie(request):
    num1 = float(request.GET.get('number1'))

    if request.GET.get('relativiteitstheorie') == "":
        ans = num1 * 300000**2

    return render(request, 'result_relativiteitstheorie.html', {'ans': ans})



    








