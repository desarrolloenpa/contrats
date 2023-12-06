from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(ServiceRequest)
admin.site.register(Contract)
admin.site.register(ContractService)
admin.site.register(ContractStatus)

admin.site.register(Offer)
admin.site.register(OfferStatus)

admin.site.register(Order)

