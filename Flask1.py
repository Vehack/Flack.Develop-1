from flask import Flask, render_template, request
from googletrans import *

app = Flask(__name__)
@app.route('/', methods=['post', 'get'])
def login():
    username = ''
    password = ''
    attention = 'Введите логин и пароль. '
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
    message = 'Information will be here'
    if username == '' or password == '':
        attention = 'Не получилось!'
        message = 'Неверный логин или пароль. Пожалуйста, попробуйте снова.'
    else:
        attention = 'Отлично!'
        message = 'Ваш логин - '+ username + '. Ваш пароль - ' + password + '. Вы готовы продолжить?'

    return render_template('index.html', message = message, attention = attention, title='Франкейштейн')



@app.route('/translator', methods=['POST', 'GET'])
def translater():
    code_dict = {'Russian': 'ru', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de'}

    translator = Translator()

    if request.method == 'POST':
        text = request.form.get('text')  # запрос к данным формы
        language = request.form.get('language')
        if language in code_dict.keys():
            lang_edited = code_dict[language]
            translation = translator.translate(text, dest=lang_edited)
            translated_message = translation.text
            return render_template('translator.html', my_string=translated_message,
                                   lang='Your native language is ' + translation.src)
        else:
            return render_template('translator.html')
    return render_template('translator.html')



if __name__ == '__main__':
    app.run(port=3000, debug=True)