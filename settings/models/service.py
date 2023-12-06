from django.db import models

from settings.models.user import CustomUser

# Create your models here.

# definicion de tipos de servicios ofertados
class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value_cup = models.FloatField(null=True, blank=False, help_text="Valor CUP segun la norma")
    value_usd = models.FloatField(null=True, blank=False, help_text="Valor USD segun la norma")
    
    description = models.TextField(null=True, blank=False)
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="service_type_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "tb_service_types"

    def __str__(self):
        return self.name
    

# Ministerios o OSDEs a considerar    
class Ministry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    acronym = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Siglas o acronico del organismo")
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, related_name="Ministry_user_fk")
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "tb_ministeries"

    def __str__(self):
        return self.acronym