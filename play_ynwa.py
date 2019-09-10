"""
play_ynwa.py.py
Plays You'll Never Walk Alone
"""

import sys
import urllib.request
import playsound

#url = "http://oit2.scps.nyu.edu/~meretzkm/python/string/romeo.txt"
url = "https://raw.githubusercontent.com/hardeep-leyl/play/Liverpool_You_ll_Never_Walk_Alone.mp3"

try:
    ynwa = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

playsound.playsound(ynwa, True)

ynwa.close()
sys.exit(0)
