from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import Users
from flask_login import login_required, current_user

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        # пустая форма
        if sum(1 for value in request.form.values() if value.strip()) == 0:
            flash("Нет параметров для изменения!", "danger")
            return redirect(url_for('settings'))

        # смена имени
        new_name = request.form.get('new-name')
        if new_name:
            if len(new_name) > 50:
                flash("Длина имени не может быть больше 50 символов!", "danger")
                return redirect(url_for('settings'))
            user = Users.query.filter_by(id=current_user.id).first()
            user.name = new_name
            db.session.commit()

        # смена email
        new_email = request.form.get('new-email')
        if new_email:
            if len(new_email) > 50:
                flash("Длина Email не может быть больше 50 символов!", "danger")
                return redirect(url_for('settings'))
            user = Users.query.filter_by(id=current_user.id).first()
            user.email = new_email
            db.session.commit()

        # смена пароля
        old_password = request.form.get('old-password')
        new_password = request.form.get('new-password')
        repeat_password = request.form.get('repeat-password')
        password_args_count = len([x for x in [old_password, new_password, repeat_password] if x])

        if password_args_count > 0:
            if password_args_count != 3:
                flash("Заполните все поля!", "danger")
                return redirect(url_for('settings'))
            if new_password != repeat_password:
                flash("Пароли не совпадают!", "danger")
                return redirect(url_for('settings'))
            if new_password == old_password:
                flash("Новый пароль совпадает со старым!", "danger")
                return redirect(url_for('settings'))

            user = Users.query.filter_by(id=current_user.id).first()
            if user and user.checkPassword(old_password):
                user.hashPassword(new_password)
                db.session.commit()
            else:
                flash("Старый пароль введён неверно!", "danger")
                return redirect(url_for('settings'))

        flash("Данные успешно обновлёны!", "success")
        return redirect(url_for('settings'))

    return render_template('settings.html')