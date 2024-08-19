from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    name = 'John'
    age = 25
    return render_template('about.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

if __name__ == '__main__':
    app.run(debug=True)
