# Flask
from flask import jsonify

# Third-party
from utils import get_info
from settings import app


@app.route('/', methods=['GET', 'POST'])
def main_page():
    data = get_info()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)