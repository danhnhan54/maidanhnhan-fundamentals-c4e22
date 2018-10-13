from youtube_dl import YoutubeDL

# Sample 1: Download simple youtube videos   
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

# Sample 2: Download multiple youtube videos
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

# Sample 3: Download audio
options = {
    'format': 'bestaudio/best',
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
