# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

height_sum = int(0)
height_count = 0

for height in student_heights:
    height_sum += height   

for total_count in student_heights:
    height_count += 1 

average = round(height_sum / height_count)

print(average)
