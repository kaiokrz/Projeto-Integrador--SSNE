from django import forms
from .models import Mensagem, User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.forms import UsernameField
from .models import User, Curso, Setor, Aviso, Mensagem

class UserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = "__all__"

class SetorForm(forms.ModelForm):

    class Meta:
        model = Setor
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-md-6'),
                Column('bloco', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('categoria', css_class='col-md-4'),
                Column('posicao_x', css_class='col-md-4'),
                Column('posicao_y', css_class='col-md-4'),
                css_class='row'
            ),
            Row(
                Column('descricao', css_class='col-12'),
                css_class='row'
            ),
            Submit('submit', 'Salvar', css_class='btn btn-primary'))

class AvisoForm(forms.ModelForm):

    class Meta:
        model = Aviso
        fields = ("titulo", "curso", "imagem", "conteudo")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('titulo', css_class='col-md-8'),
                Column('curso', css_class='col-md-4'),
                css_class='row'
            ),
            Row(
                Column('imagem', css_class='col-12'),
                css_class='row'
            ),
            Row(
                Column('conteudo', css_class='col-12'),
                css_class='row'
            ),
            Submit('submit', 'Publicar', css_class='btn btn-primary'))