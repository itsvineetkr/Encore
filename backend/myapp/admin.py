from django.contrib import admin
from django.contrib.auth.models import User, Group

# Create Yash Sir
yash_sir, created = User.objects.get_or_create(username='yash_sir')
if created:
    yash_sir.set_password('yash_password')  # Set a secure password
    yash_sir.is_staff = True
    yash_sir.is_superuser = True
    yash_sir.save()

# Create Aditya
aditya, created = User.objects.get_or_create(username='aditya')
if created:
    aditya.set_password('aditya_password')  # Set a secure password
    aditya.is_staff = True
    aditya.is_superuser = True
    aditya.save()

# Create a custom admin group
admin_group, created = Group.objects.get_or_create(name='Custom Admins')
if created:
    admin_group.user_set.add(yash_sir, aditya)

# Register other models if needed
# admin.site.register(MyModel)


# Register your models here.
