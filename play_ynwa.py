"""
play_ynwa.py.py
Plays You'll Never Walk Alone
"""

import sys
import urllib.request
import playsound

#url = "http://oit2.scps.nyu.edu/~meretzkm/python/string/romeo.txt"
url = "https://github.com/sf19pb1-hardeep-leyl/play/blob/master/Liverpool_You_ll_Never_Walk_Alone.mp3"

try:
    ynwa = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

playsound.playsound(ynwa, True)

ynwa.close()
sys.exit(0)
