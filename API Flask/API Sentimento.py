from flask import Flask
from textblob import TextBlob

app = Flask("__name__")
print(app)

@app.route('/')
def home():
    return "API 1 em Flask"

@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to="en")
    polaridade = tb_en.sentiment.polarity
    return "Analise de sentimento: {}".format(polaridade)


app.run(debug=True)