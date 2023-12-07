from django.db import models
from settings.models import service

from settings.models.user import CustomUser
from settings.models.local import Province, Municipality
from settings.models.service import Ministry, ServiceType

# Create your models here.

# Identificacion del cliente
class Client(models.Model):
    type = models.CharField(max_length=6, null=False, blank=False, help_text="Tipo de cliente")
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Nombre de la empresa")
    acronym = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Siglas o acronico de la empresa")
    
    first_name = models.CharField(max_length=50, unique=False, null=True, help_text="Nombre del Representante")
    last_name = models.CharField(max_length=50, unique=False, null=True, help_text="Apellidos del Representante")
    company_position = models.CharField(max_length=80, null=True, blank=False, help_text="Cargo del Representante")

    province = models.ForeignKey(Province, null=False, blank=False, on_delete=models.RESTRICT, related_name="client_province_fk")
    municipality = models.ForeignKey(Municipality, null=False, blank=False, on_delete=models.RESTRICT, related_name="client_municipality_fk")
    address = models.CharField(max_length=100, unique=True, null=False)
    
    email = models.EmailField(max_length=80, null=True, blank=False)
    telephone = models.CharField(max_length=80, null=True, blank=False)
    
    bank = models.CharField(max_length=80, null=True, blank=False, help_text="Datos de Banco")
    bank_branch = models.CharField(max_length=80, null=True, blank=False, help_text="Datos de Sucursal bancaria")
    account_usd = models.CharField(max_length=20, null=True, blank=False, help_text="Cuenta USD")
    account_cup = models.CharField(max_length=20, null=True, blank=False, help_text="Cuenta CUP")
    
    description = models.TextField(null=True, blank=False)
    ministry = models.ForeignKey(Ministry, null=False, blank=False, on_delete=models.RESTRICT, 
                                 help_text="Organismo al que pertenece la empresa")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="client_user_logged_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tb_clients"

    def __str__(self):
        return self.name
    

# Registro de solicitudes de servicio
class ServiceRequest(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Descripcion rapida del servicio")
    
    number = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=50, unique=False, null=True, help_text="Nombre del Solicitante")
    last_name = models.CharField(max_length=50, unique=False, null=True, help_text="Apellidos del Solicitante")
    company_position = models.CharField(max_length=80, null=True, blank=False, help_text="Cargo del Solicitante")
    
    email = models.EmailField(max_length=80, null=True, blank=False)
    telephone = models.CharField(max_length=80, null=True, blank=False)
    
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=True, related_name="service_client_fk")
    description = models.TextField(null=True, blank=False)
    
    user_receiving = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=False, 
                                       related_name="service_user_receiving_fk", help_text="Usuario que registro el servicio")
    date_receiving = models.DateTimeField(null=False)
    
    user_approved = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, 
                                    related_name="service_user_approved_fk", help_text="Usuario que registro el servicio")
    date_approved = models.DateTimeField(null=True, blank=False)
    
    user_assigned = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, 
                                    related_name="service_user_aproved_fk", help_text="Usuario que registro el servicio")
    date_assigned = models.DateTimeField(null=True, blank=False)
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="service_request_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tb_servicies"

    def __str__(self):
        return self.number



# Registro del contrato
class Contract(models.Model):
    type = models.CharField(max_length=3, null=False, blank=False, help_text="Tipo de contrato u orden de trabajo")
    number = models.CharField(max_length=8, unique=True, null=False, blank=False, help_text="Numero de contrato")
    title = models.CharField(max_length=100, null=False, blank=False, help_text="Titulo del contrato")
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=False, blank=False)
    service = models.ForeignKey(ServiceRequest, on_delete=models.RESTRICT, null=False, blank=False)
    contract= models.ForeignKey('self', on_delete=models.RESTRICT, null=False, blank=False, 
                                related_name="contract_contract_fk", help_text="Contrato primario")
    
    user_receiving = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=False, 
                                       related_name="contract_user_receiving_fk", help_text="Usuario que registro el servicio")
    date_receiving = models.DateTimeField(null=False)
    
    user_manager = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="contract_user_manager_fk")    
    
    value_cup = models.FloatField(null=True, blank=False, help_text="valor CUP de todo los servicios")
    value_usd = models.FloatField(null=True, blank=False, help_text="valor USD de todo los servicios")
    
    date_elaboration = models.DateTimeField(null=False, blank=False, help_text="Fecha de elaboración")
    date_receiving = models.DateTimeField(null=False, blank=False, help_text="Fecha de recibida")
    date_circulation = models.DateTimeField(null=False, blank=False, help_text="Fecha de circulación a las areas")
    date_committed_presentation = models.DateTimeField(null=False, blank=False, help_text="Fecha de circulación al comite")
    date_committed_approved = models.DateTimeField(null=False, blank=False, help_text="Fecha de aprobacion por comite")
    date_client_signature = models.DateTimeField(null=False, blank=False, help_text="Fecha de firma por el cliente")
    date_approved = models.DateTimeField(null=False, blank=False, help_text="Fecha de aprobación")
    date_start = models.DateTimeField(null=False, blank=False, help_text="Fecha de inicio")
    date_end = models.DateTimeField(null=False, blank=False, help_text="Fecha de terminación")
    
    description = models.TextField(null=True, blank=True, help_text="Descripcion del objeto del contrato")
    observation = models.TextField(null=True, blank=True, help_text="Observaciones posibles al contrato en cualquier momento")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="contract_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tb_contracts"

    def __str__(self):
        return self.number



