from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# forms.py
# where the django documentation recommends you place all your forms code; 
# to keep your code easily maintainable.
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']