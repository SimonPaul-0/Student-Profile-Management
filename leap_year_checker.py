class StudentProfile:
    def __init__(self, first_name, last_name, age, gender, grade, address, contact):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.grade = grade
        self.address = address
        self.contact = contact

    def display_profile(self):
        print("\nStudent Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Grade: {self.grade}")
        print(f"Address: {self.address}")
        print(f"Contact: {self.contact}")

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Grade updated to: {self.grade}")

    def age_category(self):
        if self.age <= 12:
            return "Child"
        elif 13 <= self.age <= 17:
            return "Teenager"
        else:
            return "Adult"

def main():
    print("Enter the details for the student:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    grade = input("Grade: ")
    address = input("Address: ")
    contact = input("Contact: ")

    student = StudentProfile(first_name, last_name, age, gender, grade, address, contact)

    # Display the student profile
    student.display_profile()

    # Update the student's grade
    new_grade = input("\nEnter the new grade: ")
    student.update_grade(new_grade)

    # Display the updated profile
    student.display_profile()

    # Determine the age category
    category = student.age_category()
    print(f"\nAge Category: {category}")

if __name__ == "__main__":
    main()
