# Trasnapp

Trasn is a Python API for dealing with word translations Eng/Spa.
Available online [here](https://trasnapp.herokuapp.com/) ready to be used for free with Postman or similar solution

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Trasnapp.

```bash
pip install -r requirements.txt
```

## Quickstart

After installing the requirements, modified the config file credentials to access Mongo DB, then just follow this steps:

```python
set FLASK_APP=main.py
flask run
```

## Usage

### Translate

To translate words from english to spanish use this endpoint:

```python
#https://trasnapp.herokuapp.com/main/translate
POST /main/translate HTTP/1.1
Host: trasnapp.herokuapp.com
Content-Type: application/json

{
  "word": "nothing",
  "lang": "en"
}
```

To translate words from spanish to english use this endpoint:
```python
#https://trasnapp.herokuapp.com/main/translate
POST /main/translate HTTP/1.1
Host: trasnapp.herokuapp.com
Content-Type: application/json

{
  "word": "casa",
  "lang": "es"
}
```

### Add Translation
To add new translations from english to spanish use this endpoint:

```python
#https://trasnapp.herokuapp.com/main/add
POST /main/add HTTP/1.1
Host: trasnapp.herokuapp.com
Content-Type: application/json

{
  "word": "nothing",
  "lang": "en",
  "transl": "nada"
}
```

To translate words from spanish to english use this endpoint:
```python
#https://trasnapp.herokuapp.com/main/add
POST /main/translate HTTP/1.1
Host: trasnapp.herokuapp.com
Content-Type: application/json

{
  "word": "home",
  "lang": "en",
  "transl": "casa"
}
```

### Remove Translation
To remove translations in english use this endpoint:

```python
#https://trasnapp.herokuapp.com/main/remove
POST /main/remove HTTP/1.1
Host: trasnapp.herokuapp.com
Content-Type: application/json

{
  "word": "nothing",
  "lang": "en"
}
```

To translate words in spanish use this endpoint:
```python
#https://trasnapp.herokuapp.com/main/remove
POST /main/remove HTTP/1.1
Host: trasnapp.herokuapp.com
Content-Type: application/json

{
  "word": "nada",
  "lang": "es"
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
