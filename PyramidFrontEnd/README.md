Siyavula Education TodoList Frontend App
=================================



Getting Started
---------------

Running Locally
---------------------------
- Change directory into your newly created project.

  ```
  cd PyramidFrontend
  ```

- Create a Python virtual environment.

  ```
  python3 -m venv env
  ```

- Upgrade packaging tools.

  ```
  env/bin/pip install --upgrade pip setuptools
  ```

- Install the project in editable mode with its testing requirements.
  ```
  env/bin/pip install poetry
  env/bin/poetry install
  ```

- Run your project's tests.
    ```
    env/bin/pytest
    ```

- Run your project.
    ```
    env/bin/pserve development.ini
    ```


- Or you can start with Docker.
## Build and Run the App With Docker)
Run `docker-compose build` to build the containers.  
Run `docker-compose up` to start the app.  
Run `docker-compose up -d` to start the app in detached mode.  
Run `docker-compose down` to stop the app.