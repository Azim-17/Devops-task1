from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def abc():
    name = None

    if request.method == 'GET':
        name = request.args.get('name')
    else:
        if request.is_json:
            data = request.get_json(silent=True) or {}
            name = data.get('name')
        else:
            name = request.form.get('name') or request.values.get('name')
            if not name:
                raw = request.data.decode().strip()
                if raw:
                    name = raw

    if not name:
        name = "stranger"

    return f"Hello {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9097)
