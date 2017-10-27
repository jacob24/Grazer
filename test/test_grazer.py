import unittest
import mock
from grazer import Grazer
from grazer.data import GrazerData


class TestMainGrazerFunction(unittest.TestCase):
    def setUp(self):
        self.grazer = Grazer()

    def test_generation_of_data_same_value_for_key(self):
        data = self.grazer.generate_data('FAKE DATA')
        self.assertIsInstance(data, GrazerData)

        data.add_metadata('address', 'FAKE ADDRESS 1')
        data.add_metadata('address', 'FAKE ADDRESS 1')
        data.add_metadata('product', 'FAKE PRODUCT 1')
        data.add_metadata('product', 'FAKE PRODUCT 2')
        data.add_metadata('product', 'FAKE PRODUCT 2')
        data.add_metadata('product', 'FAKE PRODUCT 3')

        _fake_meta_data = {
            'address': [
                'FAKE ADDRESS 1',
            ],
            'product': [
                'FAKE PRODUCT 1',
                'FAKE PRODUCT 2',
                'FAKE PRODUCT 3'
            ]
        }

        self.assertEqual(data.get_metadata(), _fake_meta_data)

    def test_generation_of_data(self):
        data = self.grazer.generate_data('FAKE DATA')
        self.assertIsInstance(data, GrazerData)

        data.add_metadata('address', 'FAKE ADDRESS 1')
        data.add_metadata('address', 'FAKE ADDRESS 2')
        data.add_metadata('product', 'FAKE PRODUCT 1')
        data.add_metadata('product', 'FAKE PRODUCT 2')
        data.add_metadata('product', 'FAKE PRODUCT 3')
        data.add_metadata('product', 'FAKE PRODUCT 4')

        _fake_meta_data = {
            'address': [
                'FAKE ADDRESS 1',
                'FAKE ADDRESS 2'
            ],
            'product': [
                'FAKE PRODUCT 1',
                'FAKE PRODUCT 2',
                'FAKE PRODUCT 3',
                'FAKE PRODUCT 4'
            ]
        }

        self.assertEqual(data.get_metadata(), _fake_meta_data)