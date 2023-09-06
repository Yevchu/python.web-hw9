from mongoengine import Document
from mongoengine.fields import StringField, ListField, ReferenceField

class Author(Document):
    name = StringField()

class Tag(Document):
    tag = ListField()

class Quote(Document):
    quote = StringField()