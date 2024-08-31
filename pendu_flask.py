from flask import Flask, render_template, request
app = Flask(__name__)

liste_mots = ["affichage", "reste", "manger"]

@app.route('/')
def welcome():
    mot = request.args.get('mot')
    mot_final = mot if mot in liste_mots else 0
    return render_template('index.html', mots=str(mot_final))


if __name__ == '__main__':
    app.run(debug=True)