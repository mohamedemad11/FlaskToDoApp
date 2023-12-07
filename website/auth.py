from flask import Blueprint , render_template ,request ,flash

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/SignUp',methods= ['GET','POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        firstname= request.form.get('firstName')
        lastname = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2= request.form.get('password2')
        if len(email) < 4 :
            flash('Email Must be larger than 4 characters !',category='error') 
        elif len(firstname) < 2 :
            flash('First Name Must be larger than 4 characters !',category='error')
        elif len(lastname) < 2 :
            flash('Last Name must be more than 4 characters  !',category='error')
        elif password1 != password2 :
            flash('Passwords Don\'t Match !',category='error')
        elif len(password1) < 7 :
            flash('The Password must be more than 6 !',category='error')
        else :
            flash('Account Created Successfully !' ,category='success')
    return render_template('signup.html',text = "Hello Hard Worker ! :) ")


