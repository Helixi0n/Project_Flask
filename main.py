from flask import Flask, url_for, render_template
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
    print(links_str)
    return render_template('index.html', links_str=links_str)

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

    return render_template('boss.html', name=name, hp=hp, location=location, loot=loot, game_description=game_description, description=description, attack=attack)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
