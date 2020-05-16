from django.shortcuts import render
from .models import Pesan
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def api(request):
    if(request.method == "GET"):
        return HttpResponse("There's nothing here")

    if(request.method == "POST"):
        auth = dict(request.headers)['Authorization']
        allpesan = Pesan.objects.all()
        result = {
            'isError' : True,
            'nama' : '',
            'pesan' : '',
            'img': ''
        }
        for pesan in allpesan:
            if pesan.secret == auth:
                result['nama'] = pesan.nama
                result['pesan'] = pesan.story
                result['isError'] = False
                result['img'] = pesan.img
                break
        return JsonResponse(result)
