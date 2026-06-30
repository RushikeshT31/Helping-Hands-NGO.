from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------------
# Temporary Donation Records
# -------------------------------

donations = []

# -------------------------------
# Home Page
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# About Page
# -------------------------------

@app.route("/about")
def about():
    return render_template("about.html")


# -------------------------------
# Projects Page
# -------------------------------

@app.route("/projects")
def projects():
    return render_template("projects.html")


# -------------------------------
# Donate Page
# -------------------------------

@app.route("/donate", methods=["GET", "POST"])
def donate():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        amount = request.form["amount"]

        donations.append({
            "name": name,
            "email": email,
            "amount": amount
        })

        return render_template(
            "thankyou.html",
            name=name,
            amount=amount
        )

    return render_template(
        "donate.html",
        donations=donations
    )


# -------------------------------
# Contact Page
# -------------------------------

@app.route("/contact")
def contact():
    return render_template("contact.html")


# -------------------------------
# Admin Login
# -------------------------------

@app.route("/login")
def login():
    return render_template("login.html")


# -------------------------------
# Dashboard
# -------------------------------

@app.route("/register", methods=["POST"])
def register():

    # Get form data
    username = request.form["username"]
    email = request.form["email"]
    phone = request.form["phone"]
    city = request.form["city"]
    password = request.form["password"]

    # (Optional) Save data here

    return render_template("dashboard.html")

# -------------------------------
# Run Flask
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)