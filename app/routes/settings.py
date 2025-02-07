from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import Users
from flask_login import login_required, current_user

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        old_password = request.form.get('old-password')
        new_password = request.form.get('new-password')
        repeat_password = request.form.get('repeat-password')

        if any(not x for x in (old_password, new_password, repeat_password)):
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
            flash("Пароль успешно обновлён!", "success")
            return redirect(url_for('settings'))
        else:
            flash("Старый пароль введён неверно!", "danger")
            return redirect(url_for('settings'))



    return render_template('settings.html')