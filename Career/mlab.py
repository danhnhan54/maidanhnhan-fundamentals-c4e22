import mongoengine

# mongodb://admin:admin1@ds113648.mlab.com:13648/c4e22_project_career

host = "ds113648.mlab.com"
port = 13648
db_name = "c4e22_project_career"
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