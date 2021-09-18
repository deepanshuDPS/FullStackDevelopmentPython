from django import forms
from django.core import validators
from first_app.models import User


def check_for_d(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError('Need the name to start with D')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_d])
    # custom validators :)
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    ## custom validator to validate or check all the cleaned data at a time
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")

    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    # validators is inbuild validators like we make function below

    # two define our own validations two form inputs
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha Bot!")
    #     return botcatcher


class NewUser(forms.ModelForm):

    class Meta():
        model = User
        fields = "__all__"