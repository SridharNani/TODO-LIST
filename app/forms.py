
from django.forms import ModelForm
from app.models import TODO

class TODOForm(ModelForm):
    class Meta:
        fields=['title','status','priority']
        model=TODO