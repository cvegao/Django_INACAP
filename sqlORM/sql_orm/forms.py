from django import forms

from sql_orm.models import Wizard


class WizardForm(forms.Form):
    name = forms.CharField(max_length=45, label="Name: ")
    house = forms.ChoiceField(label="House: ", choices=Wizard.Houses.choices)
    pet = forms.CharField(max_length=45, label="Pet: ")
    year = forms.IntegerField(label="Year: ")

    class Meta:
        model = Wizard
        fields = '__all__'

    def __str__(self):
        return vars(self).keys().__str__()



            # "name: " + self.name.initial \
            #    + "; house: " + self.house.initial \
            #    + "; pet: " + self.pet.initial \
            #    + "; year: " + self.year.initial
