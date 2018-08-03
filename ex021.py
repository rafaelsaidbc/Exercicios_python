from pygame import *

mixer.init()
mixer.music.load('C:/Users/Usuario/Music/braulio.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.Clock().tick(10)
