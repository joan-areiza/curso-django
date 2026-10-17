from django import forms

class FormArticle(forms.Form): #Hereda de la clase forms

    #creamos las propiedades
    title = forms.CharField(
        label= "Titulo"
    )
    content = forms.CharField(
        label= "Contenido",
        widget=forms.Textarea
    )