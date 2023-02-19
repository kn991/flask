from flask import Flask


app = Flask(__name__)

@app.route("/")
def ma():
    return '''<h1></h1>'''
@app.route('/promotion_image')
def promotion_image():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <link rel="stylesheet" href="static/css/style.css">
    <title>Колонизация</title>
</head>
<body>
    <h1 class="red_text">Жди нас, Марс!</h1>
    <img src="static/img/mars.jpeg">
    <h4 class="first">Человечество вырастает из детства.</h4>
    <h4 class="second">Человечеству мала одна планета.</h4>
    <h4 class="third">Мы сделаем обитаемыми безжизненные пока планеты.</h4>
    <h4 class="fourth">И начнем с Марса!</h4>
    <h4 class="fifth">Присоединяйся!</h4>
</body>
</html>'''


if __name__ == '__main__':
    app.run()
