from flask import render_template, flash, redirect, session, url_for, request, g
from app import app
from datetime import datetime

@app.route('/')
@app.route('/start')
def start():
    return render_template('start.html')

    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/project')
def project():
    return render_template('Project.html')

@app.route('/influenced')
def influenced():
    return render_template('Influenced.html')        

@app.route('/contact')
def contact_view():
    return render_template('Contact.html')

@app.route('/about')
def about_view():
    return render_template('About.html')          



    