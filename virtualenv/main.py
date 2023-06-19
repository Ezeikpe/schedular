from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a list to store the to-do items
todo_items = []

# Define a route to handle the home page
@app.route("/")
def home():
    return render_template("index.html", todo_items=todo_items)

# Define a route to handle adding a new item
@app.route("/add", methods=["POST"])
def add():
    # Get the text from the form
    item_text = request.form["item_text"]

    # Add the new item to the list
    todo_items.append({"text": item_text, "completed": False})

    # Redirect back to the home page
    return redirect(url_for("home"))

# Define a route to handle removing completed items
@app.route("/remove", methods=["POST"])
def remove():
    # Get the indexes of the completed items
    completed_indexes = [int(index) for index in request.form.getlist("item_completed")]

    # Remove the completed items from the list
    global todo_items
    todo_items = [item for index, item in enumerate(todo_items) if index not in completed_indexes]

    # Redirect back to the home page
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
