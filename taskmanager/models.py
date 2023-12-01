# Import the db object from the taskmanager package
from taskmanager import db

# Define the Category model
class Category(db.Model):
    # schema for Category model
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    category_name = db.Column(
        db.String(25), unique=True, nullable=False)  # Category name column
    # Define a relationship between Category and Task models
    tasks = db.relationship(
        "Task",  # The other model in the relationship
        backref="category",  # Reference to the Category model from the Task model
        cascade="all, delete",  # Delete all related tasks when a category is deleted
        lazy=True  # Load the data as necessary, not upfront
    )

    # String representation of the Category model
    def __repr__(self):
        return self.category_name

# Define the Task model
class Task(db.Model):
    # schema for Task model
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    task_name = db.Column(db.String(50), unique=True,
                          nullable=False)  # Task name column
    task_description = db.Column(
        db.Text, nullable=False)  # Task description column
    is_urgent = db.Column(db.Boolean, default=False,
                          nullable=False)  # Urgency flag column
    due_date = db.Column(db.Date, nullable=False)  # Due date column
    # Foreign key column linking to the Category model
    category_id = db.Column(
        db.Integer,
        # Reference to the Category model
        db.ForeignKey("category.id", ondelete="CASCADE"),
        nullable=False
    )

    # String representation of the Task model
    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
