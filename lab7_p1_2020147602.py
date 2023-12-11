import re

# 파일읽기
with open("./input_7_1.txt", "r") as file:
    codes = file.read()

#re 형식으로 함수이름 찾기
function_decl = set(re.findall(r"def\s+(\w+)\s*\(", codes))

# 딕셔너리 선언 함수 불러와진 라인 찾기
decl_lines = {}
#함수 불러와진 라인 리스트
call_lines = []
#함수선언된 딕셔너리 생성
def_lines={}

#함수이름 하나씩 돌면서, 함수선언된 것과 함수가 사용된 곳을 나누어서 각 딕셔너리,리스트에 저장
for def_name in function_decl:
    for code_num,code in enumerate(codes.split("\n"),1):
        #함수 사용된 곳
        if (f"def {def_name}" not in code and f'{def_name}(' in code):
            call_lines.append(code_num)
        #함수 선언된 곳
        if (f"def {def_name}" in code):
            def_lines[def_name]=code_num
    decl_lines[def_name]=call_lines
    #초기화
    call_lines=[]

#키 값을 알파벳 순으로 정렬
sorted_key = sorted(decl_lines.keys())

#결과 출력
for key in sorted_key:
    print(f"{key}: def in {def_lines[key]}, calls in {decl_lines[key]}")

