from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
posts = db['posts']
post = {
    'title': 'Cảm nhận về lớp C4E22',
    'author': 'Nhân',
    'content': 'Lớp học rất vui. Nhưng mình thì lười làm btvn vãi nồi. ahihi',
}
posts.insert_one(post)
