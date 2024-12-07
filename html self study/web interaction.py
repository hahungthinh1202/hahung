import json
import game


from flask import Flask, render_template,jsonify, request
app = Flask(__name__)


@app.route('/')
@app.route('/logo/')
@app.route('/home/')
@app.route('/main/')
def main():
    return render_template("main.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route('/products/')
def product():
    return render_template("products.html")

@app.route('/test2')
def test2():
    dataFromJavaScript = request.args.get('data')
    print(dataFromJavaScript)
    try:
        command  = dataFromJavaScript.split()
        print(command)
        dataToJavaScript = game.gameLogic(command[0],command[1])
        return jsonify(dataToJavaScript)
    except:
        print("error in python")
        return jsonify({"message":"error"})

if __name__ == '__main__':
    app.run(debug=True)
