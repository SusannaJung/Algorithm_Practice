input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

result = 0

#나이트가 이동할 수 있는 8가지 방향 정의
steps =[(-2,-1), (-2,1), (2, -1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]

for step in steps:
    nrow = row + step[0]
    ncolumn = column + step[1]

    if nrow >=1 and ncolumn >=1 and nrow <=8 and ncolumn <=8:
        result += 1


print(result)