# Realacion de los servicios de un contrado
class ContractService(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=False, blank=False)
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT, null=False, blank=False)
    service = models.ForeignKey(ServiceType, on_delete=models.RESTRICT, null=False, blank=False)
    
    description = models.TextField(null=True, blank=False)
    value_cup = models.FloatField(null=True, blank=False, help_text="Valor CUP del servicio en particular")
    value_usd = models.FloatField(null=True, blank=False, help_text="Valor USD del servicio en particular")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="contract_service_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        db_table = "tb_contract_services"

    def __str__(self):
        return [self.client, self.service]



# Trazabilidad al estado del contarto
class ContractStatus(models.Model):
    status = models.CharField(max_length=20, unique=True, null=False, blank=False, help_text="Estado del contrato")
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT, null=False, blank=False, related_name="contract_status_contract_fk")
    date_register = models.DateTimeField(null=False, blank=False, help_text="Fecha de tregistro del estado")
    observation = models.TextField(null=True, blank=True, help_text="Observaciones posibles al contrato en cualquier momento")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="contract_status_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
     
    class Meta:
        db_table = "tb_contract_status"

    def __str__(self):
        return [self.contract, self.status]    



# Registro de oferta técnico Económica
class Offer(models.Model):
    number = models.CharField(max_length=8, unique=True, null=False, blank=False, help_text="Numero de la oferta")
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, null=False, blank=False, 
                               related_name="offer_client_fk")
    service = models.ForeignKey(ServiceType, on_delete=models.RESTRICT, null=False, blank=False, 
                                related_name="offer_service_fk")
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT, null=False, blank=False, 
                                 related_name="offer_contract_fk")
    
    value_cup = models.FloatField(null=True, blank=False, help_text="valor CUP de todo los servicios")
    value_usd = models.FloatField(null=True, blank=False, help_text="valor USD de todo los servicios")
    observation = models.TextField(null=True, blank=True, help_text="Observaciones a la oferta")
    
    date_elaboration = models.DateTimeField(null=False, blank=False, help_text="Fecha de elaboración")
    user_client_receiving = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, 
                                    related_name="offer_user_client_receiving_fk", help_text="Especialista comercial que entrega")
    date_client_receiving = models.DateTimeField(null=False, blank=False, help_text="Fecha de recibida por el cliente")
    date_approved = models.DateTimeField(null=False, blank=False, help_text="Fecha de aprobación por el cliente")
    
    user_receiving = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, 
                                       related_name="offer_user_receiving_fk", help_text="Especialista comercial que recibe")
    date_receiving = models.DateTimeField(null=False, blank=False, help_text="Fecha de entrega al especialista comercial")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="work_order_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        db_table = "tb_offers"

    def __str__(self):
        return [self.number, self.contract]    
    

# Trazabilidad del estado de la oferta tecnica comercial
class OfferStatus(models.Model):
    status = models.CharField(max_length=20, unique=True, null=False, blank=False, help_text="Estado del contrato")
    offer = models.ForeignKey(Offer, on_delete=models.RESTRICT, null=False, blank=False, 
                              related_name="offer_status_contract_fk")
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT, null=False, blank=False, related_name="offer_status_contract_fk")
    date_register = models.DateTimeField(null=False, blank=False, help_text="Fecha de tregistro del estado")
    observation = models.TextField(null=True, blank=True, help_text="Observaciones posibles al contrato en cualquier momento")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="offer_status_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
     
    class Meta:
        db_table = "tb_offer_status"

    def __str__(self):
        return [self.offer, self.status]   
    

# Ordenes de trabajo
class Order(models.Model):
    number = models.CharField(max_length=8, unique=True, null=False, blank=False, help_text="Numero de la orden")
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT, null=False, blank=False, related_name="order_contract_fk")
    description = models.TextField(null=True, blank=False)
    
    date_elaboration = models.DateTimeField(null=False, blank=False, help_text="Fecha de elaboración")
    date_receiving = models.DateTimeField(null=False, blank=False, help_text="Fecha de recibida")
    date_approved = models.DateTimeField(null=False, blank=False, help_text="Fecha de aprobación")
    date_approved = models.DateTimeField(null=False, blank=False, help_text="Fecha  de cierre de la orden")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="order_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        db_table = "tb_orders"

    def __str__(self):
        return [self.number, self.contract]
