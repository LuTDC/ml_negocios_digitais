from textblob import TextBlob

def analisar(frase):
    text_blob = TextBlob(frase)

    return text_blob.sentiment.polarity