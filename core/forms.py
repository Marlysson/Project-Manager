from django.forms import ModelForm
from .models import Funcionario


class FuncionarioForm(ModelForm):

    class Meta:
        model = Funcionario
        fields = ["nome", "idade", "salario", "cargo"]
