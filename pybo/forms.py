from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('답변 내용', validators=[DataRequired('답변 내용은 필수입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    #Length:이름 최소 3글자, 최대 25글자
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])

    # EqualTo : password1 == password2 동일한지 check용도
    # <input type='password'/>
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    #<input type='email'/>
    #pip install email_validator
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

