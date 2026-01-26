#create two variables to store the title and artists of a song
title='here comes the sun'
artist='the beatles'

#create a formatted string to display the message
message=f'My favourite song is {title.title()},by the artist {artist.title()}'
print(message)

#create a list called 'playlist' that contains 3 song tiles of my choice
playlist=['Ex-factor', 'Waterfalls', 'Creep']
print(playlist)

#add a new song to the playlist using .extend
playlist.extend(["God's plan",'Forever young', 'Rato laka'])
print(playlist)