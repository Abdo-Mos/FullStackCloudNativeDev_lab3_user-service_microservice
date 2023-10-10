# user_service.py

from flask import Flask, jsonify, request

app = Flask(__name__)


users = [ 
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

# users = {
#     '1': {'name': 'Alice', 'email': 'alice@example.com'},
#     '2': {'name': 'Bob', 'email': 'bob@example.com'}
# }


@app.route('/')
def home():
    return "Hello from User Service!"

# -R- read user by id Route
@app.route('/user/<id>')
def user(id):
    # user_info = users.get(id, {})
    # user_info = users['id'] = id
    user = None
    for usr in users:
        if int(usr['id']) == int(id):
            user = usr
            break

    if user == None:
        return jsonify({'error:': 'user not found'})
    
    return jsonify({'found': user})

# -C- create user 
@app.route('/user', methods=['POST'])
def create_user():
    # lool = {request.json['id']: {'name': request.json['name'], 'email': request.json['email']}}
    # users[request.json['id']] = {'name': request.json['name'], 'email': request.json['email']}
    # users = lool
    new_user = {
        'id': request.json['id'],
        'name': request.json['name'],
        'email': request.json['email']
    }
    users.append(new_user) 
    return users

if __name__ == '__main__':
    app.run(port=5000)