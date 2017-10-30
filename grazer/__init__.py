import hashlib
from elasticsearch import Elasticsearch, NotFoundError, ElasticsearchException
from grazer.data import GrazerData


class Grazer(object):
    def __init__(self):
        try:
            self.engine = Elasticsearch()
        except ElasticsearchException:
            raise ElasticsearchException()

    def generate_data(self, data_key):
        return GrazerData(data_key)

    def add_data(self, data):
        assert isinstance(data, GrazerData)

        try:
            grazer_data = self.engine.get(
                index='grazer_data',
                doc_type='xxxxx',
                id=hashlib.md5(data.get_key()).hexdigest()
            )

            if grazer_data:
                merged_data = GrazerData(data.get_key())

                for key, value in grazer_data['_source'].iteritems():
                    for _val in value:
                        merged_data.add_metadata(key, _val)

                for key, value in data.get_metadata().iteritems():
                    for _val in value:
                        merged_data.add_metadata(key, _val)

                self.engine.index(
                    index='grazer_data',
                    doc_type='xxxxx',
                    id=hashlib.md5(merged_data.get_key()).hexdigest(),
                    body=merged_data.get_metadata()
                )

        except NotFoundError:
            self.engine.index(
                index='grazer_data',
                doc_type='xxxxx',
                id=hashlib.md5(data.get_key()).hexdigest(),
                body=data.get_metadata()
            )

