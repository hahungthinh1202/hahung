import json

from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    try:

        args = request.args
        number1 = float(args.get("number1"))
        number2 = float(args.get("number2"))
        total_sum = number1+number2
        response = {
            "Greeting": "Hello world",
            "Number1": number1,
            "Number2": number2,
            "TotalSum": total_sum
        }
        return json.dumps(response)
    except ValueError:
        response = {
            "error": "this 400"
        }
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status=400, mimetype='application/json')
        return http_response

@app.errorhandler(404)
def not_found(error):
    response = {
        "error": "this 404"
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=400, mimetype='application/json')
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)