from flask import render_template, session, redirect, request, url_for, flash
from . import main
from .forms import TaskForm, CardForm
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
		card = Cards(card=form1.card.data, author=current_user._get_current_object())
		db.session.add(card)
		db.session.commit()
		flash('You have made a new List')
		return redirect(url_for('.index'))
	user = current_user._get_current_object()
	cards = user.cards.order_by(Cards.created_time.desc()).all()
	return render_template('index.html', form1=form1, task_form=TaskForm(), user=user,
	 cards=cards)

@main.route('/tasks/<int:id>/', methods=['GET', 'POST'])
def task(id):
	"""
		Contains the url and form for adding a new task in a card
	"""
	card = Cards.query.get_or_404(id)
	task_form = TaskForm()
	if request.method == 'POST' and task_form.validate_on_submit():
		task = Tasks(task=task_form.tasks.data, card=card)
		db.session.add(task)
		db.session.commit()
		flash('You have made a new Task')
		return redirect(url_for('.task', id=card.id))
	task_form.tasks.data = ''
	tasks = Tasks.query.order_by(Tasks.task).all()
	return render_template('index.html', task_form=task_form, form1=CardForm(), tasks=[card])


@main.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_task(id):
	"""
		Contains the url and id for deleting a card in the database
	"""
	card = Cards.query.get_or_404(id)
	if request.method == 'POST':
		db.session.delete(task)
		db.session.commit()
		flash('Card deleted')
		return redirect(url_for('.index', cards=[task]))
