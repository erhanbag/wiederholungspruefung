from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from forms import CreateTodoForm, RegisterForm, LoginForm, TodoForm
from flask_bcrypt import Bcrypt
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

app = Flask(__name__)
app.static_folder = 'static'
app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, Todo, List, User, insert_sample  # (1.)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/index')
@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error_message = None 

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('todos'))
            else:
                error_message = 'The password is wrong, please try again.'
                return render_template('login.html', form=form, error_message=error_message)
        else:
            error_message = "The user doesn't exist, please try again."
            return render_template('login.html', form=form, error_message=error_message)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Check if the username already exists in the database
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            error_message = 'That username already exists. Please choose a different one.'
            return render_template('register.html', form=form, error_message=error_message)
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('todos'))
    return render_template('register.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()

    return redirect(url_for('login'))




@app.route('/todos/', methods=['GET', 'POST'])
@login_required
def todos():
    form = CreateTodoForm()
    if request.method == 'GET':
        todos = db.session.execute(db.select(Todo).order_by(Todo.id)).scalars()  # !!
        return render_template('todos.html', todos=todos, form=form)
    else:  # request.method == 'POST'
        if form.validate():
            todo = Todo(description=form.description.data)  # !!
            db.session.add(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been created.', 'success')
        else:
            flash('No todo creation: validation error.', 'warning')
        return redirect(url_for('todos'))

@app.route('/todos/<int:id>', methods=['GET', 'POST'])
@login_required
def todo(id):
    todo = db.session.get(Todo, id)  # !!
    form = TodoForm(obj=todo)  # (2.)  # !!
    if request.method == 'GET':
        if todo:
            if todo.lists: form.list_id.data = todo.lists[0].id  # (3.)  # !!
            choices = db.session.execute(db.select(List).order_by(List.name)).scalars()  # !!
            form.list_id.choices = [(0, 'List?')] + [(c.id, c.name) for c in choices]  # !!
            return render_template('todo.html', form=form)
        else:
            abort(404)
    else:  # request.method == 'POST'
        if form.method.data == 'PATCH':
            if form.validate():
                form.populate_obj(todo)  # (4.)
                todo.populate_lists([form.list_id.data])  # (5.)  # !!
                db.session.add(todo)  # !!
                db.session.commit()  # !!
                flash('Todo has been updated.', 'success')
            else:
                flash('No todo update: validation error.', 'warning')
            return redirect(url_for('todo', id=id))
        elif form.method.data == 'DELETE':
            db.session.delete(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been deleted.', 'success')
            return redirect(url_for('todos'), 303)
        else:
            flash('Nothing happened.', 'info')
            return redirect(url_for('todo', id=id))

@app.route('/lists/')
@login_required
def lists():
    lists = db.session.execute(db.select(List).order_by(List.name)).scalars()  # (6.)  # !!
    return render_template('lists.html', lists=lists)

@app.route('/lists/<int:id>')
@login_required
def list(id):
    list = db.session.get(List, id)  # !!
    if list is not None:
        return render_template('list.html', list=list)
    else:
        return redirect(url_for('lists'))

@app.route('/insert/sample')
def run_insert_sample():
    insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

@app.get('/faq/<css>')
@app.get('/faq/', defaults={'css': 'default'})
def faq(css):
    return render_template('faq.html', css=css)

@app.get('/ex/<int:id>')
@app.get('/ex/', defaults={'id':1})
def ex(id):
    if id == 1:
        return render_template('ex1.html')
    elif id == 2:
        return render_template('ex2.html')
    else:
        abort(404)