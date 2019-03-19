"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort
from app.models import Profile
from app.forms import ProfileForm
from werkzeug.utils import secure_filename
from glob import glob
import re, time, os
 
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
    return render_template('about.html', name="Mary Jane")
    
@app.route("/profile",methods=["GET","POST"])
def profile():
    form=ProfileForm()
    if request.method=="POST" and form.validate_on_submit():
        firstname=form.firstname.data
        lastname=form.lastname.data
        gender=form.gender.data
        email=form.email.data
        location=form.location.data
        biography=form.biography.data
        print (biography)
        created_on = format_date_joined()
        
        image=request.files['photo']
        if allowed_file(image.filename):
            filename=secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            flash('Incorrect File Format','danger')
            return redirect(url_for('profile'))
        
        user=Profile(firstname,lastname,gender,email,location,biography,filename,created_on)
        db.session.add(user)
        db.session.commit()
        flash('File Saved','success')
        return redirect(url_for('profiles'))
    return render_template("profile.html", form=form)

@app.route('/profiles/')
def profiles():
    images = get_uploaded_images()
    users = Profile.query.all()
    return render_template("profiles.html", users=users, images=images)
    
@app.route("/profiles/<id>")
def user_profile(id):
    user = Profile.query.filter_by(id=id).first()
    images= get_uploaded_images()
    return render_template('profile_user.html', user=user, images=images)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)
    
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')
            
def format_date_joined():
    """format date"""
    dtime = time.strftime("%B %d, %Y")
    return dtime
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_UPLOADS']
           
def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)
    img = []
    for subdir, dirs, files in os.walk(rootdir + app.config['UPLOAD_FOLDER']):
        for file in files:
            img.append(os.path.join(subdir, file).split('/')[-1])
    return img


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
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
