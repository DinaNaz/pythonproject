m = int(input())
all_present = set()

for i in range(m):
    k = int(input())
    current_lesson = set()
    for _ in range(k):
        current_lesson.add(input().strip())
    
    if i == 0:
        all_present = current_lesson
    else:
        all_present &= current_lesson

for student in all_present:
    print(student)