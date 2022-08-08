class BaseModel:
    def parseData(self, data):
        for attribute in self.__class__.__dict__.keys():
            if attribute[:2] != '__':
                value = getattr(self.__class__, attribute)
                if not callable(value):
                    self[attribute].set(data[attribute])
    
    def to_json(self):
        json_object = {}
        for attribute in self.__class__.__dict__.keys():
            if attribute[:2] != '__':
                value = getattr(self.__class__, attribute)
                if not callable(value):
                    json_object[attribute] = value.value