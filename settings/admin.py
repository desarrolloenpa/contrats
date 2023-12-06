from django.contrib import admin
from .models.user import CustomUser, GroupUser
from .models.local import Province, Municipality
from .models.user import SalaryScale, CompanyPosition
from .models.service import ServiceType

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(GroupUser)
admin.site.register(Province)
admin.site.register(Municipality)

admin.site.register(SalaryScale)
admin.site.register(CompanyPosition)

admin.site.register(ServiceType)
