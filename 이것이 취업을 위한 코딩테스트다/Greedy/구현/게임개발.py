n, m = map(int, input().split())
a, b, direction = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


#북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dmap = [[0]* m for _ in range(n)]
x, y = a, b

dmap[x][y] = 1

count = 1
turn_count = 0

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    turn_count += 1

    if dmap[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny
        dmap[x][y] = 1
        count += 1
        turn_count = 0
    elif turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        turn_count = 0

        if dmap[nx][ny] == 0 or array[nx][ny] == 0:
            x, y = nx, ny
            dmap[x][y] = 1
            count += 1
        else:   
            break
              
    else:
        continue

   


print(count)


    





