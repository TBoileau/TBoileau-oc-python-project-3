.PHONY: install
install:
	python -m pip install --upgrade pip
	python -m venv ./venv
	./venv/Scripts/python -m pip install -r requirements.txt

freeze:
	./venv/Scripts/python -m pip freeze > requirements.txt

test:
	./venv/Scripts/python -m pytest

coverage:
	./venv/Scripts/python -m pytest --cov=./src --cov-report=html

coding-style:
	./venv/Scripts/python -m flake8 ./src ./tests