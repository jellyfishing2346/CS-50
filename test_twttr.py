from twttr import shorten
import sys

# Creare a fucntion to shorten any given word
def shortenTest():
    assert shorten("testing") == "tsting"
    assert shorten("this is your tweet") == "ths s you twt"
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("s0mething") == "s0mething"
sys.exit(1)