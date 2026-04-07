class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.students = []


    def introduce(self):
        print(f"Hello, I am {self.name}. I teach {self.subject} and have {self.experience} years of experience.")


    def add_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} has been added to {self.name}'s class.")


    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} has been removed from the class.")
        else:
            print(f"{student_name} is not in this class.")


    def list_students(self):
        if self.students:
            print(f"Students in {self.name}'s class:")
            for s in self.students:
                print(f" - {s}")
        else:
            print("No students in the class yet.")


    def give_marks(self, student_name, marks):
        print(f"{self.name} gave {marks} marks to {student_name} in {self.subject}.")



teacher1 = Teacher("Mr. Rahman", "Mathematics", 10)
teacher1.introduce()
teacher1.add_student("Tasin")
teacher1.add_student("Aisha")
teacher1.list_students()
teacher1.give_marks("Tasin", 95)
teacher1.remove_student("Aisha")
teacher1.list_students()


class Teacher:
    def __init__(self, name, department, base_salary):
        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.subjects = []
        self.performance_scores = []


    def add_subject(self, subject_name):
        self.subjects.append(subject_name)
        print(f"{self.name} is now teaching {subject_name}.")


    def show_subjects(self):
        if self.subjects:
            print(f"{self.name} teaches: {', '.join(self.subjects)}")
        else:
            print(f"{self.name} is not assigned to any subjects yet.")


    def add_performance_score(self, score):
        if 0 <= score <= 100:
            self.performance_scores.append(score)
            print(f"Added performance score: {score}")
        else:
            print("Score must be between 0 and 100.")


    def calculate_performance(self):
        if self.performance_scores:
            avg = sum(self.performance_scores) / len(self.performance_scores)
            print(f"Average performance score for {self.name}: {avg:.2f}")
            return avg
        else:
            print("No performance data available.")
            return 0


    def calculate_bonus(self):
        avg = self.calculate_performance()
        if avg >= 90:
            bonus = self.base_salary * 0.25
        elif avg >= 75:
            bonus = self.base_salary * 0.15
        elif avg >= 60:
            bonus = self.base_salary * 0.05
        else:
            bonus = 0
        print(f"{self.name}'s bonus: ${bonus:.2f}")
        return bonus


    def check_promotion(self):
        avg = self.calculate_performance()
        if avg >= 85:
            print(f"{self.name} is eligible for a promotion! 🎉")
        else:
            print(f"{self.name} is not eligible for promotion yet.")


# Example usage
teacher = Teacher("Ms. Rima", "Computer Science", 50000)

teacher.add_subject("Python Programming")
teacher.add_subject("Data Structures")
teacher.show_subjects()

teacher.add_performance_score(85)
teacher.add_performance_score(90)
teacher.add_performance_score(95)

teacher.calculate_performance()
teacher.calculate_bonus()
teacher.check_promotion()







