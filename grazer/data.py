class GrazerData(object):

    def __init__(self, key, **kwargs):
        self.key = key
        self.meta_data = {}

    def add_metadata(self, key, value):
        if key not in self.meta_data.keys():
            _values = [value]
            self.meta_data.update({key:_values})
        else:
            for _val in self.meta_data[key]:
                if _val == value:
                    return

            self.meta_data[key].append(value)

    def get_metadata(self):
        return self.meta_data

    def get_key(self):
        return self.key