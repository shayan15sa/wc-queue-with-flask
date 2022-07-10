import base64
import io
from flask import Flask, render_template, request
import qrcode
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
engine = create_engine('sqlite:///user.sqlite3')

db = SQLAlchemy(app)
class User(db.Model):

    id = db.Column('user_id', db.Integer, primary_key = True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname

@app.route("/")
def sus():
    return render_template("index.html")

@app.route("/reg")
def reg():    
    return render_template("reg.html")


@app.route("/reg/check" , methods=["GET"])
def check():
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    if User.query.filter_by(fname = fn).all() != [] and User.query.filter_by(lname = ln).all() !=[]:
        return "2"
    else:
        return "1"

@app.route("/qrcode", methods=['GET'])
def qr():
    fnam = request.args.get("fname")
    lnam = request.args.get("lname")
    t = False
    if fnam != "" and lnam != "":
        if User.query.filter_by(fname = fnam).all() != [] and User.query.filter_by(lname = lnam).all() ==[]:    
            t = True
    if  t:
        db.session.add(User(fnam,lnam))
        db.session.commit()
    else:
        return "GOTCHA"
    id = User.query.filter_by(fname= fnam,lname = lnam).all()[-1].id

    qri = qrcode.make(fnam+"^"+lnam)
    
    i = io.BytesIO()
    qri.save(i,format=qri.format)
    
    #return str(i.getvalue())
    #return type(i)
    i.seek(0)
    img = base64.b64encode(i.getvalue()).decode()
    #return '<img src="data:image/png;base64,{}">'.format(img)
    return  render_template("qr.html",i = "data:image/png;base64,{}".format(img),id = id)    
        
@app.route("/all")
def show_all():
    st = ""
    for i in User.query.all():
        st += i.fname + " "
        st += i.lname + "<br>"
        print(type(i))
    return st

@app.route("/qrcheck")
def qrcheck():
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    firstrow = User.query.first()
    if firstrow.fname == fn and firstrow.lname == ln:
        User.query.filter_by(id=firstrow.id).delete()
        db.session.commit()
        return "1"
    else:
        return "2"