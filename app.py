from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Caminho para as imagens das letras
LETRAS_DIR = os.path.join(app.static_folder, "letras")

def obter_imagens_palavra(palavra):
    imagens = []
    for letra in palavra.upper():
        caminho = f"{letra}.png"
        if os.path.exists(os.path.join(LETRAS_DIR, caminho)):
            imagens.append(caminho)
    return imagens

@app.route("/", methods=["GET", "POST"])
def index():
    imagens = []
    if request.method == "POST":
        palavra = request.form.get("palavra", "").strip()
        if palavra:
            imagens = obter_imagens_palavra(palavra)
    return render_template("index.html", imagens=imagens)

@app.route("/letras/<filename>")
def letras(filename):
    return send_from_directory(LETRAS_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
