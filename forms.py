from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('User', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Criar conta')

class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit_login = SubmitField('Login')

class AeroportoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Adicionar aeroporto')

class AssentoForm(FlaskForm):
    assento_id = StringField('assento_id', validators=[DataRequired(), Length(min=3, max=5)])
    id_aviao = IntegerField('id_aviao', validaotrs=[DataRequired()])
    ocupado = BooleanField('ocupado', validators=[DataRequired()])
    submit = SubmitField('Adicionar assento')

class AviaoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(min=1, max=50)])
    qtdAssentos = IntegerField('quantidade de assentos', validators=[DataRequired()])
    submit = SubmitField('Adicionar avião')

class PassageiroForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(min=3, max=50)])
    id_usuario = IntegerField('id_aviao', validators=[DataRequired()])
    submit = SubmitField('Adicionar passageiro')

class TicketForm(FlaskForm):
    id_assento = IntegerField('id_assento', validators=[DataRequired()])
    id_voo = IntegerField('id_voo', validators=[DataRequired()])
    id_passageiro = IntegerField('id_passageiro', validators=[DataRequired()])
    submit = SubmitField('Adicionar ticket')

class UsuarioForm(FlaskForm):
    username = StringField('user', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('senha', validators=[DataRequired()])
    submit = SubmitField('Adicionar usuario')

class VooForm(FlaskForm):
    id_aeroporto_saida = IntegerField('id_aeroporto_saida', validators=[DataRequired()])
    id_aeroporto_chegada = IntegerField('id_aeroporto_chegada', validators=[DataRequired()])
    horario = DateTimeField('horario', validators=[DataRequired()])
    id_aviao = IntegerField('id_aviao', validators=[DataRequired()])
    submit = SubmitField('Adicionar voo')
