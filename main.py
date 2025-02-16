from flask import Flask, url_for

from utils import get_boss_list_names, get_boss_info_by_name

app = Flask(__name__)

@app.route("/") 
@app.route("/home")
def index():
    bosses = get_boss_list_names()

    links_list = []
    for name in bosses:
        links_list.append(
            f'<li class="list-group-item"><a href="/boss/{name}" class="text-decoration-none">{name}</a></li>'
        )
    links_str = " ".join(links_list)

    return f"""
<!DOCTYPE html>
        <html lang="ru">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Вики по боссам Hollow Knight</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
          <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
          <div class="container">
              <div class="row mt-5">
                <h1 class="text-center mt-5 mb-5">Вики по боссам Hollow Knight</h1>
                <div class="row justify-content-center">
                  <div class="col-md-4">
                    <ul class="list-group">
                      {links_str}
                    </ul>
                  </div>
                </div>
            </div>
          </div>
        </body>
        </html>
"""

@app.route("/boss/<boss_name>")
def boss_info(boss_name):
    boss_info = get_boss_info_by_name(boss_name)

    name = boss_info[0]
    hp = boss_info[1]
    location = boss_info[2]
    loot = boss_info[3]
    game_description = boss_info[4]
    description = boss_info[5]
    attack = boss_info[6]

    return f"""
<!DOCTYPE html>
        <html lang="ru">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Информация о боссе</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
          <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
          <div class="container">
            <div class="row mt-5">
              <div class="col-md-6 offset-md-3">
                <h1 class="text-center mt-5 mb-5"><b>{name}</b></h1>
                <div class="card">
                  <div class="card-body">
                    <p class="card-text"><b>Здоровье босса:</b>  {hp}</p>
                    <p class="card-text"><b>Локация:</b>  {location}</p>
                    <p class="card-text"><b>Добыча:</b>  {loot}</p>
                    <p class="card-text"><b>Игровое описание:</b>  {game_description}</p>
                    <p class="card-text"><b>Описание:</b>  {description}</p>
                    <p class="card-text"><b>Атаки:</b>  {attack}</p>
                    <a href="/" class="btn btn-light">Назад к списку</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </body>
        </html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
