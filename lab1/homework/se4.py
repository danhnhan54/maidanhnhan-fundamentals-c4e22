from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
customers = db['customers']
num_events = customers.find({"ref": "events"}).count()
num_wom = customers.find({"ref": "wom"}).count()
num_ads = customers.find({"ref": "ads"}).count()

number_ref = [num_events, num_wom, num_ads]
ref_sorce = ['Event', 'Wom','Ads']
pyplot.pie(number_ref, labels = ref_sorce,autopct="%.1f%%",explode=[0, 0.05, 0])
pyplot.axis("equal")
pyplot.title("Ref Percentage")
pyplot.show()