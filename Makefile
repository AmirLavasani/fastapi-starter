install-deps:
	pip install -r requirements.txt

install-dev-deps:
	pip install -r requirements-dev.txt

run:
	uvicorn app.main:app --reload

lint:
	mypy app
	flake8 app

docs:
	pdoc -f --html --output-dir docs --config show_source_code=False app/

summary:
	pygount --suffix=py  --format=summary .