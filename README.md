# DjangoRestCRUD-and-Upload


Full CRUD with Upload using Django rest



## Running Locally

#### Clone the repo

```bash
   git clone git@github.com:anjeldiniz/DjangoRestCRUD-and-Upload.git
```

#### Change the working directory

```bash
   cd projetoDjangoRest
```

****
**Make sure you install the dependencies with your virtualenv active**


#### If not active:
```bash
   python3 -m venv .venv
```
```bash
   source .venv/bin/active
```
*It may be different from your operating system*

****

#### Install the requirements

```bash
   python3 -m pip install -r requirements.txt
```



## Django Rest Framework Init

*Step by step*

```python
   python manage.py makemigrations
```

```python
   python manage.py migrate
```

#### *You can register with any user*
```python
   python manage.py createsuperuser
```
*Write the superuser username, email and password*

Last Step:

```python
   python manage.py runserver
```

Now you can access routes on your local server either via browser or through request tools.
