from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from forms import AddPetForm
from pet_finder import find_random_pet
from secrets import API_KEY, TOKEN


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptionagency'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app) 

connect_db(app)
db.create_all()

@app.route('/')
def index():
    pets = Pet.query.all()
    pet_finder = find_random_pet()

    return render_template('home.html', pets=pets, pet_finder=pet_finder)


@app.route('/add', methods=['POST','GET'])
def add_pet_form():
    '''Create a form for adding pets.'''
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=['GET','POST'])
def edit_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        #can replace filterby with get or 404
        pet = Pet.query.filter_by(id=pet_id).update(dict(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available))
        db.session.commit()
        return redirect(f'/{pet_id}')

    else:
        return render_template('pet_info.html', pet=pet, form=form)


