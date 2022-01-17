name = input("이름을 입력해주세요: ")
korean = input("국어 성적을 입력해주세요: ")
english = input("영어 성적을 입력해주세요: ")
math = input("수학 성적을 입력해주세요: ")

total = int(korean) + int(english) + int(math)
avg = total / 3

print(name, "님의 총점 =", total, "평균 =", avg, "입니다.")
