from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    descriptio = forms.CharField(label="Descripcion de la tarea",widget=forms.TextInput(attrs={'class':'input'}))

class CreateNewProjects(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200,widget=forms.TextInput(attrs={'class':'input'}))