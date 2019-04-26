# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/workouts')
@login_required
def workouts():
    return render_template('workouts.html', name=current_user.name)

@main.route('/meal_plans')
@login_required
def meal_plans():
    return render_template('plans.html', name=current_user.name)

@main.route('/tools')
@login_required
def tools():
    return render_template('tools.html', name=current_user.name)

@main.route('/about')
@login_required
def about():
    return render_template('about.html', name=current_user.name)

#All routes for workouts:
@main.route('/warm_up')
@login_required
def warm_up():
    return render_template('warmup.html', name=current_user.name)

@main.route('/build_total_body_strength')
@login_required
def build_total_body_strength():
    return render_template('bodystrength.html', name=current_user.name)

@main.route('/train_your_body_in_5_minutes')
@login_required
def train_your_body_in_5_minutes():
    return render_template('train.html', name=current_user.name)

@main.route('/improve_your_endurance')
@login_required
def improve_your_endurance():
    return render_template('endurance.html', name=current_user.name)


#All routes for meal plans:

@main.route('/the_beginner_meal_plan')
@login_required
def the_beginner_meal_plan():
    return render_template('beg.html', name=current_user.name)

@main.route('/the_get_lean_meal_plan')
@login_required
def the_get_lean_meal_plan():
    return render_template('lean.html', name=current_user.name)

@main.route('/the_skinny_guy_muscle_gain_plan')
@login_required
def the_skinny_guy_muscle_gain_plan():
    return render_template('gain.html', name=current_user.name)


#All routes for tools:
@main.route('/bmi_tool')
@login_required
def bmi_tool():
    return render_template('bmi.html', name=current_user.name)