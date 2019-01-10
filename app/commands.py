import click

from app.db import db


def create_db():
  db.create_all()

def drop_db():
  if click.confirm('Are you sure?', abort=True):
    db.drop_all()
