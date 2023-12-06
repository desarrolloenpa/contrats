from django.shortcuts import HttpResponse, redirect
from django.db.models import Q

from settings.models.local import Province, Municipality


def list_municipality_ajax(request):
    province_id = request.GET.get("province")
    municipality_id = request.GET.get("municipality")
    municipality_id = municipality_id if municipality_id != 'None' and municipality_id != 'undefined' else None
    
    municipalities = Municipality.objects.filter(province=province_id).values()

    html = "<select id='municipality' name='municipality' class='form-control form-select'>"
    html += "<option value=0>Selecione ...</option>"
    for item in municipalities:
        if municipality_id and item['id'] == int(municipality_id):
            selected = "selected='selected'"
        else:
            selected = ""
        html += "<option value='"+str(item['id'])+"'" + selected +">"+item['name']+"</option>"
    html += "</select>"

    return HttpResponse(html)