from django.shortcuts import render
from .models import Pesan
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def api(request):
    if(request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        auth = body['secret']
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
    return HttpResponse("There's nothing here")