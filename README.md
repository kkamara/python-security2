# python-react-boilerplate

With docker support.

* [Installation](#installation)

* [Usage](#usage)

* [Using docker](#using-docker)

* [iPython Django Shell](#ipython-django-shell)

* [API](#api)

* [Admin](#admin)

* [Mail server](#mail-server)

* [Misc](#misc)

* [Contributing](#contributing)

* [License](#license)

## Installation

```bash
cp .env.example .env
pip3 install virtualenv && \
  virtualenv env && \
  source env/bin/activate
```

## Usage

```bash
# alias py3="python3"
py3 manage.py runserver 3000
# http://localhost:3000
```

## Using docker?

```bash
alias compose='docker-compose -f local.yml'
compose build
compose up
# http://localhost:80 and http://localhost
```

## iPython Django Shell

```bash
  python3 manage.py shell -i ipython
```

## API

```bash
  python manage.py show_urls
```

View the api collection [here](https://documenter.getpostman.com/view/17125932/UVyxQYrt).

## Admin

Admin creds are set in [./compose/local/django/start](https://raw.githubusercontent.com/kkamara/django-app/develop/compose/local/django/start)

```bash
export DJANGO_SUPERUSER_PASSWORD=secret

python manage.py createsuperuser \
  --username admin_user \
  --email admin@django-app.com \
  --no-input
```

## Mail Server

![docker-mailhog.png](https://raw.githubusercontent.com/kkamara/useful/main/docker-mailhog.png)

Mail environment credentials are at [.env](https://raw.githubusercontent.com/kkamara/django-app/develop/.env.example).

The [mailhog](https://github.com/mailhog/MailHog) docker image runs at `http://localhost:8025`.

## Misc

[See django app.](https://github.com/kkamara/django-app)

[See python amazon scraper 2.](https://github.com/kkamara/selenium-py)

[See python docker skeleton.](https://github.com/kkamara/python-docker-skeleton)

[See python for finance.](https://github.com/kkamara/python-for-finance)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
