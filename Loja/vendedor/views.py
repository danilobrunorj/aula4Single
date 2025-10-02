from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Cliente

def listar_clientes(request):

    if request.method != "GET":

        return HttpResponseNotAllowed(["GET"])
    clientes = Cliente.objects.all().order_by("nome").values("id","nome","email","ativo")
    return JsonResponse(list(clientes), safe=False)
