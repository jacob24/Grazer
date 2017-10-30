import unittest
import mock
from elasticsearch import NotFoundError

from grazer import Grazer
from grazer.data import GrazerData


class TestMainGrazerFunction(unittest.TestCase):
    def setUp(self):
        self.grazer = Grazer()

    @mock.patch('elasticsearch.Elasticsearch.index')
    def test_exact_result_found_combining_meta_data(self, mock_index):
        with mock.patch('elasticsearch.Elasticsearch.get') as mock_get:
            mock_get.return_value = {
                '_index': 'grazer_data',
                'doc_type': 'xxxxx',
                '_id': '9517b5e8a042566405c2f40195e4e1f3',
                '_source': {
                    'products': [
                        'FROZEN TILAPIA FILLET',
                        'FROZEN SALMON'
                    ]
                }
            }

            grazer = Grazer()
            data = grazer.generate_data('THE FISHIN COMPANY')
            data.add_metadata('know_address', '3714 MAIN STREET, PITTSBURGH, PA 15201, USA')
            data.add_metadata('products', 'FROZEN TILAPIA FILLET')
            data.add_metadata('products', 'FROZEN TILAPIA')
            data.add_metadata('products', 'TILAPIA FILLET')
            grazer.add_data(data)

            mock_index.assert_called_with(index='grazer_data',
                                          doc_type='xxxxx',
                                          id='9517b5e8a042566405c2f40195e4e1f3',
                                          body={
                                                'know_address': [
                                                    '3714 MAIN STREET, PITTSBURGH, PA 15201, USA'
                                                ],
                                                'products': [
                                                    'FROZEN TILAPIA FILLET',
                                                    'FROZEN SALMON',
                                                    'FROZEN TILAPIA',
                                                    'TILAPIA FILLET'
                                                ]
                                          })


    @mock.patch('elasticsearch.Elasticsearch.index')
    def test_no_found_result(self, mock_index):
        with mock.patch('elasticsearch.Elasticsearch.get') as mock_get_no_result:
            mock_get_no_result.side_effect = NotFoundError
            grazer = Grazer()
            data = grazer.generate_data('THE FISHIN COMPANY')
            data.add_metadata('products', 'FROZEN TILAPIA FILLET')
            grazer.add_data(data)

            mock_index.assert_called_with(index='grazer_data',
                                          doc_type='xxxxx',
                                          id='9517b5e8a042566405c2f40195e4e1f3',
                                          body={
                                              'products': [
                                                  'FROZEN TILAPIA FILLET'
                                              ]
                                          })

            data2 = grazer.generate_data('APPLE COMPUTER, INC C/O OHL')
            data2.add_metadata('know_address', '1710 W BASE LINE RD, RIALTO, CA 92376, USA')
            data2.add_metadata('products', 'POWER ADAPTER')
            data2.add_metadata('products', 'POWER')
            data2.add_metadata('products', 'ADAPTER')
            grazer.add_data(data2)

            mock_index.assert_called_with(index='grazer_data',
                                          doc_type='xxxxx',
                                          id='a223a9b0448c27a1a878d7ff24f275aa',
                                          body={
                                              'know_address': [
                                                  '1710 W BASE LINE RD, RIALTO, CA 92376, USA'
                                              ],
                                              'products': [
                                                  'POWER ADAPTER',
                                                  'POWER',
                                                  'ADAPTER',
                                              ]
                                          })

    @mock.patch('elasticsearch.Elasticsearch.get')
    def test_adding_of_data(self, mock_es):
        grazer = Grazer()
        data = grazer.generate_data('THE FISHIN COMPANY')
        data.add_metadata('know_address', '. 3714 MAIN STREET, PITTSBURGH PA 151 20 US')
        data.add_metadata('products', 'FROZEN TILAPIA FILLET')
        data.add_metadata('products', 'FROZEN TILAPIA')
        data.add_metadata('products', 'TILAPIA FILLET')
        grazer.add_data(data)

        mock_es.assert_called_with(index='grazer_data', doc_type='xxxxx', id='9517b5e8a042566405c2f40195e4e1f3')

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