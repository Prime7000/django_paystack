from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

user = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['username', 'email']