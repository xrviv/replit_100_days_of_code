class Jobs:
  name = None
  salary = None
  hoursWorked = None
  
  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked
   
  def show(self):
    print("🌟Jobs Jobs Jobs!🌟")
    print()
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hoursWorked}")
    print()

class Doctor(Jobs):
  def __init__(self, name, salary, hoursWorked, experience, specialty):
    super().__init__(name, salary, hoursWorked)
    self.experience = experience
    self.specialty = specialty

  def print_details(self):
    super().show()
    print(f"Speciality: {self.speciality}")
    print(f"Years of experience: {self.years_of_experience}")

class Teacher(Jobs):
  def __init__(self, name, salary, hoursWorked, subject, position):
    super().__init__(name, salary, hoursWorked)
    self.subject = subject
    self.position = position

lawyer = Jobs("Atty. Daniel Webster", 300000, 40)

doctor = Doctor("Dr. Jones", 60000, 2920, "7 years", "Pediatric Consultant")

teacher = Teacher("Mr. Krab", 30000, 5000, "Computer Science", "Substitute Teacher")

lawyer.show()
teacher.show()
doctor.show()
