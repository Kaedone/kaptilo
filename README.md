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

## Server
```bash
export API_KEY=...
export SECRET_KEY=...
export DOMAIN=domain.com

docker-compose up -d --build
docker-compose run back migrate
docker-compose run back collectstatic
docker-compose exec back ./manage.py create_super_user --username admin --password sup-pass-123
open https://domain.com:8000/admin/sec/
```