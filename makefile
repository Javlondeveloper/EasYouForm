mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
admin:
	python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='admin', password='12345678')"

