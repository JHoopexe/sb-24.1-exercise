
from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from form import AddPet, EditPet

app = Flask(__name__)
app.config['SECRET_KEY'] = "bunnyrabbit"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route("/")
def homepage():
    pet = Pet.query.all()
    return render_template("homepage.html", pet=pet)

@app.route("/add")
def add_pet():
    form = AddPet()
    return render_template("add.html", form=form)

@app.route("/add", methods=["POST"])
def add_pet_post():
    form = AddPet()
    if form.validate_on_submit():
        name = request.form["name"]
        species = request.form["species"]
        image = request.form["image"]
        age = request.form["age"]
        notes = request.form["notes"]

        if age == '':
            age = None

        new_pet = Pet(name=name, species=species, photo_url=image, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    else:
        return redirect("add")

@app.route("/<int:pet_id>")
def display(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPet()
    return render_template("display.html", pet=pet, form=form)


@app.route("/<int:pet_id>", methods=["POST"])
def display_post(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPet()
    if form.validate_on_submit():
        pet.photo_url = request.form["image"]
        pet.notes = request.form["notes"]
        available = request.form["available"]
        
        if available == 'true':
            pet.available = True
        else:
            pet.available = False

        db.session.add(pet)
        db.session.commit()
        
        return redirect("/")
    else:
        return redirect(f"/{pet.id}")
