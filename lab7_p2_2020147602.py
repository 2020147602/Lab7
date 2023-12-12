from string import ascii_uppercase

#파일 열기
with open('./input_7_2.txt', 'r') as file:
    text = file.read()

# 파일들 대문자로 변환
text = text.upper()
upper_alphabet = list(ascii_uppercase)

# 딕셔너리 컴프리헨션, 0으로 초기화
cnt_dict = {i: 0 for i in upper_alphabet}

# 알파벳 찾으면 value 값 증가
for line in text:
    if line in cnt_dict:
        cnt_dict[line] += 1

# 딕셔너리 아이템을 key 값 기준으로 정렬하기
sorted_items = sorted(cnt_dict.items(), key=lambda x: x[1], reverse=True)

# 빈배열 초기화
sorted_alpah=[]

# cnt>0 이상인 것만 sorted_alpha에 담기
for char, count in sorted_items:
    if count > 0:
        sorted_alpah.append(char)
#출력
print(sorted_alpah)

