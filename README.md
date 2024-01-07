# AI Service Template

Welcome to the AI Service Template repository! This template is designed for building AI services using FastAPI as the REST API server, with Docker and docker-compose for containerization.

## Main Folders

- **app:** Main application code resides here.
  - **app/assets:** Houses assets and AI models.
  - **app/controllers:** Contains the controllers and logic code for the server.
  - **app/errors:** Holds error response definitions.
  - **app/routers:** Routers for defining API paths.
  - **app/schemas:** Pydantic schemas for the API.
  - **app/utils:** Any additional utility functions can be found here.
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
