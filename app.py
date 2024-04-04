from flask import Flask, redirect, url_for, render_template, flash
from flask import session, request
from datetime import timedelta
from utilities.calc_grades import calc_grades
from utilities.reset_password import reset_password
from utilities.env import SECRET_KEY, DB_URI, MAX
from models.database import db
from models.form import LoginResetForm
from controllers.users import get_user, set_password, verify_password
from controllers.grades import get_grades, get_rank, set_grades
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.permanent_session_lifetime = timedelta(minutes=15)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginResetForm()
    if "seq" in session:
        return redirect(url_for("grades"))
    elif form.validate_on_submit():
        user = get_user(id=request.form["id"])
        if not user:
            flash("Incorrect id")
        elif user.password == "0":
            check = calc_grades(user, request.form["password"])
            if type(check) is not dict:
                flash(check)
            else:
                set_password(user, request.form["password"])
                set_grades(user, check)
                session["seq"] = user.seq
                return redirect(url_for("grades"))
        else:
            if verify_password(user, request.form["password"]):
                session["seq"] = user.seq
                return redirect(url_for("grades"))
            else:
                flash("Incorrect password")
        return redirect(url_for("login"))
    else:
        return render_template("login.html", form=form)


@app.route("/reset/", methods=["GET", "POST"])
def reset():
    form = LoginResetForm()
    if "seq" in session:
        return redirect(url_for("grades"))
    elif form.validate_on_submit():
        user = get_user(id=request.form["id"])
        if not user:
            flash("Incorrect id")
        elif user.password == "0":
            flash("Please login first")
        else:
            check = reset_password(user.id, request.form["password"])
            if check is not True:
                flash(check)
            else:
                set_password(user, request.form["password"])
                flash("Password has been reset")
        return redirect(url_for("reset"))
    else:
        return render_template("reset.html", form=form)


@app.route("/grades/")
def grades():
    if "seq" in session:
        user = get_user(seq=session["seq"])
        name = user.name
        grades = get_grades(user)
        rank = get_rank(user)
        max_total = sum(v for k, v in MAX["TOTAL"].items() if grades[k] > 0)
        return render_template("grades.html", name=name, grades=grades,
                               max=MAX, max_total=max_total, rank=rank)
    else:
        return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    if "seq" in session:
        session.clear()
    return redirect(url_for("login"))
