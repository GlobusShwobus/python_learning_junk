from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up',methods = ['GET', 'POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<4:
            flash('Email must be greater than 4 chars', category='error')
            pass
        elif len(firstName)<2:
            flash('first name must be greater than 2 chars', category='error')
            pass
        elif password1!=password2:
            flash('passwords dont match', category='error')
            pass
        elif len(password1)<7:
            flash('password too shlong', category='error')
            pass
        else:
            #add user
            flash('account created', category='success')
            pass

    return render_template("signup.html")