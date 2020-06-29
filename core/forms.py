from django import forms

from .models import BuktiBayar

# PAYMENT_CHOICES = (
#     ('Kredit', "Kartu Kredit"),
#     ('Debit', "Kartu Debit")
# )
PROVINCE_CHOICES = (
    ('Aceh', 'Aceh'),
    ('Sumatera Utara', 'Sumatera Utara'),
    ('Sumatera Barat', 'Sumatera Barat'),
    ('Riau', 'Riau'),
    ('Kepulauan Riau', 'Kepulauan Riau'),
    ('Jambi', 'Jambi'),
    ('Sumatera Selatan', 'Sumatera Selatan'),
    ('Bangka Belitung', 'Bangka Belitung'),
    ('Bengkulu', 'Bengkulu'),
    ('Lampung', 'Lampung'),
    ('DKI Jakarta', 'DKI Jakarta'),
    ('Jawa Barat', 'Jawa Barat'),
    ('Banten', 'Banten'),
    ('Jawa Tengah', 'Jawa Tengah'),
    ('Daerah Istimewa Yogyakarta', 'Daerah Istimewa Yogyakarta'),
    ('Jawa Timur', 'Jawa Timur'),
    ('Bali', 'Bali'),
    ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'),
    ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'),
    ('Kalimantan Utara', 'Kalimantan Utara'),
    ('Kalimantan Barat', 'Kalimantan Barat'),
    ('Kalimantan Tengah', 'Kalimantan Tengah'),
    ('Kalimantan Selatan', 'Kalimantan Selatan'),
    ('Kalimantan Timur', 'Kalimantan Timur'),
    ('Sulawesi Utara', 'Sulawesi Utara'),
    ('Sulawesi Barat ', 'Sulawesi Barat '),
    ('Sulawesi Tengah ', 'Sulawesi Tengah '),
    ('Sulawesi Selatan ', 'Sulawesi Selatan '),
    ('Gorontalo', 'Gorontalo'),
    ('Maluku', 'Maluku'),
    ('Maluku Utara', 'Maluku Utara'),
    ('Papua Barat', 'Papua Barat'),
    ('Papua', 'Papua'),
)


class CheckoutForm(forms.Form):
    alamat = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    ket_lain = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'warna rumah, nama kos atau lainnya'
    }))
    provinsi = forms.ChoiceField(choices=PROVINCE_CHOICES)
    kode_pos = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    save_info = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False)
    # pembayaran = forms.ChoiceField(
    #     widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class FormBuktiBayar(forms.Form):
    invoice = forms.CharField()
    foto = forms.ImageField()
