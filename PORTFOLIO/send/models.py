from django.db.models import Model, DateField

# Create your models here.
class WakeDatabase(Model):
    created = DateField(auto_created=True, auto_now_add=True)
