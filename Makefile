PORT ?= 8080
TIMEOUT ?= 1800

install:
	poetry install

app-dry:
	export DEBUG=true; export LOGLEVEL=DEBUG; poetry run python app.py

app:
	poetry run gunicorn index:server --bind="0.0.0.0:${PORT}" --timeout ${TIMEOUT}

flake8:
	git ls-files '*.py' | poetry run flake8 --count

pylint:
	git ls-files '*.py' | xargs poetry run pylint --disable=duplicate-code --fail-under=9.5

black:
	git ls-files '*.py' | poetry run black --check .

pytest:
	poetry run pytest --no-cov-on-fail --cov-fail-under=70 --cov-branch --cov-report=term --cov-report=html:htmlcov --cov=pages

docker-dry:
	docker build . -t derick-portfolio && docker run -p 8080:8080 derick-portfolio

