from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def calculate():
    number_of_vowels = 0
    if request.method == 'POST' and 'input_string' in request.form:
        input_string = request.form.get('input_string')
        for i in input_string:
            if i in 'aeiou':
                number_of_vowels += 1
    return render_template('index.html', number_of_vowels=number_of_vowels)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)