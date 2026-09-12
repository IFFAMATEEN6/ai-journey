# Variables & data types
student_name = "Iffa"
student_age = 22
gpa = 3.7

# Dictionary
profile = {
    "name": student_name,
    "age": student_age,
    "gpa": gpa,
    "skills": []
}

# List
skills = ["Python", "Git", "GitHub", "Virtual Env"]
profile["skills"] = skills

# Loop through skills, print each with an if-check
for skill in skills:
    if skill == "Python":
        print(f"{skill} - core language!")
    else:
        print(f"{skill} - supporting tool")

# Tuple - fixed info
birth_year_tuple = (2004,)

# Set - unique interests
interests = {"AI", "ML", "AI", "Backend"}
print("Unique interests:", interests)

print(f"\nFull profile: {profile}")