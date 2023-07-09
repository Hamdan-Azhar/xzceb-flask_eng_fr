from machinetranslation import translator as t
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return t.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return t.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
      return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
