from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    number = 10
    str = 'lili'
    tuple = (1, 2, 3, 4, 5, 6)
    list = [7, 8, 9, 10, 11, 12]
    dict = {
        'name': "lili",
        'age': 18
    }
    return render_template("file02variable.html", number=number, str=str, tuple=tuple, list=list, dict=dict)


if __name__ == '__main__':
    app.run(debug=True)