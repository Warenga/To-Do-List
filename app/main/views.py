from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import ListForm, TaskForm
from .. import db
from ..models import Lis, Tasks

@main.route('/', methods=['GET', 'POST'])
def index():
	form = ListForm()
	if form.validate_on_submit():
		lis = Lis(title=form.title.data)
		db.session.add(lis)
		flash('You have made a new List')
		return redirect(url_for('.index'))
	lists = Lis.query.order_by(Lis.title).all()
	return render_template('index.html', form=form, lists=lists)

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
