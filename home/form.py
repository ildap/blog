from django import forms

from models import Contact


class ContactForm(forms.ModelForm):
    #good_team = forms.CheckboxInput(attrs={'class':''})
    class Meta:
        model = Contact
        fields = ['good_team', 'good_code', 'other_goods', 'name', 'mail', 'phone']

        checkatr = forms.CheckboxInput(attrs={'class':'main-form__checkbox js-checkbox'})

        my_name = '\xec\xe5\xed\xff \xe7\xee\xe2\xf3\xf2'.decode('cp1251')
        my_phone = '\xec\xee\xe9 \xf2\xe5\xeb\xe5\xf4\xee\xed'.decode('cp1251')
        my_mail = '\xec\xee\xe9 e-mail'.decode('cp1251')

        widgets = {
            'good_team': checkatr,
            'good_code': checkatr,
            'other_goods': checkatr,
            'name': forms.TextInput(attrs={'placeholder':my_name,'class':'main-form__input js-input'}),
            'phone': forms.TextInput(attrs={'placeholder':my_phone,'class':'main-form__input js-input'}),
            'mail':forms.EmailInput(attrs={'placeholder':my_mail,'class':'main-form__input js-input'}),
        }
