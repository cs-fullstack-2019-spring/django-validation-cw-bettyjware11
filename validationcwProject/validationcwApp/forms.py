from django import forms
from .models import newCarModel

class newCarForm(forms.ModelForm):
    class Meta:
        model = newCarModel
        fields = "__all__"

    def clean_goodCarMileage(self):
        mpg = self.cleaned_data["goodCarMileage"]


        if mpg<20:
            raise forms.ValidationError("That's less than a truck!!!")

        if mpg>500:
            raise forms.ValidationError("That's impossible (in 2019)")

        return mpg

    def clean_goodCarYear(self):
        year = self.cleaned_data["goodCarYear"]

        if year<2019:
            raise forms.ValidationError("That's not new!!!")

        return year