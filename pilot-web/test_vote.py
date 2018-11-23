import mlab
from vote import Vote
from poll import Poll

mlab.connect()

#  From vote => poll
# vote = Vote.objects().first()
# print(vote.choice)
# print(vote.voter)
# poll = vote.poll
# print(poll.question,poll.options)

# From poll => votes
poll = Poll.objects(code="AKHVCU").first()
votes = Vote.objects(poll=poll)
for vote in votes:
    print(vote.voter)
    print(vote.poll.question)
