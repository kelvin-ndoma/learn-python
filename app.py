from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    result = "Hello from your Python script!"
    return f"<h1>{result}</h1>"

if __name__ == '__main__':
    app.run()
