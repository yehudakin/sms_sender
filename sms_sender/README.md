# SMS Sender

Service for sending SMS messages and handling user's accounts

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The service uses Flask-SQLAlchemy package, PostgreSQL DB and Docker

### Installing

Install postgresql:

```
brew install postgresql

pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
```

Create DB and user:

```
psql postgres

psql postgres -U yehuda

postgres=# CREATE DATABASE sms_db;
postgres=# GRANT ALL PRIVILEGES ON DATABASE sms_db TO yehuda
postgres-# \connect sms_db
```

Make sure to be inside the sms_sender directory.

Create DB tables:

```
python manage.py db upgrade
```

Build docker (will install all requirements):

```
docker build -t sms-sender .
```

And run it:

```
docker run sms-sender
```
Now the service is ready for use.

## Running the (very basic) test (NOTICE: it clears the DB)

```
nosetests
```