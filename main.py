from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Student:
    def __init__(self, name, age, marks):
        self.name = name[cite: 4]
        self.age = age[cite: 5]
        self.marks = marks[cite: 6]

    def save(self):
        """Save this student to students.txt [cite: 8-9]"""
        with open("students.txt", "a") as file:
            # Saving with clean comma separation [cite: 10]
            file.write(f"{self.name},{self.age},{self.marks}\n")


# --- WEB ROUTES ---

@app.route('/')
def index():
    """Reads the file and shows all students in a web table [cite: 12-16]"""
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                # Splitting logic from your original code [cite: 18]
                name, age, marks = line.strip().split(",")
                students.append({'name': name, 'age': age, 'marks': marks})
    except (FileNotFoundError, ValueError):
        pass
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Handles the 'Add Student' form [cite: 46, 54]"""
    if request.method == 'POST':
        # Replaces terminal input() with web form data [cite: 55-60]
        name = request.form['name']
        age = request.form['age']
        marks = request.form['marks']

        # Creating and saving the student object [cite: 63-64]
        new_student = Student(name, age, marks)
        new_student.save()
        return redirect('/')
    return render_template('add.html')


@app.route('/search')
def search_student():
    """Search logic for the browser [cite: 23, 49]"""
    query = request.args.get('query', '').lower()
    results = []
    if query:
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    name, age, marks = line.strip().split(",")
                    # Matching the name just like your original search [cite: 30-32]
                    if query in name.lower():
                        results.append({'name': name, 'age': age, 'marks': marks})
        except FileNotFoundError:
            pass
    return render_template('search.html', results=results, query=query)


if __name__ == '__main__':
    app.run(debug=True)