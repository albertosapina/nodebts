import constants
from nosql_wiki.utils.appexception import AppException

class Field:
    def __init__(self, name, type, many=False, null=True):
        self.name = name
        self.type = self.loadFieldTypeByCode(type)
        self.many = many
        self.null = null
        if null:
            self.value = None
            if many:
                self.value = []
            else:
                self.value = type.getDefault()
    
    def loadFieldTypeByCode(self, value):
        if value == constants.FIELD_TYPE_STRING:
            return StringField
        if value == constants.FIELD_TYPE_NUMBER:
            return NumberField
        if value == constants.FIELD_TYPE_DATE:
            return DateField
        else:
            raise AppException("Invalid field type: " + value)
        
    def set(self, new_value):
        if not self.many:   
            if self.type.validate(new_value):
                self.value = new_value
            else:
                raise AppException("Invalid value "+ str(new_value) +" for type: " + self.type.name)
        else:
            for single_value in new_value:
                if not self.type.validate(single_value):
                    raise AppException("Invalid value "+ str(single_value) +" for type: " + self.type.name)
                self.value = new_value
                
    def get(self):
        return self.value
    
    def add(self, new_value):
        if self.many:
            self.value.append(new_value)
        else:
            raise AppException("Can not call method 'add' with many=False")
            
class BaseFieldType:
    name='basefield'
    @staticmethod
    def getDefault():
        return None
    @staticmethod
    def validate(value):
        return True
        
    
class StringField(BaseFieldType):
    name='string'
    @staticmethod
    def getDefault():
        super()
        return ''
    @staticmethod
    def validate(value):
        super()
        if type(value) == str:
            return True
        else:
            return False
        
class NumberField(BaseFieldType):
    name='number'
    @staticmethod
    def getDefault():
        super()
        return 0
    @staticmethod
    def validate(value):
        super()
        if type(value) == int or type(value) == float:
            return True
        else:
            return False
        
class DateField(BaseFieldType): # Work in progress
    name='date'
    @staticmethod
    def getDefault():
        return super()
    @staticmethod
    def validate(value):
        return super()