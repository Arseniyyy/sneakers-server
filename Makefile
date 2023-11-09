PYTHON := python
MANAGE := $(PYTHON) manage.py

.PHONY: runserver

runserver:
	$(MANAGE) runserver 127.0.0.1:8000

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate $(ARGS)

rungunicorn:
	gunicorn sneakers_server.wsgi:application --bind 0.0.0.0:8000
