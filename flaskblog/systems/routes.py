from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import System
from flaskblog.systems.forms import SystemForm

systems_bp = Blueprint('systems', __name__)

@systems_bp.route("/systems/")
def systems():
    systems = System.query.all()
    return render_template('systems.html', title="System Catalogue", systems=systems)

@systems_bp.route("/systems/new", methods=['GET', 'POST'])
@login_required
def new_system():
    form = SystemForm()
    if form.validate_on_submit():
        system = System(**{k: v for k, v in form.data.items() if k not in ['csrf_token', 'submit']}, 
            author=current_user)
        db.session.add(system)
        db.session.commit()
        flash('The system entry has been successfully added for ', 'success')
        return redirect(url_for('systems.system', system_id=system.id))
    return render_template('system_new.html', title="Add a system entry", form=form, legend='Add New System')

@systems_bp.route("/system/<int:system_id>", methods=['GET', 'POST'])
def system(system_id):
    system = System.query.get_or_404(system_id)
    return render_template('system.html', title=system.system_name, system=system)

@systems_bp.route("/systems/<int:system_id>/update", methods=['GET', 'POST'])
@login_required
def update_system(system_id):
    system = System.query.get_or_404(system_id)
    form = SystemForm(obj=system)
    if form.validate_on_submit():
        form.populate_obj(system)
        db.session.commit()
        flash('The system entry has been updated', 'success')
        return redirect(url_for('systems.system', system_id=system.id))
    elif request.method == 'GET':
        form.populate_obj(system)  
    return render_template('system_new.html', title="Update a system entry", form=form, legend='Update System')

@systems_bp.route("/systems/<int:system_id>/delete", methods=['POST'])
@login_required
def delete_system(system_id):
    system = System.query.get_or_404(system_id)
    db.session.delete(system)
    db.session.commit()
    flash('The system entry has been deleted', 'success')
    return redirect(url_for('main.home'))