# Deploy
## Local
- create virtualenv & install requirements
```bash
pyenv virtualenv 3.9.0 kaptilo
pyenv activate kaptilo
pip install poetry
poetry install
cp .env.dev .env
``` 
- apply DB migrations `./manage.py migrate`
- run localserver `./manage.py runserver`
