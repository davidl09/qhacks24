from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/')


if __name__ == "__main__":
    app.run(debug=True)