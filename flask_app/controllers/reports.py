from flask import render_template, redirect, request, session, url_for, flash, jsonify
from flask_app import app
from flask_app.models import report

@app.route('/report/<int:report_id>/json')
def show_one_report_json(report_id:int):
    if session.get('logged_in'):
        this_report = report.Report.get_one_json(report_id)
        if session.get('item_attempt'):
            session.pop('item_attempt')
        return jsonify({'this_report_json' : this_report})
    else:
        flash('Please Login', 'login')
    return redirect('/')

@app.get('/report/<int:report_id>')
def show_one_report(report_id:int):
    if session.get('logged_in'):
        this_report = report.Report.get_one(report_id)
        if this_report == False:
            flash('No such record!', 'unauthorized')
            return redirect(url_for('show_all_reports'))
        elif this_report.user.id != session.get('current_login'):
            flash("That's not yours!", 'unauthorized')
            return redirect(url_for('show_all_reports'))
        if session.get('list_attempt'):
            pre_fill = {
                'list_name': session['list_attempt']['list_name'],
            }
        else:
            pre_fill = {
                'list_name': '',
            }
        return render_template('show_one_report.html', this_report = this_report, pre_fill = pre_fill)
    else:
        flash('Please Login', 'login')
    return redirect('/')

@app.get('/dashboard')
def show_all_reports():
    if session.get('logged_in'):
        all_reports = report.Report.get_all()
        # if session.get('item_attempt'):
        #     session.pop('item_attempt')
        return render_template('show_all_reports.html', all_reports = all_reports)
    else:
        flash('Please Login', 'login')
    return redirect('/')

@app.route('/add_report', methods=["GET", "POST"])
def add_report() -> None:
    if session.get('logged_in'):
        if session.get('item_attempt'):
            session.pop('item_attempt')
        if request.method == "GET":
            if session.get('report_attempt'):
                pre_fill = {
                    'location': session['report_attempt']['location'],
                    'date': session['report_attempt']['date'],
                    'description': session['report_attempt']['description'],
                    'offense': session['report_attempt']['offense'],
                    'img_file': session['report_attempt']['img_file'],
                }
            else:
                pre_fill = {
                    'location': '',
                    'date': '',
                    'description': '',
                    'offense': '',
                    'img_file': '',
                }
            return render_template('new_report.html', pre_fill = pre_fill)
        elif request.method == "POST":
            if report.Report.is_legit_report(request.form):
                new_report = report.Report.insert_one(request.form)
                if session.get('report_attempt'):
                    session.pop('report_attempt')
                return redirect(url_for('show_all_reports'))
            session['report_attempt'] = request.form
        return redirect('/add_report')
    else:
        flash('Please Login', 'login')
    return redirect('/dashboard')

@app.get('/report/<int:report_id>/delete')
def delete_report(report_id:int) -> None:
    if session.get('logged_in'):
        if session.get('item_attempt'):
            session.pop('item_attempt')
        this_report = report.Report.get_one(report_id)
        if not this_report:
            flash('No such record!', 'unauthorized')
            return redirect(url_for('show_all_reports'))
        elif this_report.user_id != session.get('current_login'):
            flash("That's not yours!", 'unauthorized')
            return redirect(url_for('show_all_reports'))
        report.Report.delete_one(report_id)
        return redirect(url_for('show_all_reports'))
    else:
        flash('Please Login', 'login')
    return redirect('/')

@app.route('/report/<int:report_id>/edit', methods=["GET", "POST"])
def edit_report(report_id:int) -> None:
    this_report = report.Report.get_one(report_id)
    if not this_report:
        flash('No such record!', 'unauthorized')
        return redirect(url_for('show_all_reports'))
    elif this_report.user_id != session.get('current_login'):
        flash("That's not yours!", 'unauthorized')
        return redirect(url_for('show_all_reports'))
    if session.get('logged_in'):
        if request.method == "GET":
            if session.get('edit_attempt'):
                pre_fill = {
                    'location': session['edit_attempt']['location'],
                    'date': session['edit_attempt']['date'],
                    'description': session['edit_attempt']['description'],
                    'offense': session['edit_attempt']['offense'],
                    'img_file': session['edit_attempt']['img_file'],
                    'is_cleaned': session['edit_attempt']['is_cleaned'],
                }
            else:
                pre_fill = {
                    'location': this_report.location,
                    'date': this_report.date,
                    'description': this_report.description,
                    'offense': this_report.offense,
                    'img_file': this_report.img_file,
                    'is_cleaned': this_report.is_cleaned,
                }
            return render_template('edit_report.html', pre_fill = pre_fill, report_id = report_id)
        elif request.method == "POST":
            if report.Report.is_legit_report(request.form):
                updated_report = report.Report.update_one(request.form)
                if session.get('edit_attempt'):
                    session.pop('edit_attempt')
                return redirect(url_for('show_one_report', report_id = report_id))
            session['edit_attempt'] = request.form
        return redirect(url_for('edit_report', report_id = report_id))
    else:
        flash('Please Login', 'login')
    return redirect('/')

@app.get('/report/<int:report_id>/edit/link')
def edit_report_from_link(report_id:int) -> None:
    if session.get('logged_in'):
        if session.get('edit_attempt'):
            session.pop('edit_attempt')
    else:
        flash('Please Login', 'login')
    return redirect(url_for('edit_report', report_id = report_id))