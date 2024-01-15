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

# change ai-service-template to your project name
docker-build:
	docker build -t ai-service-template:latest .

# change ai-service-template to your project name
docker-run:
	docker run --rm -ti -p 8000:8000 ai-service-template:latest
