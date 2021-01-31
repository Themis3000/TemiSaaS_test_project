from flask import Flask

app = Flask(__name__)


@app.route('/<value>')
def hello_world(value):
    print(f"got {value}")
    return f'Hello World! {value}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
