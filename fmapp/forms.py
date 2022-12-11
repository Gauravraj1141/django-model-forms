from .models import registeration, mynewform
from django import forms


class register(forms.ModelForm):

    class Meta:
        model = registeration
        # fields = ('Myname', 'Subject', 'Myurl', 'city', )
        # we use this place of above line "__all__" means all fiels will come in this form
        fields = "__all__"


class login(forms.ModelForm):
    class Meta:
        model = registeration
        exclude = ("Myurl", "city",)


# here we can inherit our model form
class Studentform(forms.ModelForm):

    class Meta:
        model = mynewform
        fields = ('Studentname', 'myclass', 'registraionid', )


class Teacherform(Studentform):
    class Meta(Studentform.Meta):
        fields = ('Teachername', 'registraionid', )
