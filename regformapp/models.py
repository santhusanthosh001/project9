from django.db import models
class reg (models.model):
    first_name=models.cherfield(max_lenght=10)
    last_name=models.cherfield(max_lenght=10)
    user_name=models.cherfield(max_length=10,primary_key=True)
    password=models.cherfield(max_length=10)
    cpassword=models.cherfield(max_lenght=10)
    email=models.emailfield()
    mobile=models.integerfield()


# Create your models here.
