from google_speech import Speech

# say "Hello World"
text = "Hello World"
with open("dfd.txt",'r') as tf:
    text = tf.read()
    lang = "en"
    speech = Speech(text,lang)
    sox_effects = ("speed","1")
    speech.play(sox_effects)
