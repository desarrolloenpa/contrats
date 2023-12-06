from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from contracts.views import index
from contracts.views import contract, client

urlpatterns = [
    path("", index.index, name="index"),
    path("index", index.index, name="index"),
     
    # crud para los clientes
    path("list_client/", client.list_client, name="list_client"),
    path("create_client/", client.create_client, name="create_client"),
    path("edit_client/<int:id>/", client.edit_client, name="edit_client"),
    path("update_client/<int:id>/", client.update_client, name="update_client"),
    path("delete_client/<int:id>/", client.delete_client, name="delete_client"),    
    
    # crud para servicios
    path("list_contract/", contract.list_contract, name="list_contract"),
    path("create_contract/", contract.create_contract, name="create_contract"),
    path("edit_contract/", contract.edit_contract, name="edit_contract"),
    path("delete_contract/", contract.delete_contract, name="delete_contract"),
]
