PYTHON := python
MANAGE := $(PYTHON) manage.py

.PHONY: runserver

runserver:
	$(MANAGE) runserver 0.0.0.0:8000
