import unittest
import os
from flask import current_app
from app import create_app
from app.models.categoria_cargo import CategoriaCargo

class CategoriaCargoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_categoriacargo_creation(self):
        
        categoriacargo = CategoriaCargo()
        categoriacargo.nombre = "Categoria 1"
        self.assertIsNotNone(categoriacargo)
        self.assertEqual(categoriacargo.nombre, "Categoria 1")

if __name__ == "__main__":
    unittest.main()