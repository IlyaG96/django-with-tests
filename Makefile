prepare-venv:
	python3 -m venv env && source env/bin/activate && pip install -r requirements.txt

run-app:
	cd django-with-tests && python manage.py migrate && python manage.py runserver

copy-env:
	cp ./django-with-tests/.env.example ./django-with-tests/.env || true

run-local: prepare-venv copy-env run-app
