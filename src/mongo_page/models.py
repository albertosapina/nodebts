import nosql_wiki.utils.constants as constants
from nosql_wiki.utils.base_model import BaseModel
from nosql_wiki.utils.field import Field

class Page(BaseModel):
    id = Field("id", constants.FIELD_TYPE_NUMBER, null=False)
    title = Field("title", constants.FIELD_TYPE_STRING, null=False)
    content = Field("content", constants.FIELD_TYPE_STRING, null=False)
    tags = Field("tags", constants.FIELD_TYPE_STRING, many=True, null=False)