makemigrations:
	python manage.py makemigrations application
	python manage.py makemigrations call
	python manage.py makemigrations data
	python manage.py makemigrations employee
	python manage.py makemigrations person
	python manage.py makemigrations signin
	python manage.py makemigrations student

rollbackall:
	python manage.py migrate zero

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

populate_data:
	python manage.py populate_data

delete_migrations:
	find . -path "./*/migrations/*.py" -not -name "__init__.py" -delete
