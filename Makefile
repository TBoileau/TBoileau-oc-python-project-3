.PHONY: install build
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
	./venv/Scripts/python -m pydocstyle ./src ./tests ./main.py

build:
	./venv/Scripts/python -m PyInstaller maze.spec