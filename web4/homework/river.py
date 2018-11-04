from mongoengine import Document, StringField, ListField

class River(Document):
    name = StringField()
    continent = StringField()
    length = StringField()