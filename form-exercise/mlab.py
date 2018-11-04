import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds247223.mlab.com:47223/c4e22-register-form

host = "ds247223.mlab.com"
port = 47223
db_name = "c4e22-register-form"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())