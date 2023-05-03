# db_insights

Company database insights should be a web scrapper based on django that extracts and stores company info (logo, name, domain, number of employees, country, among others), always looking for the extracted info to be public domain.

This information would be used to build frontends being served from an endpoint for consultation.

## Setup project

- Install dependencies
```shell
$ git clone git@github.com:carlosgomez2/db_insights.git
$ cd db_insights
$ pip3 install -r requirements.txt
```

- Create your env with venv or conda and activate with `. ./venv/bin/activate`

- Duplicate `.env-sample` and configure your credentials, then rename to `.env`

- Create your database in postgres

- Run migrations `./manage.py migrate`

- Create a superuser `./manage.py createsuperuser`

- Load fixtures for companies `./manage.py loaddata companies.json`

- Run the server `./manage.py runserver 0.0.0.0:8000`

### Test

Selenium webdriver uses firefox.

- To run test `./manage.py test`

