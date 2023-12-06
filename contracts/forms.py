from django import forms
from .models import Client, ServiceRequest


# clase form para el cliente
class ClientForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(), required=False)
    
    class Meta:
        model = Client
        fields = [
            "type",
            "name",
            "acronym",
            "first_name",
            "last_name",
            "company_position",
            "province",
            "municipality",
            "address",
            "email",
            "telephone",
            "description",
            "ministry",
        ]
    

class ServiceForm(forms.ModelForm):

    class Meta:
        model = ServiceRequest
        fields = [
            "title",
            "number",
            "first_name",
            "last_name",
            "company_position",
            
            "email",
            "telephone",
            "client",
            "description",
        ]


