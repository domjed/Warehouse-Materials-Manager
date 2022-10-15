from constants.constants import CONSTANTS
from datetime import datetime, date, timedelta
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from static.python.calculate_summary import calculate_summary

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///materials.db"
db = SQLAlchemy(app)


class MaterialItem(db.Model):
    """Class representing materials database"""

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    dateAdded = db.Column(db.Date, nullable=False, default=datetime.now().date())
    timeAdded = db.Column(db.Time, nullable=False, default=datetime.now().time())

    def __repr__(self):
        return "Material item " + str(self.id)


# db.create_all() shall be executed only once, to create database
db.create_all()


@app.route("/")
def show_main_page():
    """Render main menu template"""
    return render_template("mainMenu.html")


@app.route("/materials", methods=["GET", "POST"])
def show_materials():
    """Present current materials stored in database and enable adding new"""

    if request.method == "POST":
        search_criteria = {}
        search_criteria["sortingOrder"] = request.form["sortingOrder"]
        search_criteria["filterBalance"] = request.form["filterBalance"]
        search_criteria["filterHistory"] = request.form["filterHistory"]

        search_criterion = getattr(
            MaterialItem, search_criteria["sortingOrder"].split(" ")[0]
        )

        if search_criteria["filterHistory"] == "futureTrades":
            first_day_to_scope = date.today()
            last_day_to_scope = date.max
        elif search_criteria["filterHistory"] == "fromVeryBeginning":
            first_day_to_scope = date.min
            last_day_to_scope = date.max
        else:
            timespan = timedelta(int(search_criteria["filterHistory"]))
            today = date.today()
            first_day_to_scope = today - timespan
            last_day_to_scope = today

        if search_criteria["filterBalance"] == "soldMaterials":
            balance_filter = MaterialItem.weight < 0
        elif search_criteria["filterBalance"] == "purchasedMaterials":
            balance_filter = MaterialItem.weight >= 0
        else:
            balance_filter = True

        materials = (
            MaterialItem.query.order_by(search_criterion)
            .filter(
                MaterialItem.delivery_date >= first_day_to_scope,
                MaterialItem.delivery_date <= last_day_to_scope,
                balance_filter,
            )
            .all()
        )
        direction = search_criteria["sortingOrder"].split(" ")[-1]

        if direction == "desc":
            materials.reverse()

        summary = {}
        summary = calculate_summary(materials)

        return render_template(
            "materials.html", materials=materials, summary=summary, constants=CONSTANTS
        )

    if "search_criteria" not in locals():
        materials = MaterialItem.query.order_by(MaterialItem.id).all()
    else:
        materials = MaterialItem.query.order_by(MaterialItem.title).all()

    summary = {}
    summary = calculate_summary(materials)

    return render_template(
        "materials.html", materials=materials, summary=summary, constants=CONSTANTS
    )


@app.route("/materials/delete/<int:id>")
def delete(id):
    """Remove material from database"""

    material = MaterialItem.query.get_or_404(id)
    db.session.delete(material)
    db.session.commit()

    return redirect("/materials")


@app.route("/materials/view/<int:id>")
def view(id):
    """View details of material database item"""

    material = MaterialItem.query.get_or_404(id)

    return render_template("view.html", material=material)


@app.route("/materials/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    """Edit existing material from database"""

    material = MaterialItem.query.get_or_404(id)
    if request.method == "POST":
        material.title = request.form["titleEdit"]
        material.weight = request.form["weightEdit"]
        material.category = request.form["categoryEdit"]
        material.description = request.form["descriptionEdit"]
        material.delivery_date = datetime.strptime(
            request.form["deliveryDateEdit"], "%Y-%m-%d"
        )
        material.dateAdded = datetime.now().date()
        material.timeAdded = datetime.now().time()
        db.session.commit()
        return redirect("/materials")

    return render_template("edit.html", material=material, constants=CONSTANTS)


@app.route("/materials/new", methods=["GET", "POST"])
def new_material():
    """Add new material to database"""

    if request.method == "POST":
        material_title = request.form["title"]
        material_weight = request.form["weight"]
        material_category = request.form["category"]
        material_description = request.form["description"]
        time = datetime.strptime(request.form["delivery_date"], "%Y-%m-%d")
        delivery_date = date(time.year, time.month, time.day)
        new_item = MaterialItem(
            title=material_title,
            weight=material_weight,
            category=material_category,
            description=material_description,
            delivery_date=delivery_date,
            dateAdded=datetime.now().date(),
            timeAdded=datetime.now().time(),
        )
        db.session.add(new_item)
        db.session.commit()

        return redirect("/materials")

    return render_template("addNew.html", constants=CONSTANTS)


if __name__ == "__main__":
    app.run(debug=True)
