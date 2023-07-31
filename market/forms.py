from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User 

class RegisterationForm(FlaskForm) :
    def validate_username(self, user_to_check) :
        user = User.query.filter_by(user_name=user_to_check.data).first()
        if user:
            raise ValidationError("UserName already exists ! Please try to register with different username")
        
    def validate_email_address(self, email_to_check) :
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email :
            raise ValidationError("Email Address already exists !!!")



    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    emailAddress = StringField(label='Email:', validators=[Email(), DataRequired()])
    password_1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password_2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label="Create Account")



class LoginForm(FlaskForm) :
    username = StringField(label='User Name:', validators= [DataRequired()])
    password = PasswordField(label='Password:', validators= [DataRequired()])
    submit = SubmitField(label="Login")



class PurchaseItemForm(FlaskForm) :
    submit = SubmitField(label="Purchase Item")



class SellItemForm(FlaskForm) :
    submit = SubmitField(label="Sell Item")