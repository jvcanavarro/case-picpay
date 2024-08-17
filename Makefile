.PHONY: environment
environment:
	pyenv install -s 3.11.0
	pyenv virtualenv 3.11.0 ml-server
	pyenv local ml-server
	pyenv activate ml-server

.PHONY: requirements
requirements:
	pip install --upgrade pip
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install

.PHONY: lock
lock:
	poetry lock

.PHONY: serve
serve:
	poetry run uvicorn souce.main:app --reload

.PHONY: black
black-check:
	poetry run black .

.PHONY: flake8
flake8-check:
	poetry run flake8 --extend-ignore E203,E501,P103 .

.PHONY: isort
isort-check:
	poetry run isort .

.PHONY: clean
clean:
	find . -name "*.py[co]" -delete
	find . -name "*~" -delete
	find . -name "__pycache__" -delete
