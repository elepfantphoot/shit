from wtforms import * # IntegerField, Form, StringField, RadioField, SelectField, TextAreaField, validators, BooleanField
from wtforms.validators import InputRequired, EqualTo, NumberRange, Length, ValidationError
from wtforms.fields import EmailField, DateField, PasswordField, IntegerField, Field
from datetime import datetime
from wtforms.validators import ValidationError


def date_cannot_be_in_the_past(form, field):
    if field.data and field.data < datetime.utcnow():
        raise ValidationError('Date cannot be in the past')

# def number_only(form, field):
#    if not field.data.isdigit():
#        raise ValidationError("This field must contain numbers only.")


# def letters_only(form, field):
#    if field.data.isdigit():
#        raise ValidationError("This field must contain letters only.")


class CreateReminderForm(Form):
    name = StringField('Written By', [validators.Length(min=1, max=150), validators.DataRequired()])
    reminder_type = RadioField('Reminder Type', choices=['Offers & Promotions', 'Unforeseen Circumstances', 'Neutral'],
                               default='neutral')
    information = TextAreaField('Enter Information', [validators.Optional()])


class SignUpForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    bio = TextAreaField('Bio (Optional)', [validators.length(max=200), validators.Optional()])
    citizen = RadioField('Citizen', choices=[('Singaporean', 'Singaporean'), ('PR', 'Permanent Resident'), ('Foreigner', 'Foreigner')], default='Yes')
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_of_birth = DateField('Date Of Birth', format='%Y-%m-%d')
    phone_no = IntegerField('Phone number', [Length(max=8), NumberRange(min=0, max=100000000, message='Please enter a valid phone number!'), validators.DataRequired()])
    password = PasswordField('New Password', [InputRequired(), validators.DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Repeat Password', [validators.DataRequired()])


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')],
                            default='F')


class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_leaving = DateField('Date Of Birth', format='%Y-%m-%d')
    tour_package = TextAreaField('Bio (Optional)', [validators.length(max=200), validators.Optional()])
    membership = RadioField('Citizen', choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes')


class transactionform(Form):
    card_name = StringField("Card Holder's name", [validators.Length(min=1, max=150), validators.DataRequired(), ]) # letters_only
    card_number = StringField('Card Number', [validators.Length(min=16, max=16), validators.DataRequired(), ]) # number_only
    expiry = StringField('Expiry Date', [validators.Length(min=4, max=4), validators.DataRequired(), ]) # number_only
    cvc = StringField('CVC/CVV', [validators.Length(min=3, max=3), validators.DataRequired(), ]) # number_only
    default_card = BooleanField("Set as default card")
    remember_card = BooleanField("Remember card")


class CustomerKeyInfoForm(Form):
    Adult = IntegerField("(12yrs and above)", [validators.NumberRange(min=1, max=3)], default=1)
    Child = IntegerField("(12yrs and below)", [validators.NumberRange(max=2)])
    Infant = IntegerField("(below 2yrs)", [validators.NumberRange(max=2)])


class PackageForm(Form):
    Departure = DateTimeField("Departure Date:", validators=[date_cannot_be_in_the_past])
    Return = DateTimeField("Return Date:", validators=[date_cannot_be_in_the_past])
    Duration = StringField("Length of Trip:", [validators.length(min=4, max=4)])
    Destination = StringField("Destination:")  # letters_only
    Airline = StringField("Chosen Airline:")  # letters_only
    Adult_price = IntegerField("Adult Price:")  # number_only
    Child_price = IntegerField("Child Price:")  # number_only
    Infant_price = IntegerField("Infant Price:")  # number_only




