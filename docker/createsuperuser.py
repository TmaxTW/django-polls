from django.contrib.auth.models import User
usr = User.objects.create(username='admin',email='john@doe.com')
usr.is_superuser=True
usr.is_staff=True
usr.set_password('admin')
usr.save()
