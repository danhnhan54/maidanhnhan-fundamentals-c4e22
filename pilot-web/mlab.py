import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds149732.mlab.com:49732/c4e22-poll

host = "ds149732.mlab.com"
port = 49732
db_name = "c4e22-poll"
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