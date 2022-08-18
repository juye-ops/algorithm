init = input()

if len(init) == 1:
    init = '0' + init
new = init
cnt=0
while True:
    tmp = new
    new = tmp[-1] + str(sum(map(int, tmp)))[-1]
    cnt += 1
    if init == new: break
print(cnt)
