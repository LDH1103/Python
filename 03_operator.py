# 연산자
print( 2 ** 3 ) # 2 ^ 3
print( 2 // 1 ) # 2를 1로 나누었을때의 몫
print( 2 == 1 ) # ===이 없음
print( 2 == "2" ) # 완전비교 
print( 2 == int("2") ) # 완전비교 
print( 1 != 3 )
print( not( 1 != 3 ) ) # False

print( ( 3 > 0 ) and ( 3 < 5 ) ) # True
print( ( 3 > 0 ) & ( 3 < 5 ) ) # True
print( ( 3 < 0 ) and ( 3 < 5 ) ) # False

print( ( 3 < 0 ) or ( 3 < 5 ) ) # True
print( ( 3 < 0 ) | ( 3 < 5 ) ) # True

print( 5 > 4 > 3 ) # True
print( 5 > 4 > 7 ) # False