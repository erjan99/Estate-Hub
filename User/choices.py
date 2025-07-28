from django.db.models import TextChoices

class MyUserRole( TextChoices):
    STANDARD = 'standard_user'
    MANAGER = 'manager'
    ACCOUNTANT = 'accountant'