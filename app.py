from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    python_message = "LOL"
    cock = "MEOW!!!!!!"
    return render_template('index.html', python_message=python_message, cock=cock)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1212)