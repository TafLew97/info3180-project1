"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os, time
from app import app,db
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
from app.forms import ProfileForm
from app.models import UserProfile
rootdir = os.getcwd()

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    

@app.route('/profile',methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            firstname  = form.firstname.data
            lastname   = form.lastname.data
            email      = form.email.data
            biography  = form.biography.data
            location   = form.location.data
            gender     = form.gender.data
                
            created_on= format_date_joined()
            
            photo      = form.photo.data
            filename   = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename)) 
            
            User=UserProfile(firstname=firstname,lastname=lastname,email=email,location=location,gender=gender,created_on=created_on,filename=filename,biography=biography)
            db.session.add(User)
            db.session.commit()
            
            flash("User Created Successfully!")
            return redirect(url_for("viewprofiles"))
        else:
            flash_errors(form)

            
    return render_template('profile.html',form=form)
    
  

@app.route('/profiles')
def viewprofiles():
    profiles = db.session.query(UserProfile).all()
    return render_template('profiles.html',profiles=profiles )
    
    
@app.route('/profile/<userid>')
def userprofile(userid):
    User = UserProfile.query.get(userid)
    return render_template("userprofile.html", User=User)
        
    
###
# The functions below should be applicable to all Flask apps.
###
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (getattr(form, field).label.text,error))

def format_date_joined():
    """format date"""
    dtime = time.strftime("%B %d, %Y")
    return dtime


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")