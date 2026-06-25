print("\n=== Student Report Card ===")
name = input("Enter student's name: ")
maths = float(input("Enter Maths marks    : "))
physics = float(input("Enter Physics marks  : "))
chemistry = float(input("Enter Chemistry marks: "))
total_marks = maths + physics + chemistry
percentage = (total_marks / 300) * 100
print(f"  Percentage   : {percentage:.2f}%")
