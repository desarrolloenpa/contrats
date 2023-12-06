from django.db import models
from django.contrib.auth.models import AbstractUser, GroupManager


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_position = models.ForeignKey('CompanyPosition', on_delete=models.SET_NULL, null=True, blank=False)
    role = models.SmallIntegerField(null=True, blank=False)
    salary_scale = models.ForeignKey('SalaryScale', on_delete=models.SET_NULL, null=True)
    
    email = models.EmailField(max_length=80, null=False, blank=False, unique=True, default="desarrollo@local.local")
    telephone = models.CharField(max_length=80)
    
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tb_users"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Grupo de usuarios 
class Group(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True)
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, blank=False, related_name='Group_user_fk')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "tb_groups"
  
    def __str__(self):
        return self.name
    

# Usuarios en los grupos
class GroupUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name="GroupUser_user_fk")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name="GroupUser_group_fk")
    
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
     
    class Meta:
        db_table = "tb_group_users"

    def __str__(self):
        return [self.group, self.user]  


    
# Escala salarial    
class SalaryScale(models.Model):
    number = models.CharField(max_length=3, null=False, blank=False)
    salary = models.FloatField(null=False, blank=False)
    description = models.TextField(null=True)
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, blank=False, related_name='SalaryScale_user_fk')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        db_table = "tb_salary_scales"
   
    def __str__(self):
        return self.number    
     
        
# Plantilla de cargos de la empresa
class CompanyPosition(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    salary = models.FloatField(null=False, blank=False)
    salary_scale = models.ForeignKey('SalaryScale', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    
    user_at = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, blank=False, related_name='CompanyPosition_user_fk')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        db_table = "tb_company_positions"

    def __str__(self):
        return self.title