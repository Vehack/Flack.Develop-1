from flask import Flask, render_template, request
from googletrans import *

app = Flask(__name__)
@app.route('/', methods=['post', 'get'])
def login():
    attention1 = 'Введите логин и пароль. '
    message1 = '...'
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')

        if username == '' or password == '':
            attention1 = 'Не получилось!'
            message1 = 'Неверный логин или пароль. Пожалуйста, попробуйте снова.'
        else:
            attention1 = 'Отлично!'
            message1 = 'Ваш логин - '+ username + '. Ваш пароль - ' + password + '. Вы готовы продолжить?'

    return render_template('index.html', message1 = message1, attention1 = attention1, title='Франкенштейн')



@app.route('/translator', methods=['POST', 'GET'])
def translator():
    code_dict = {'chinese (traditional)': 'zh-tw','Russian': 'ru', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de'}

    translator = Translator(service_urls=['translate.googleapis.com'])

    if request.method == 'POST':
        text = request.form.get('text')
        language = request.form.get('language')
        if language in code_dict.keys():
            lang_edited = code_dict[language]
            translation = translator.translate(text, dest=lang_edited)
            translated_message = translation.text
            return render_template('translator.html', my_string=translated_message)
        else:
            return render_template('translator.html',title='Франкенштейн-Переводчик')
    return render_template('translator.html',title='Франкенштейн-Переводчик')



if __name__ == '__main__':
    app.run(debug=True)
#debug=True