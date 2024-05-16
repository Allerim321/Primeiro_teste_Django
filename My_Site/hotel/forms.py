from django import forms


#criação que herde as funções da classe forms
class FormNome(forms.Form):
    nome = forms.CharField(label="Nome:", max_length=30)
    email = forms.CharField(label="E-mail:", max_length=20)
    senha = forms.CharField(label="Senha:", max_length=10)