from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/logo/')
@app.route('/home/')
def main():
    return render_template("main.html", cities=data)

@app.route('/contact/')
def contact():
    return render_template("contact.html", cities=data)


@app.route('/products/')
def product():
    return render_template("products.html", cities=data)

#main

data = "nothing"
if __name__ == '__main__':
    app.run(debug=True)
