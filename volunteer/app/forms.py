from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "first_name", "last_name"]
        error_class = "error"

class CustomerUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ["email", "first_name", "last_name"]
        error_class = "error"