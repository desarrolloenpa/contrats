from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=100, unique=False)
    class Meta:
        db_table = "tb_provinces"

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=100, unique=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="municipality_province_fk")
    
    class Meta:
        db_table = "tb_municipalities"

    def __str__(self):
        return self.name