# Import necessary modules from flask
from flask import render_template, request, redirect, url_for
# Import the app and db from taskmanager
from taskmanager import app, db
# Import the Category and Task models from taskmanager.models
from taskmanager.models import Category, Task

# Define the route for the home page


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    # Render the tasks.html template
    return render_template("tasks.html", tasks=tasks)

# Define the route for the categories page


@app.route("/categories")
def categories():
    # Query the database for all categories, ordered by category name
    categories = list(Category.query.order_by(Category.category_name).all())
    # Render the categories.html template with the categories
    return render_template("categories.html", categories=categories)

# Define the route for adding a category, accepting both GET and POST requests


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # If the request method is POST
    if request.method == "POST":
        # Create a new Category object with the category name from the form
        category = Category(
            category_name=request.form.get("category_name")
        )
        # Add the new category to the session
        db.session.add(category)
        # Commit the session to save the new category
        db.session.commit()
        # Redirect to the categories page
        return redirect(url_for('categories'))
    # If the request method is not POST, render the add_category.html template
    return render_template("add_category.html")

# Define the route for editing a category, accepting both GET and POST requests


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # Get the category with the given id, or return a 404 error if it doesn't exist
    category = Category.query.get_or_404(category_id)
    # If the request method is POST
    if request.method == "POST":
        # Update the category name with the value from the form
        category.category_name = request.form.get("category_name")
        # Commit the session to save the changes
        db.session.commit()
        # Redirect to the categories page
        return redirect(url_for("categories"))
    # If the request method is not POST, render the edit_category.html template with the category
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('categories'))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    # If the request method is POST
    if request.method == "POST":
        # Create a new Task object from the form data
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        # Add the new task to the session
        db.session.add(task)
        # Commit the session to save the new task
        db.session.commit()
        # Redirect to the tasks page
        return redirect(url_for('home'))
    # If the request method is not POST, render the add_task.html template
    return render_template("add_task.html", categories=categories)
