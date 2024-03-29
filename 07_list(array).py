# 리스트(배열) []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호씨가 몇번째 칸에 타고있는지
print(subway.index('조세호'))

# 리스트 마지막에 더하기
subway.append('하하')
print(subway)

# 리스트 사이에 넣기
subway.insert(1, '정형돈')
print(subway)

# 리스트 뒤에서부터 제외
subway.pop()
print(subway)

# subway.pop()
# print(subway)

# subway.pop()
# print(subway)

# 값이 몇개인지 확인
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 순차 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 역순 정렬
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ['조세호', 20, True]

# 리스트 합치기
num_list.extend(mix_list)
print(num_list)