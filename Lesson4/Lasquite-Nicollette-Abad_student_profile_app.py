# Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        # Store the three values in instance attributes.
        self.name = name
        self.course = course
        self.year_level = year_level

    def get_profile(self):
        # Return the student's information using HTML-like tags.
        return (
            f"<h2>{self.name}</h2>\n"
            f"<p>Course: {self.course}</p>\n"
            f"<p>Year Level: {self.year_level}</p>"
        )


# Child class for an IT student.
class ITStudent(Student):
    # Class attribute shared by all ITStudent objects.
    skill = "Python"

    def get_skill(self):
        # Return the programming skill using a <p> tag.
        return f"<p>Programming Skill: {self.skill}</p>"


# Application class with Flask-inspired routes.
class StudentApp:
    def __init__(self, title, student):
        # Store the app title and the student object.
        self.title = title
        self.student = student

    def route(self, path):
        # Return the correct page content for the given path.
        if path == "/":
            return f"<h1>{self.title}</h1>"
        elif path == "/profile":
            # Uses the inherited get_profile() and the child's own get_skill().
            return self.student.get_profile() + "\n" + self.student.get_skill()
        else:
            return "<h1>404 - Page Not Found</h1>"

    def run(self):
        # Print the app title, then test each route.
        print(f"Running: {self.title}")
        for path in ["/", "/profile", "/unknown"]:
            print()
            print(f"GET {path}")
            print(self.route(path))


# Create the student and application objects.
student = ITStudent("Nicollette Lasquite", "BS Information Technology", 4)
app = StudentApp("PSU Student Profile App", student)

# Start the application.
app.run()
