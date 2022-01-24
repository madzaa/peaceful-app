# -*- coding: utf-8 -*-
"""Application configuration."""


class Config(object):
    """Base configuration"""

    DEBUG = False

    # db config

    POSTGRES_HOST = 'postgresql-ha-pgpool.default.svc.cluster.local' ##normally would subsitute this with ConfigMap in helm
    POSTGRES_PORT = '5432'
    POSTGRES_USER = 'postgres'
    POSTGRES_PASS = 'postgres'
    POSTGRES_DB = 'blacklisted'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False

    # mail configuration

    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '52f84271aec163'
    MAIL_PASSWORD = '98eadb1b3182fa'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
