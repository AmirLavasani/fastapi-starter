# Install project dependencies from requirements.txt
install-deps:
	pip install -r requirements.txt

# Install development dependencies from requirements-dev.txt
install-deps-dev:
	pip install -r requirements-dev.txt

# Run the FastAPI app using uvicorn with auto-reload
run:
	uvicorn app.main:app --reload

# Run mypy for type checking, Run flake8 for linting
lint:
	mypy src/app
	ruff check src/app

# Generate HTML documentation using pdoc
docz:
	pdoc -f --html --output-dir docs --config show_source_code=False src/app/

# Generate code statistics using pygount
summary:
	pygount --suffix=py  --format=summary .

# Build Docker image with the project name specified
# Change ai-service-template to your project name
docker-build:
	docker build -t ai-service-template:latest .

# Run Docker container, mapping port 8000 from container to host
# Change ai-service-template to your project name
docker-run:
	docker run --rm -ti -p 8000:8000 ai-service-template:latest

# Run semantic-release for versioning without VCS release
version:
	semantic-release version --no-tag --no-vcs-release

# Run semantic-release in dry-run mode to print the next version
next-version:
	semantic-release --noop version --print

# Build distribution packages using build module
package-build:
	python -m build

# Source distribution. A “source distribution” is unbuilt (i.e. it’s not a Built Distribution), 
# and requires a build step when installed by pip.
build-sdist:
	python -m build --sdist

# Wheels. A wheel is a built package that can be installed without needing to go through the 
# “build” process.
build-wheel:
	python -m build --wheel

# Clean up generated artifacts and build files
clean:
	rm -rf dist/ build/ docs/

# Install this project as a pypi package
install:
	pip install .

uninstall:
	pip uninstall ai-service-template -y

# Run tests and write the coverage in html format
testz:
	pytest --disable-warnings --cov=app --cov-report html tests/

all: clean lint docz summary install testz package-build uninstall
