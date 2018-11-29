from wtforms import Form, StringField, SelectField

class BookSearchForm(Form):
    select = SelectField('Search for music:')
    search = StringField('')