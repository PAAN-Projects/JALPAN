# JALPAN

## Comands

- ### Init setup

    run the below command before running the app:

  - Install Poetry

    ```shell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

    run this in powershell

  - Install dependencies:

    ```shell
    poetry install
    ```

    run in powershell
  
  - Open venv shell

    ```shell
    poetry shell
    ```

- ### Run server
    
    After opening the venv shell
    run the dev server to see the frontend at `localhost:8000` and the app routes will be listed

    ```shell
    py ./jalpan/manage.py runserver
    ```


> # Code Documentation can be found [here](/docs/documentation.docx)
