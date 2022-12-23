import sqlite3,os
from flask import Flask,render_template, request,redirect, current_app,g 
from db import db as DB


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.path.join(app.instance_path, "APP.sqlite"),
)


with app.app_context():
    DB.init_db()
DB.init_app(app)

@app.route("/",methods = ['POST', 'GET'])
def root():
    return "Tá tudo tolo"

@app.route("/register",methods = ['POST', 'GET'])
def register():
    if request.method == 'POST' :
        db=DB.get_db()
        print(request.form)
        db.execute("INSERT INTO inquerito (nprocesso, nome, ano, turma, interesse, classificacao, opiniao) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (request.form["nprocesso"],request.form["nome"],request.form["ano"],request.form["turma"],request.form["interesse"],request.form["fopiniao"])
                )
        return redirect("/")
    elif request.method == 'GET':
        return render_template("register.html")

if __name__ == "__main__":

    app.run()
    print("hi")


