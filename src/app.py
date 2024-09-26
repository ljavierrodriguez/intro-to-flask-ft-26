from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def main():
    response = {
        "message": "API REST Flask"
    }
    return jsonify(response)


@app.route('/search', methods=['GET'])
def search():
    
    response = {
        "action": "/search",
        "query": request.args,
        "q": request.args.get('q'),
        "limit": request.args.get('limit')
    }

    return jsonify(response)


@app.route('/form', methods=['GET', 'POST'])
def form():

    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        age = request.form["age"]

        avatar = request.files.get('avatar')

        response = {
            "action": "/form",
            "form": request.form,
            "email": email,
            "password": password,
            "age": age,
            "avatar": avatar.filename
        }

        return jsonify(response)
    
@app.route('/json-data', methods=['POST', 'PUT'])
def json_data():
    

    email = request.json.get('email')
    password = request.json.get('password')
    age = request.json.get('age')

    response = {
        "action": "/json-data",
        "form": request.json,
        "email": email,
        "password": password,
        "age": age,
    }

    return jsonify(response)

@app.route('/people/<int:id>')
def get_people_by_id(id):

    response = {
        "action": f"/people/{id}",
        "id": id
    }

    return jsonify(response)

@app.route('/products/<int:id>/category/<int:category>')
def get_products(id, category):

    response = {
        "action": f"/product/{id}/category/{category}",
        "id": id,
        "category": category
    }

    return jsonify(response)

@app.route('/header-information')
def header_information():

    response = {
        "action": f"/header-information",
        "Authorization": request.headers.get('Authorization'),
        "token": request.headers.get('token'),
        "x-api-key": request.headers.get('x-api-key')
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)