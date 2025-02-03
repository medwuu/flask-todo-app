from flask import render_template, request, jsonify
from app import app, db
from app.models import Tasks
from flask_login import login_required, current_user


@app.route('/my', methods=['GET', 'POST'])
@login_required
def my():
    if request.method == 'POST':
        data = request.get_json()

        # добавление таски
        if data['form_type'] == "add":
            task_text = data['task'].strip()
            new_task = Tasks(task=task_text, owner=current_user.id)
            db.session.add(new_task)
            db.session.commit()

            return jsonify({
                'success': True,
                'id': new_task.id,
                'task': new_task.task,
                'creation_date': new_task.creation_date.strftime('%d.%m.%Y %H:%M')
            })

        # изменение состояния таски
        elif data['form_type'] == "edit":
            task_completed_id = data['id']
            is_task_completed = data['completed']
            task = Tasks.query.filter_by(id=task_completed_id, owner=current_user.id).first()
            task.completed = is_task_completed
            db.session.commit()

            return jsonify({
                'success': True,
                'id': task.id,
                'completed': task.completed
            })

        # удаление таски
        elif data['form_type'] == "delete":
            id_to_delete = data['id']
            Tasks.query.filter_by(id=id_to_delete, owner=current_user.id).delete()
            db.session.commit()

            return jsonify({
                'success': True,
                'id': id_to_delete
            })

    tasks = Tasks.query.filter_by(owner=current_user.id).all()
    return render_template('my.html', tasks=tasks)