from flask import render_template, redirect, request, session, url_for, flash, jsonify, send_from_directory
from flask_app import app
from flask_app.models import report
import re, os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'flask_app/static/images'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1000 * 1000


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        return render_template('show_one_report.html', this_report = this_report)
    else:
        flash('Please Login', 'login')
    return redirect('/')

@app.get('/dashboard')
def show_all_reports():
    if session.get('logged_in'):
        all_reports = report.Report.get_all()
        return render_template('show_all_reports.html', all_reports = all_reports)
    else:
        flash('Please Login', 'login')
    return redirect('/')

@app.route('/add_report', methods=["GET", "POST"])
def add_report() -> None:
    if session.get('logged_in'):
        # if session.get('item_attempt'):
        #     session.pop('item_attempt')
        if request.method == "GET":
            if session.get('report_attempt'):
                pre_fill = {
                    'location': session['report_attempt']['location'],
                    'date': session['report_attempt']['date'],
                    'description': session['report_attempt']['description'],
                    'offense': session['report_attempt']['offense'],
                }
            else:
                pre_fill = {
                    'location': '',
                    'date': '',
                    'description': '',
                    'offense': '',
                }
            return render_template('new_report.html', pre_fill = pre_fill)
        elif request.method == "POST":
            if 'img_file' not in request.files:
                img_filename = report.Report.save_url_to_static_images(request.form)
            else:
                img_file = request.files['img_file']
                if img_file and allowed_file(img_file.filename):
                    img_filename = secure_filename(img_file.filename)
                    img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
            if report.Report.is_legit_report(request.form):
                data = {
                    'location': request.form['location'],
                    'date': request.form['date'],
                    'description': request.form['description'],
                    'offense': request.form['offense'],
                    'img_file': img_filename,
                    'user_id': session['current_login'],
                }
                new_report = report.Report.insert_one(data)
                if session.get('report_attempt'):
                    session.pop('report_attempt')
                return redirect(url_for('show_one_report', report_id = new_report))
            session['report_attempt'] = request.form
        return redirect('/add_report')
    else:
        flash('Please Login', 'login')
    return redirect('/dashboard')

@app.get('/report/<int:report_id>/delete')
def delete_report(report_id:int) -> None:
    if session.get('logged_in'):
        # if session.get('item_attempt'):
        #     session.pop('item_attempt')
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

# FUTURE: ~ Andrew
# Add SQL IF to validate user owns the report
# Break route into GET and POST routes
# use request.form to rerender template on POST route if validation fails
# pre-populate inputs with request.form or database data instead of using session

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
                updated_report = report.Report.update_one(request.form, report_id)
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