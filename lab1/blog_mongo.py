from pymongo import MongoClient
uri = "mongodb://admin:c4e22lab1@ds225253.mlab.com:25253/c4e22n"

# Connect to database
client = MongoClient(uri)
db = client.get_default_database()
# Collection
posts = db['posts'] # insert_one (C), find(R)

post_list = posts.find()
for p in post_list:
    print(p['author'])
    print(p['title'])
    print(p['content'])
# Document
# Create a document
# post = {
#     'title': 'Hôm nay là thứ 2',
#     'content': 'Tôi phải đi làm',
#     'author': 'Me',
# }
# # Insert created document
# posts.insert_one(post)

