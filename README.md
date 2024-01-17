# AI Service Template

Welcome to the AI Service Template repository! This template is designed for building AI services using FastAPI as the REST API server, with Docker and docker-compose for containerization.

## Main Folders

- **app:** Main application code resides here.
  - **app/assets:** Houses assets, files, and images.
  - **app/controllers:** Contains the controllers and logic code for the server.
  - **app/errors:** Holds error response definitions.
  - **app/routers:** Routers for defining API paths.
  - **app/schemas:** Pydantic schemas for the API.
  - **app/utils:** Any additional utility functions can be found here.
  - **app/models:** Store the AI models here.
  - **app/main.py:** The main FastAPI file.

- **docs:** Auto-generated code documentation. Do not modify this directory; it's generated using `make docs`.

- **tests:** Primary folder for unit tests and integration tests.

## Setup

### Using setup.sh

Run the `setup.sh` script to create a Conda environment, install main and development dependencies, and execute the project.

### Using Makefile

1. **Create a Conda environment:**
    ```sh
    conda create -n your-project-name python=3.11
    ```

2. **Install Dependencies:**
    ```sh
    make install-deps
    make install-dev-deps
    ```

3. **Run the Project:**
    ```sh
    make run
    ```

Feel free to explore the folders and utilize the structure to build robust AI services with FastAPI. Have fun coding!


## Linting

Before committing any changes, it's recommended to run the linting process using the following command:

```bash
make lint
```

This command will execute the linting checks based on the configurations specified in mypy.ini and .flake8 files. These configurations define rules for mypy and flake8 to ensure code consistency, style adherence, and type checking across the project.

## Make New AI Service Project

1. clone this repo
```bash
git clone http://172.31.112.27/ai-services/ai-service-template.git
```

2. change the remote to your-project
```bash
git remote rename origin template
git remote add origin http://172.31.112.27/ai-services/your-service-project.git
```

3. change `ai-service-template` in the following locations to your project service name.
- docker-compose.yml
- Makefile
- setup.sh
- README.md
- interface.py
- main.py (docstring, fastapi, and root endpoint)

4. create conda env and running the `setup.sh` file, and installing the dependencies.
```bash
./setup.sh
```

5. start by creating a router file in `routers` and add your router in `routers/__init__.py`. Use `version_router` example.

6. we use trunk-based development. You can create feature branches and merge those frequent updates to `main` or directly push to main.

7. use `main` as default branch name.

8. use `make lint` before every commit and resolve `mypy` and `flake8` errors.

9. build docs after developing the main functionalities and classes.

```bash
make docs

pdoc -f --html --output-dir docs --config show_source_code=False app/
```

10. add gradio interface after developing the service api.

11. update dockerfile and build docker image.
```bash
make build-docker
```

12. build pydantic schemas for input and output of your api's.
