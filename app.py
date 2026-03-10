from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>Simple Unit Converter</h1>
    <form action="/convert">
        Miles: <input name="miles">
        <input type="submit">
    </form>
    '''

@app.route("/convert")
def convert():
    miles = float(request.args.get("miles"))
    km = miles * 1.609
    return f"{miles} miles = {km:.2f} kilometers"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

