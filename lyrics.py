import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("When you call my name", 0.07),
        ("When you call my name", 0.07),
        ("When you call my name ...", 0.09),
        ("",0.2),
        ("Kyal thar yar twe linn ny dl", 0.1),
        ("Yin khwin ta sone hr nwayy ny dl", 0.1),
        ("Ayar yar hr tagl hla ny dl", 0.07),
        ("Ayin chain twe pyan yout chin dl", 0.07),
    ]

    delays = [0.08, 0.1, 1.5, 0.1, 1.11, 1, 1.3, 1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()