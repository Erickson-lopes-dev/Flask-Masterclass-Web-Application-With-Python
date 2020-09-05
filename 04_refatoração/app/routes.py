from datetime import timedelta

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models import User


def init_app(app):
    @app.route("/")
    def index():
        users = User.query.all() # Select * from users; 
        return render_template("users.html", users=users)

    @app.route("/user/<int:id>")
    @login_required
    def unique(id):
        user = User.query.get(id)
        return render_template("user.html", user=user)

    @app.route("/user/delete/<int:id>")
    def delete(id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        return redirect("/")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            user = User()
            user.name = request.form["name"]
            user.email = request.form["email"]
            user.password = generate_password_hash(request.form["password"])

            db.session.add(user)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            remember = request.form["remember"]

            user = User.query.filter_by(email=email).first()

            if not user:
                flash("Credênciais incorretas")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, password):
                flash("Credênciais incorretas")
                return redirect(url_for("login"))

            login_user(user, remember=remember, duration=timedelta(days=7))
            return redirect(url_for("index"))

        return render_template("login.html")


    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("index"))
