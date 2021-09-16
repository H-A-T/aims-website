from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def about_page():
    return render_template("about.html")

@app.route("/events")
def events_page():
    return render_template("events.html")

@app.route("/people")
def people_page():
    return render_template("people.html")

@app.route("/publications")
def publications_page():
    return render_template("publications.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/projects")
def projects_page():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)