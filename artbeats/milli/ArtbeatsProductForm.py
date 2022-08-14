from django.forms import ModelForm
from .entity.model import artbeatproducts
class ProductForm(ModelForm):
    class Meta:
        model = artbeatproducts
        fields = ['artsname', 'artsdescr','artsprice','artscatagory','artsimage']



