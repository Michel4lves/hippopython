from django.shortcuts import render


def indice(request):
    return render(request, 'turmas/turmas_indice.html')
