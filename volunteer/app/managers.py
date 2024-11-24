from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You have entered an invalid email address."))

    def create_user(self, first_name, last_name, email, password):

        if not first_name:
            raise ValueError(_("The first name must be set"))

        if not last_name:
            raise ValueError(_("The last name must be set"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User: and email address is required"))

        if not password:
            raise ValueError(_("Superusers must have set password"))

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.password = make_password(password)
        user.save(using=self._db)
        return user