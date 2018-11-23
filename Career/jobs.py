from mongoengine import Document, StringField, ListField, DictField, ReferenceField

class Job_sector(Document):
    job_sector = StringField()
    js_code = StringField()

class Jobs(Document):
    job_name = StringField()
    job_sector = StringField()
    job_define = StringField()
    res = ListField()
    empls = DictField()
    quals = DictField()
    skills = DictField()
    code = StringField()
