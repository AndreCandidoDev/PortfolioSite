from django.shortcuts import render


def curriculo(request):
    return render(request, 'curriculo/curriculo.html')