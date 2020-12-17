from django import forms

carparks = [
    (1, "Glasnevin"),
    (2, "St.Pats"),
    (3, "All Hallows"),
]


class MapForm(forms.Form):
    address = forms.CharField(label="address", max_length=200, required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'Street Name, City, Country',
                                                            'class': "form-control",
                                                            'type': "text"}))
    carpark = forms.ChoiceField(choices=carparks, widget=forms.Select(attrs={'class': "form-control"}))
