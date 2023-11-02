from flask import Flask, request
from app import app
from flask import jsonify
from flask_httpauth import HTTPBasicAuth 
from db import User, Todo, db
import controller


auth = HTTPBasicAuth()

@app.route("/api/todos/", methods=['GET'])
@auth.login_required
def api_todos():
    current_user = auth.current_user()
    user_data = User.query.filter_by(username=current_user).first()
    todos = Todo.query.filter_by(user_id=user_data.id).order_by(Todo.id).all()

    todos_data = []
    for todo in todos:
        todo_info = {
            'id': todo.id,
            'complete': todo.complete,
            'description': todo.description,
            'user_id': todo.user_id
            
        }
        todos_data.append(todo_info)

    respuesta = {'todos': todos_data}

    return jsonify(respuesta)


@app.route('/api/todos/delete/<int:todo_id>', methods=['DELETE'])
@auth.login_required
def delete_todo(todo_id):
    print(todo_id)
    current_user = auth.current_user()
    user_data = User.query.filter_by(username=current_user).first()
    todo = Todo.query.filter_by(id=todo_id, user_id=user_data.id).first()

    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'message': f'Todo with ID {todo_id} deleted succesfully.'})
    else:
        return jsonify({'error': 'The specified "todo" was not found.'}), 404

@app.route('/api/todos', methods=['POST'])
@auth.login_required
def add_todo():
    current_user = auth.current_user()
    user_data = User.query.filter_by(username=current_user).first()
    data = request.get_json()

    if 'description' in data:
        new_todo = Todo(description=data['description'], user_id=user_data.id)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({'message': 'New todo added succesfully.'}), 201
    else:
        return jsonify({'error': 'The todo description is required.'}), 400


@app.route('/api/todos/<int:todo_id>', methods=['PATCH'])
@auth.login_required
def update_todo(todo_id):
    current_user = auth.current_user()
    print(current_user)
    user_data = User.query.filter_by(username=current_user).first()
    todo = Todo.query.filter_by(id=todo_id, user_id=user_data.id).first()

    if not todo:
        return jsonify({'error': 'The specified "todo" was not found.'}), 404

    data = request.get_json()

    if 'description' in data:
        todo.description = data['description']

    if 'complete' in data:
        todo.complete = data['complete']

    if 'user_id' in data:
    
        if current_user != user_data.username:
            return jsonify({'error': 'You do not have permission to change the owner.'}), 403
        new_user = User.query.filter_by(id=data['user_id']).first()
        if new_user:
            todo.user_id = new_user.id
        else:
            return jsonify({'error': 'The specified user does not exist.'}), 400

    db.session.commit()

    return jsonify({'message': f'Todo with ID {todo_id} updated successfully.'})


@auth.verify_password
def authenticate(username, password):
    if username and password:
            user_validation = controller.validate_api_user(username)

            if user_validation is None:
                return False 
            else:
                pass_validation = controller.validate_api_password(username, password)
                if pass_validation is None:
                    return False 
                else:
                    return True
    return False


