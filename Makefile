install:
	pip install -r requirements.txt
test:
	pytest --cov=app tests/
sort:
	isort ./app
format:
	bandit ./app
lint:
	pylint ./app

run:
	python3 run.py