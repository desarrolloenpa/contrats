from django.shortcuts import HttpResponse, redirect
from django.db.models import Q


TYPE_CLIENTS = {
    "PN"    : "Persona Natural",
    "TCP"   : "Trabajador por Cuenta Propia",
    "PRO"   : "Productor Agropecuario",
    "CNA"   : "Cooperativa No Agropecuaria",
    "CPA"   : "Cooperativa Agropecuaria",
    "PYME"  : "Empresa Privada",
    "EES"   : "Empresa Estatal",
    "EM"    : "Empresa Mixta",
}


BANKS= {
    "BPA"    : "Banco Popular de Ahorro",
    "BANDEC"   : "Banco de Credito y Comercio",
    "BM"   : "Banco Metropolitano",
    "BFI"   : "Banco Financiero Internacional",
}

