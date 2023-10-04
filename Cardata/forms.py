from .models import CarData, Carmodel, Carbrand, CarImage
from django import forms

fule = [("CNG", "CNG+Petrol"), ("Petrol", 'Petrol'), ("Diesel", 'Diesel')]
trans = [("Manual", "Manual"), ("Automatic", 'Automatic')]


class Add_Car(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "bg-black-50 border border-white-300 text-black-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black-700 dark:border-white-600 dark:placeholder-black-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500", 'placeholder': 'Start typing a location...'})
    )

    class Meta:
        model = CarData
        fields = ['fuletype', "transmission", 'carmodel', 'carbrand', "carIDE",
                  "caryear", "kilometers", "ownership", 'price', 'images', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fuletype'] = forms.ChoiceField(
            choices=fule, widget=forms.RadioSelect())
        self.fields['transmission'] = forms.ChoiceField(
            choices=trans, widget=forms.RadioSelect())
        self.fields['carmodel'].queryset = Carmodel.objects.none()
        # self.fields['carbrand'].widget.choices[0] = ('', '--------', {'hidden': None, 'selected': None})
        if 'carbrand' in self.data:
            try:
                brand_id = int(self.data.get('carbrand'))
                self.fields['carmodel'].queryset = Carmodel.objects.filter(
                    carbrand_id=brand_id).order_by('carmodel')
            except:
                pass
        elif self.instance.pk:
            self.fields['carmodel'].queryset = self.instance.carbrand.carmodel_set.order_by(
                'carmodel')
