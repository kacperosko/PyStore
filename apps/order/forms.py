from django import forms


class CartCheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField( max_length=255)
    email = forms.EmailField(max_length=150)
    phone = forms.CharField(max_length=10, required=False)

    city = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    postal_code = forms.CharField(max_length=6)

    payment = forms.CharField(max_length=255)

    card_number = forms.CharField(max_length=50, required=False)
    card_expiry = forms.CharField(max_length=5, required=False)
    card_cvv = forms.CharField(max_length=3, required=False)

