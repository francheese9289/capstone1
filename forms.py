from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from models import Staff, User


# def staff_member_check(email):
#     staff_member = Staff.query.filter_by(email=email).first()
#     if staff_member:
#         first = staff_member.first_name
#         last = staff_member.last_name
#         new_user = [{'username':User.create_username(first, last),
#                    'email': email,
#                    'first_name' = first,
#                    'last_name' = last,
                   
#       }]
#     else:
#         pass
            
#     db.session.add(new_user)
#     db.session.commit()
#     flash(f'You have successfully created a user account {email}', 'User-created')
#     return redirect(url_for('site.home'))
#     except:
#         raise Exception('Invalid form data: Please check your form')
#     return render_template('sign_up.html', form=form)


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class CheckUserForm

class UserSignUpForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()]) 
    username = StringField('Username', validators = [])
    password = PasswordField('Password', validators = [DataRequired()])
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

    


