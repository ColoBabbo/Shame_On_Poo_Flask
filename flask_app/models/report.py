from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
import os, sys, requests, re
from PIL import Image
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse, unquote

class Report:
    db = 'shame_on_poo_schema'

    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.user_id = data['user_id']
        self.location = data['location']
        self.date = data['date']
        self.description = data['description']
        self.offense = data['offense']
        self.is_cleaned = data['is_cleaned']
        self.img_file = data['img_file']
        self.user = {}

    def __repr__(self) -> str:
        return f'Report: {self.id} | Offense: {self.offense} | Date: {self.date}\nImg: {self.img_file} | Cleaned: {self.is_cleaned}'

    @classmethod
    def url_cleaner(cls, url):
        urlparse(url).path
        url_parsed = urlparse(url)
        file_path = unquote(Path(re.sub( r"\s+", '_', unquote(url_parsed.path))).name)
        final_path = str(file_path).replace(os.sep, '/')
        return final_path

    @classmethod
    def save_url_to_static_images(cls, form_data):
        if not form_data.get('img_file'):
            return ''
        response = requests.get(form_data['img_file'])
        response.raise_for_status()
        this_image = Image.open(BytesIO(response.content))
        this_image_file_name = cls.url_cleaner(form_data['img_file'])
        this_image.save(f'flask_app/static/images/{this_image_file_name}')
        return this_image_file_name

    @classmethod
    def get_one_json(cls, report_id:int) -> object:
        query = """
                SELECT * FROM reports
                LEFT JOIN users ON reports.user_id = users.id
                WHERE reports.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, {'id': report_id})
        return results

    @classmethod
    def get_all(cls) -> list:
        query = """
                SELECT * FROM reports
                LEFT JOIN users ON reports.user_id = users.id;
        """
                # WHERE users.id = %(user_id)s;
        results = connectToMySQL(cls.db).query_db(query) #, {'user_id' : session.get('current_login')})
        all_reports = []
        for report in results:
            this_report = cls(report)
            user_data = {
                'id': report['users.id'],
                'first_name': report['first_name'],
                'last_name': report['last_name'],
                'email': report['email'],
            }
            this_report_user = user.User(user_data)
            this_report.user = this_report_user
            all_reports.append(this_report)
        return all_reports

    @classmethod
    def get_one(cls, report_id:int) -> object:
        query = """
                SELECT * FROM reports
                LEFT JOIN users ON reports.user_id = users.id
                WHERE reports.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, {'id': report_id})
        if results:
            this_result = results[0]
            this_report = cls(this_result)
            user_data = {
                'id': this_result['users.id'],
                'first_name': this_result['first_name'],
                'last_name': this_result['last_name'],
                'email': this_result['email'],
            }
            this_report_user = user.User(user_data)
            this_report.user = this_report_user
            return this_report
        else:
            return False

    @classmethod
    def check_one_by_description_and_offense(cls, form_dict) -> bool:
        query = """
                SELECT * FROM reports
                WHERE description = %(description)s AND offense = %(offense)s;
        """
        results = connectToMySQL(cls.db).query_db(query, form_dict)
        if results:
            return True
        else:
            return False

    @classmethod
    def update_one(cls, form_dict:dict) -> None:
        query = """
                UPDATE reports
                SET location = %(location)s, date = %(date)s, description = %(description)s, offense = %(offense)s, is_cleaned = %(is_cleaned)s, img_file = %(img_file)s
                WHERE id = %(id)s;
        """
        data = {
            'id': form_dict['id'],
            'location': form_dict['location'],
            'date': form_dict['date'],
            'description': form_dict['description'],
            'offense': form_dict['offense'],
            'img_file': form_dict['img_file'],
            'is_cleaned': ( 1 if form_dict.get('is_cleaned') else 0 ),
        }
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def insert_one(cls, form_dict:dict) -> int:
        query = """
                INSERT INTO reports ( location, date, description, offense, img_file, user_id )
                VALUES ( %(location)s, %(date)s, %(description)s, %(offense)s, %(img_file)s, %(user_id)s );
        """
        return connectToMySQL(cls.db).query_db(query, form_dict)

    @classmethod
    def delete_one(cls, report_id:int) -> None:
        query = """
                DELETE FROM reports
                WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, {"id": report_id})

    @classmethod
    def is_legit_report(cls, form_dict:dict) -> bool:
        valid_input = True
        if not len(form_dict.get('description')) > 0 :
            flash('Your report needs a description!', 'description')
            valid_input = False
        elif not len(form_dict.get('description')) >= 3:
            flash('description must be at least 3 characters.', 'description')
            valid_input = False
        elif cls.check_one_by_description_and_offense(form_dict) and form_dict.get('new_report'):
            flash(f'This report has already been added.', 'description')
            flash(f'This report has already been added.', 'offense')
            valid_input = False
        if not len(form_dict.get('location')) > 0 :
            flash('Your report needs a Location!', 'location')
            valid_input = False
        elif not len(form_dict.get('location')) >= 3:
            flash('Location must be at least 3 characters.', 'location')
            valid_input = False
        if not form_dict.get('offense'):
            flash('Your report must specify the Offense.', 'offense')
            valid_input = False
        if not form_dict.get('date'):
            flash("Your report must have a Date.", 'date')
            valid_input = False
        return valid_input