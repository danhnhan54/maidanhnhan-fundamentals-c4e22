from mongoengine import Document, DictField

class Register(Document):
    # first_name = StringField()
    # last_name = StringField()
    # email = StringField()
    # yob = IntField()
    # gender = StringField()
    # city = StringField()
    info = DictField()
    # code = StringField()