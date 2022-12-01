# JALPAN

## Comands

- ### Init setup

    run the below command before running the app:

  - ```shell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

    run this in powershell

  - ```shell
    poetry install
    ```

    run in powershell

- ### Run server

    run the dev server to see the frontend at `localhost:8000`

    ```shell
    poetry poe runserver
    ```

- ### Migrate command

    ```shell
    poetry poe migrate
    ```
