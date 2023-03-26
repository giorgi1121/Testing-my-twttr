from twttr import shorten

#test shorten function
def test_shorten():
    #test just words
    assert shorten("hello") == "hll"
    #test letters with upper case
    assert shorten("how ArE YOU?") == "hw r Y?"
    #test with punctuation
    assert shorten("What's UP?") == "Wht's P?"
    #test with numbers
    assert shorten("one 1 twO 2 three 3") == "n 1 tw 2 thr 3"
