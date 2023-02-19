from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/")
def ma():
    return '''<h1></h1>'''
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участи в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" placeholder="Введите фамилию">
                                    <input class="form-control" placeholder="Введите имя">
                                    <div>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </div>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                        </select>
                                     </div>
                                    <div class="form-group form-check">
                                        <p>Какие у вас есть професии?</p>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Инженер-исследователь</label></h6>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Инженер-строитель </label></h6>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Пилот </label></h6>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Метеоролог </label></h6>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Инженер по жизнеобеспечению </label></h6>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Инженер по радиационной защите </label></h6>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Врач</label></h6>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <h6><label for="classSelect">Экзобиолог </label></h6>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run()
