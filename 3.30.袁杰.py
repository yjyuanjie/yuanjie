# 定义学生数据列表
student_list = [
    {'name': '张三', 'age': 23, 'score': 90, 'phone': 12345, 'gender': '男'},
    {'name': '李四', 'age': 34, 'score': 45, 'phone': 45672, 'gender': '男'},
    {'name': '王五', 'age': 45, 'score': 30, 'phone': 12785, 'gender': '不明'},
    {'name': '老赵', 'age': 89, 'score': 80, 'phone': 90438, 'gender': '女'},
    {'name': '老蒋', 'age': 12, 'score': 75, 'phone': 98473, 'gender': '男'},
    {'name': '老朱', 'age': 16, 'score': 64, 'phone': 23532, 'gender': '不明'}
]

# 1. 统计不及格学生的个数
failing_students_count = sum(1 for student in student_list if student['score'] < 60)
print(f"不及格学生的个数: {failing_students_count}")

# 2. 打印不及格学生的名字和对应的成绩
failing_students = [(student['name'], student['score']) for student in student_list if student['score'] < 60]
print("不及格学生的名字和对应的成绩:")
for name, score in failing_students:
    print(f"{name}: {score}")

# 3. 统计未成年学生的个数
minor_students_count = sum(1 for student in student_list if student['age'] < 18)
print(f"未成年学生的个数: {minor_students_count}")

# 4. 打印手机尾号是8的学生的名字
students_with_phone_ending_8 = [student['name'] for student in student_list if str(student['phone']).endswith('8')]
print("手机尾号是8的学生的名字:")
for name in students_with_phone_ending_8:
    print(name)

# 5. 删除性别不明的所有学生
student_list = [student for student in student_list if student['gender'] != '不明']
print("删除性别不明的学生后的学生列表:")
print(student_list)

# 6. 打印最高分和对应的学生的名字
if student_list:
    top_student = max(student_list, key=lambda x: x['score'])
    print(f"最高分: {top_student['score']}, 学生名字: {top_student['name']}")
else:
    print("没有学生信息")