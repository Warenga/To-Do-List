from flask import render_template, redirect, url_for
from . import main
from .forms import ListForm, TaskForm

@main.route('/', methods=['GET', 'POST'])
def index():
	title = None
	form = ListForm()
	if form.validate_on_submit():
		title = form.title.data
		flash('You have made a new List')
		return redirect(url_for('.index', title=title))
	form.title.data = ''
	return render_template('index.html', form=form, title=title)


@main.route('/task', methods=['GET', 'POST'])
def task():
	form = TaskForm()
	if form.validate_on_submit():
		body = form.body.data
		flash('Task added to List')
		return redirect(url_for('.task', body=body))
	form.body.data = ''
	return render_template('task.html', form=form)