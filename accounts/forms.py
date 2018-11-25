from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(forms.Form):
    username = forms.CharField(label=("Username"), required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        print(self.helper)
        self.helper.form_id = 'form_id'
        self.helper.form_class = ''
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.label_class=''
        self.helper.field_class=''
        self.helper.add_input(Submit('submit', 'Submit'))
        print(self.helper.form_class)

