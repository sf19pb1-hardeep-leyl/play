"""
play_ynwa.py
Plays You'll Never Walk Alone
"""

import sys
import urllib.request
import playsound

#file = "/Users/kadysafar/Desktop/Liverpool_You_ll_Never_Walk_Alone.mp3"
#url = "https://github.com/sf19pb1-hardeep-leyl/play/blob/master/Liverpool_You_ll_Never_Walk_Alone.mp3"
url = "http://www.fcsongs.com/uploads/audio" \
    "/Liverpool%20FC%20-%20You%20Will%20Never%20Walk%20Alone.mp3"

try:
    ynwa = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

#Doesn't work when I call the url but works playing a local copy of the mp3
#playsound.playsound(file, True)
playsound.playsound(ynwa, True)

ynwa.close()
sys.exit(0)
