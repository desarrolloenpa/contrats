from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from settings.base import list_municipality_ajax
from settings.models.user import CustomUser
from settings.models.local import Province, Municipality
from settings.models.service import Ministry

from contracts.base import TYPE_CLIENTS, BANKS
from contracts.models import Client
from contracts.forms import ClientForm

# Create your views here.

# crea un nuevo registro de servicio
def create_client(request):
    province_id = request.session.get("province_id")
    provinces = Province.objects.all()
    municipalities = Municipality.objects.filter(province_id=province_id)

    ministeries = Ministry.objects.all()

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                register = form.save()
                messages.success(request, "Cliente agregado correctamente!")
                request.session["client_id"] = register.id
                return redirect("list_client")
            except Exception as e:
                messages.error(request, str(e))
                return render(
                    request,
                    "clients/form.html",
                    {
                        'title_page': "NUEVO CLIENTE",
                        "form": form,
                        "provinces": provinces,
                        "municipalities": municipalities,
                        "ministeries": ministeries,
                        "type_clients": TYPE_CLIENTS,
                        "banks": BANKS,
                    },
                )
        else:
            messages.error(request, form.errors)
    else:
        form = ClientForm(initial={
                                    "province": province_id,
                                })
    return render(
        request,
        "clients/form.html",
        {
            'title_page': "NUEVO CLIENTE",
            "form": form,
            "provinces": provinces,
            "municipalities": municipalities,
            "ministeries": ministeries,
            "type_clients": TYPE_CLIENTS,
            "banks": BANKS,
        },
    )
    

# lista los registros de servicios
def list_client(request):
    clients = Client.objects.all().values().order_by("province", "name")
    i = 0
    for client in clients:
        clients[i]['type_client'] = TYPE_CLIENTS[client['type']]
        clients[i]['province'] = Province.objects.get(id=client['province_id'])
        clients[i]['municipality'] = Municipality.objects.get(id=client['municipality_id'])
        clients[i]['ministry'] = Ministry.objects.get(id=client['ministry_id'])
        i = i + 1

    return render(
        request,
        "clients/list.html",
        {
            'title_page': "LISTA DE CLIENTES",
            "clients": clients,
            "type_clients": TYPE_CLIENTS,
        },
    )


# edita un servicio
def edit_client(request, id):
    provinces = Province.objects.all()
    
    client = Client.objects.get(id=id)
    client_dict = client.__dict__
    form = ClientForm(initial=client_dict)
    form.fields["province"].initial = client_dict["province_id"]

    ministeries = Ministry.objects.all()
    municipalities = Municipality.objects.filter(province_id=client_dict["province_id"])

    return render(
        request,
        "clients/form.html",
        {
            'title_page': "ACTUALIZAR CLIENTE",
            "form": form,
            "client": client,
            "provinces": provinces,
            "municipalities": municipalities,
            "ministeries": ministeries,
            "type_clients": TYPE_CLIENTS,
            "banks": BANKS,
            
            "province_id": client_dict["province_id"],
            "municipality_id": client_dict["municipality_id"],
        },
    )


# actualiza la informacion de un servicio
def update_client(request, id):
    provinces = Province.objects.all()

    client = Client.objects.get(id=id)
    client_dict = client.__dict__

    ministeries = Ministry.objects.all()
    municipalities = Municipality.objects.filter(province_id=client_dict["province_id"])
    
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            try:
                form.save()
                request.session["client_id"] = id
                messages.success(request, "Cliente actualizado correctamente!")
                return redirect("list_client")
            except Exception as e:
                messages.error(request, str(e))
                return render(
                    request,
                    "clients/form.html",
                    {
                        'title_page': "ACTUALIZAR CLIENTE",
                        "form": form,
                        "provinces": provinces,
                        "municipalities": municipalities,
                        "ministeries": ministeries,
                        "type_clients": TYPE_CLIENTS,
                        "banks": BANKS,
                    },
                )
        else:
            messages.error(request, form.errors)
    else:
        form = ClientForm(instance=client)
    return render(
        request,
        "clients/form.html",
        {
            'title_page': "ACTUALIZAR CLIENTE",
            "form": form,
            "provinces": provinces,
            "municipalities": municipalities,
            "ministeries": ministeries,
            "type_clients": TYPE_CLIENTS,
            "banks": BANKS,
        },
    )
    


# actualiza la informacion de un servicio
def delete_client(request, id):
    client = Client.objects.get(id=id)
    try:
        client.delete()
        messages.success(request, "Cliente eliminado del sistema!")
    except Exception as e:
        messages.error(request, str(e))
    return redirect("list_client")