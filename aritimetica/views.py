from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def somar(request):
    if (request.POST):
        n1 = float(request.POST.get('n1'))
        n2 = float(request.POST.get('n2'))
        res = n1 + n2
        return render(request, 'index.html', {'resp': res})
    else:
        return redirect('/calc/')


def subtrair(request):
    if (request.POST):
        n1 = float(request.POST.get('n1'))
        n2 = float(request.POST.get('n2'))
        res = n1 - n2
        return render(request, 'index.html', {'resp': res})
    else:
        return redirect('/calc/')

def multiplicar(request):
    if (request.POST):
        n1 = float(request.POST.get('n1'))
        n2 = float(request.POST.get('n2'))
        res = n1 * n2
        return render(request, 'index.html', {'resp': res})
    else:
        return redirect('/calc/')

def dividir(request):
    if (request.POST):
        n1 = float(request.POST.get('n1'))
        n2 = float(request.POST.get('n2'))
        res = n1 / n2
        return render(request, 'index.html', {'resp': res})
    else:
        return redirect('/calc/')