from poll import Poll
from random import choice
import mlab

# 1. Connect to database
mlab.connect()

# 2. Prepare data
q = "Hackathon ăn gì?"
opts = [
    "Pizza",
    "Bánh mỳ Hội An",
    "Phở xào",
]
alphabet = "abcdefjhijklmnopqrstuvwxyz".upper()
c = "" # short uuid python
for _ in range(6):
    c += choice(alphabet)

# 3. Create document
p = Poll(question=q, options=opts, code=c)

# 4. Save
p.save()