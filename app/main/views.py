from flask import jsonify, render_template, session, redirect, request, url_for, flash
from . import main
from .forms import ListForm, TaskForm
from .. import db
from ..models import Lis, Tasks, User
from flask.ext.login import login_required, current_user
import json
from flask.ext.mail import Message, Mail

@main.route('/')
def firstpage():
	return render_template('auth/firstpage.html')

@main.route('/index', methods=['GET','POST'])
@login_required
def index():
	list_form = ListForm()
	if list_form.validate():
		lis = Lis(title=list_form.title.data, author=current_user._get_current_object())
		db.session.add(lis)
		db.session.commit()
		flash('You have made a new List')
		return redirect(url_for('.index'))
	user = current_user._get_current_object()
	lists = user.lists.order_by(Lis.title).all()
	return render_template('index.html', lform=list_form, tform=TaskForm(), user=user, lists=lists)

@main.route('/task/<int:id>', methods=['GET','POST'])
def lis(id):
	lis = Lis.query.get_or_404(id)
	task_form = TaskForm()
	if request.method == 'POST' and task_form.validate():
		tas = Tasks(body=task_form.body.data, lis=lis)
		db.session.add(tas)
		db.session.commit()
		return redirect(url_for('.lis', id=lis.id))
	task_form.body.data = ''
	tasks = Tasks.query.order_by(Tasks.body).all()
	return render_template('task.html', lists=[lis], lform=ListForm(), tform=task_form, tasks=tasks)

@main.route('/delete/<int:id>', methods=['GET','POST'])
def delete_task(id):
	lis = Lis.query.get_or_404(id)
	if request.method == 'POST':
		db.session.delete(lis)
		db.session.commit()
		flash('List was deleted')
		return redirect(url_for('.index', lists=[lis]))

@main.route('/<int:id>', methods=['GET','POST'])
def send(id):
	lis = Lis.query.get_or_404(id)
	user = User.query.all()	

	msg = Message(lis.title, lis.tasks, sender='warengam@gmail.com', recipients=['warengam@gmail.com'] )
	msg.body = """From: %s &ls;%s&gt; %s""" % (user.username, user.email, msg)
	mail.send(msg)
	flash('Message Sent')
	return render_template('task.html', success=True)




@main.route('/task/', methods=['GET', 'POST'])
def show():
	# lis = Lis.query.get_or_404(id)
	lists = user.lists.order_by(Lis.title).all()
	return jsonify(lists=lists)





	