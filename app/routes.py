from flask import render_template, redirect, url_for, request, flash, abort
from app import app, db, login_manager
from app.models import User
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from is_safe_url import is_safe_url

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
  return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect('/login')
  return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and user.check_password(form.password.data):
      login_user(user, remember=form.remember.data)
      flash('Login Successful')
      next = request.args.get('next')
      # print(f'The next url is: {next}')
      if next and not is_safe_url(next, {app.config.get('SERVER_NAME')}):
        return abort(400)
      return redirect(next or url_for('dashboard', username=form.username.data))
    else:
      flash('No Such User or Bad Password')
  return render_template('login.html', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect('/')

@app.route('/dashboard/<username>')
@login_required
def dashboard(username):
  if username != current_user.username:
    abort(401)
  return render_template('dashboard.html')
