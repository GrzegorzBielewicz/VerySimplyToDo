from flask import Flask, render_template, request

app = Flask(__name__)

zadania = [
        "zrobić zakupy",
        "posprzątać pokój",
        "ugotować obiad",
    ]

@app.route('/', methods =['POST', 'GET'])
def todo():

    if request.method == "POST":
        zadania.append(request.form['zadanie'])
    return render_template('formularz.html', zadania=zadania)

if __name__ == '__main__':
    app.run(debug=True)