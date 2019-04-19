from app import app
from flask import Flask
from models import Pet, db, connect_db
import unittest


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptionagency_test'

connect_db(app)
db.create_all()


class MyAppUnitTestCase(unittest.TestCase):
    def test_index(self):
        ''' Make sure that homepage works '''
        client = app.test_client()
        result = client.get('/')

        self.assertEqual(result.status_code, 200)

    def test_add_pet_form(self):
        ''' Make sure that we can access add pet form. '''
        client = app.test_client()
        result = client.get('/add')

        self.assertEqual(result.status_code, 200)

    def test_submit_incomplete_add_pet_form(self):
        ''' Make sure that when we submit incorrect data, that nothing breaks.'''
        client = app.test_client()
        result = client.post('/add',
            data = {'wrong answer':'super wrong'})

        self.assertEqual(result.status_code, 200)

    # def test_submit_correct_add_pet_form(self):
    #     ''' Make sure that when we submit correct data that it inserts into our database and redirects us.'''
    #     client = app.test_client()
    #     result = client.post('/add',
    #         data = {'name':'Whiskey',
    #                 'species':'dog',
    #                 'age':5,
    #                 'available':True})

    #     self.assertEqual(result.status_code, 302)