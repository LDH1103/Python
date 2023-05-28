sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

# 여러줄
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 문자열 자르기(slicing)
jumin = '990120-1234567'

print('성별 : ' + jumin[7])
print('연 : ' + jumin[0:2]) # 0 부터 2 직전까지
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])
print('생년월일 : ' + jumin[:6]) # 처음부터 6 직전까지
print('생년월일 : ' + jumin[7:]) # 7번째부터 끝까지
print('생년월일 : ' + jumin[-7:]) # 뒤7자리 (뒤에서부터)

# 문자열 처리 함수
python = 'Python Is Amazing'
print(python.lower()) # 모두 소문자
print(python.upper()) # 모두 대문자
print(python[0].isupper()) # 첫번째 문자가 대문자면 true, 아니라면 false
print(len(python)) # 문자열의 길이
print(python.replace('Python', 'PHP')) # 문자열 바꾸기

index = python.index('n') # 'n'이 몇번째 위치에 있는지
print(index)
index = python.index('n' , index + 1) # 두번째 'n'이 몇번째 위치에 있는지(첫번째 'n'의 위치 +1 부터 찾음)
print(index)

print(python.find('n')) 
print(python.find('java')) # 값이 없다면 -1을 반환, index는 값이 없다면 오류

print(python.count('n')) # 문자열이 포함된 갯수

# 문자열 포맷
print('a' + 'b')
print('a', 'b')

print('나는 %d살입니다.' % 20) # %d(정수) 위치에 %뒤의 값을 넣어줌
print('나는 %s을 좋아해요.' % '파이썬') # %s(문자열) 위치에 %뒤의 값을 넣어줌
print('Apple은 %c로 시작해요.' % 'A') # %c(한글자) 위치에 %뒤의 값을 넣어줌
print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))

print('나는 {}살입니다'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간')) # 1번째에 있는 '빨간'이 앞에, 0번째에 있는 '파란'이 뒤에 들어감

print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color = '빨간'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(color = '빨간', age = 20))

age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')

# 이스케이프 문자
# \n :  줄바꿈
print('백문이 불여일견 \n백견이 불여일타')

# 저는 '나도코딩'입니다.
print('저는 \'나도코딩\'입니다.')

# \\ : 문장 내에서 \
print("D:\\workspace\\")

# \r : 커서를 맨앞으로 이동
print('Red Apple\rPine')

# \b : 백스페이스 (한글자 삭제)
print('Red\bApple')

# \t : 탭
print('Red\tApple')

# 실습 ------------------------------------------------------------
# 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성
# ex) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
# ex) 생성된 비밀번호 : nav51!

url = 'http://naver.com'
period = url.index('.')
site = url[7:period]
password = site[:3] + str(len(site)) + str(site.count('e')) + '!'
print(password)