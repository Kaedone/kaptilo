# Deploy
## Local
- create virtualenv & install requirements
```bash
pyenv virtualenv 3.9.0 kaptilo
pyenv activate kaptilo
pip install poetry
poetry install
``` 
- create reCaptcha's keys at [google.com/recaptcha](https://www.google.com/recaptcha/about/) for localhost
- copy .env file `cp .env.dev .env` or export to envs:
```bash
export API_KEY=...
export ALLOWED_HOSTS=localhost
export BASE_URL=https://localhost:8000
export RECAPTCHA_PUBLIC_KEY=...
export RECAPTCHA_PRIVATE_KEY=...
``` 
- add to env `export DB_DSN=postgres://user:pass@localhost/db_name` if you use Postgres 
- apply DB migrations `./manage.py migrate`
- created **admin:admin** `./manage.py create_super_user`
- run localserver `./manage.py runserver`
- open [localhost/admin/super-sec/](http://localhost/admin/super-sec/) and login as **admin:admin**

## Server
- create reCaptcha's keys at [google.com/recaptcha](https://www.google.com/recaptcha/about/) for **domain.com**
```bash
export API_KEY=...
export SECRET_KEY=...
export DOMAIN=domain.com
export RECAPTCHA_PUBLIC_KEY=...
export RECAPTCHA_PRIVATE_KEY=...

docker-compose up -d --build
docker-compose run back migrate
docker-compose run back collectstatic
docker-compose exec back ./manage.py create_super_user --username admin --password sup-pass-123
open https://domain.com:8000/admin/sec/
```