from flask import Blueprint

systems = Blueprint('users', __name__)

# The following code is intended for creating new
# systems, updating existing systems data and visiting existing system. 
@systems.route('/systems')
def systems():
    return render_template('systems.html', title="Systems Data")

@systems.route('/systems/new', methods=['GET', 'POST'])
@login_required
def new_system():
    form = SystemForm()
    if form.validate_on_submit():
        system = System(system_name=form.system_name.data, sp_type=form.sp_type.data, author=current_user)
        db.session.add(system)
        db.session.commit()
        flash('A new system has been successfully added!', 'success')
        return redirect(url_for('home'))
    return render_template('new_system.html', title="New System",
        form=form, legend='Add System Data')

@systems.route('/systems/<int:system_id>', methods=['GET', 'POST'])
def system(system_id):
    system = System.query.get_or_404(system_id)
    return render_template('system.html', title=system.system_name, system=system)

@systems.route('/systems/<int:system_id>/update', methods=['GET', 'POST'])
@login_required
def update_system(system_id):
    system = System.query.get_or_404(system_id)
    form = SystemForm()
    if form.validate_on_submit():
        system.name = form.name.data
        system.sp_type = form.sp_type.data
        db.session.commit()
        flash('The system data has been successfully updated.', 'success')
        return redirect(url_for('system', system_id=system.id))
    elif request.method == 'GET':
        form.name.data = system.name
        form.sp_type.data = system.sp_type
    return render_template('new_system.html', title="Update System",
        form=form, legend="Update System Data", system=system)

@systems.route('/systems/<int:system_id>/delete', methods=['POST'])
@login_required
def delete_system(system_id):
    system = System.query.get_or_404(system_id)
    db.session.delete(system)
    db.session.commit()
    flash('The system has been deleted!', 'success')
    return redirect( url_for('home'))
