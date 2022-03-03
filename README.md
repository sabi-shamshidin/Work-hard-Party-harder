# Work-hard-Party-harder

Following repository provides code that:

- Django server that receives as an input an image
- A functionality of running a CNN based image classifier
- Stores a path and results of classifyign an image into PostgtreSQL database
______________________________________________________________________________________________

Final Project was done in team - Shaliyeva N. SE-2012, Shamshidin S. SE-2008

## Installation
#### Install the file requirements.txt 
```
pip install -r requirements.txt
```

***Note:** If you are a MAC/Linux User type **3**, after keyword - pip*

## Usage
After installing requirements connect the PostgreSQL database.
Change info in settings.py in project folder. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<name_of_database>',
        'USER': '<username>',
        'PASSWORD': '<your_password>',
        'HOST': '<host>',
        'PORT': '<port>',
    }
}
```
In case, you use databases like SQLite, MySQL etc., check the django documentation - https://docs.djangoproject.com/en/4.0/

After typing your info into _settings.py_, you will need to do migrations by running this command in terminal/command prompt
```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

Then run the server:

### MacOS
```
python manage.py runserver
```

### Windows
```
python manage.py runserver
```

## Examples
#### Screenshots:

##### Home Page:

![IMAGE 2022-03-03 09:53:56](https://user-images.githubusercontent.com/82763714/156493110-034f24fc-4738-49de-b12f-abb5534f2565.jpg)
