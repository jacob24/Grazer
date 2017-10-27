from grazer.data import GrazerData


class Grazer(object):
    def generate_data(self, data_key):
        return GrazerData(data_key)