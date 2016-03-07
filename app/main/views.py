from flask import jsonify, render_template, session, redirect, request, url_for, flash
from . import main
from .forms import TaskForm, CardForm, UserForm
from ..import db
from ..models import User, Cards, Tasks
from flask.ext.login import login_required, current_user
import json
from datetime import datetime

@main.route('/index', methods=['GET', 'POST'])
@login_required
def index():
	"""
		Contains the url and form for adding a new card
	"""
	form1 = CardForm()
	if form1.validate_on_submit():
		cad = Cards(card=form1.card.data)
		db.session.add(cad)
		db.session.commit()
		flash('You have made a new List')
		return redirect(url_for('.index'))
	user = current_user._get_current_object()
	cards = user.cards.order_by(Cards.card).all()
	return render_template('index.html', form1=form1, task_form=TaskForm(), user=user,
	 cards=cards)

@main.route('/tasks/<int:id>/', methods=['GET', 'POST'])
def task(id):
	"""
		Contains the url and form for adding a new task in a card
	"""
	cad = Cards.query.get_or_404(id)
	task_form = TaskForm()
	if request.method == 'POST' and task_form.validate_on_submit():
		task = Tasks(task=task_form.tas.data, cad=cad)
		db.session.add(task)
		db.session.commit()
		flash('You have made a new Task')
		return redirect(url_for('.index'))
	tasks = str(Tasks.query.order_by(Tasks.task).all())
	return render_template('index.html', task_form=task_form, form1=CardForm(), cards=[cad], tasks=str(tasks))


@main.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_card(id):
	"""
		Contains the url and id for deleting a card in the database
	"""
	cad = Cards.query.get_or_404(id)
	if request.method == 'POST':
		db.session.delete(cad)
		db.session.commit()
		flash('Card deleted')
		return redirect(url_for('.index', cards=[cad]))


@main.route('/delete/task/<int:id>', methods=['GET', 'POST'])
def delete_task(id):
	"""
		Contains the url and id for deleting a tasks in the database
	"""
	task = Tasks.query.get_or_404(id)
	if request.method == 'POST':
		db.session.delete(task)
		db.session.commit()
		flash('Task deleted')
		return redirect(url_for('.index', tasks=[task]))

@main.route('/settings')
@login_required
def settings():
	form = UserForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.email = form.email.data
		current_user.password = form.password.data
		db.session.add(user)
		flash('Your settings have been changed')
		return redirect('/index')
	form.username.data = current_user.username
	form.email.data = current_user.email
	return render_template('settings.html', form=form)




