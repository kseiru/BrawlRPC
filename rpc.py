from flask import Flask

app = Flask(__name__)

@app.route('/api')
def main_page():
    return "Welcome to the unofficial brawl stars API!\nYou will not need an API key here!"

if __name__ == "__main__":
    app.run(host="81.177.165.173", port=80)