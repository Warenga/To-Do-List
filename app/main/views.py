from flask import render_template, session, redirect, request, url_for, flash
from . import main
from .forms import ListForm, TaskForm
from .. import db
from ..models import Lis, Tasks, User
from flask.ext.login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
	form = ListForm()
	if form.validate_on_submit():
		lis = Lis(title=form.title.data, author=current_user._get_current_object())
		db.session.add(lis)
		flash('You have made a new List')
		return redirect(url_for('.index'))
	user = current_user._get_current_object()
	lists = user.lists.order_by(Lis.title).all()
	return render_template('index.html', form=form, user=user, lists=lists)

@main.route('/task/<int:id>', methods=['GET', 'POST'])
def lis(id):
	lis = Lis.query.get_or_404(id)
	form = TaskForm()
	if form.validate_on_submit():
		tas = Tasks(body=form.body.data, lis=lis)
		db.session.add(tas)
		flash('Task added to List')
		return redirect(url_for('.lis', id=lis.id))
	form.body.data = ''
	tasks = Tasks.query.order_by(Tasks.body).all()
	return render_template('task.html', lists=[lis], form=form, tasks=tasks)

@main.route('/delete/<int:id>', methods=['GET','POST'])
def delete_task(id):
	lis = Lis.query.get_or_404(id)
	if request.method == 'POST':
		db.session.delete(lis)
		db.session.commit()
		flash('Entry was deleted')
		return redirect(url_for('.index', lists=[lis]))

	