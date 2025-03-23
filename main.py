from flask import Flask, url_for, render_template, redirect, request, session
from utils import get_boss_list_names, get_boss_info_by_name, add_boss
from models.users import UserManager
from utils import get_user_from_session


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
    add_link = f'<li class="list-group-item"><a href="/add" class="text-decoration-none">Добавить босса</a></li>'
    links_str = " ".join(links_list) + add_link
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

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
      return render_template('add.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        hp = request.form.get('hp')
        location = request.form.get('location')
        loot = request.form.get('loot')
        game_description = request.form.get('game_description')
        description = request.form.get('description')
        attack = request.form.get('attack')
        add_boss([name, 
                hp,
                location,
                loot,
                game_description,
                description,
                attack])
        return render_template('add2.html')
@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username, password = request.form.get("username"), request.form.get("password")
        remember_me = request.form.get("remember_me")
        user = UserManager().get_user_by_username(username)
        if user:
            if user.check_password(password):
                session["user"] = user.to_dict()

                if remember_me:
                    session.permanent = True

                return redirect("/")

            return render_template("login.html", error="Неправильный логин или пароль.")

        return render_template("login.html", error="Пользователь не найден.")


@app.route("/registration", methods=["GET", "POST"])
def register_page():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            return render_template("register.html", error="Пароли не совпадают.")

        registration = UserManager().create_user(username, password)
        if registration:
            return redirect("/login")

        return render_template("register.html", error="Пользователь уже существует.")
    
@app.route("/logout")
def logout_page():
    session.pop("user")
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
