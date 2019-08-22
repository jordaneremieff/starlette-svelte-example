# starlette-svelete-example

A simple example of using [Svelete](https://svelte.dev/) with [Starlette](https://www.starlette.io/) and [Databases](https://www.encode.io/databases/).

## Setup 

From the `backend/` directory, create a new virtual environment, install the dependencies, and create the database:

```shell
python3.7 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python init_db.py
```

### Frontend

From the `frontend/` directory, install the dependencies:

```shell
npm install
```

## Running

### Backend

From the `backend` directory (using the virtual environment), enter the following:

```shell
uvicorn app:app
```

### Frontend
From the `frontend/` directory, enter the following:


```shell
npm run dev
```


Then visit http://localhost:5000.
