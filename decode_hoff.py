c, symbols = input().split()
secretes = {}
for i in range(int(c)):
    key, value = input().split(': ')
    secretes[key] = value
string = input()
answer = ''
while True:
    for key, value in secretes.items():
        if string.startswith(value):
            answer += key
            string = string[len(value):]
    if not string:
        break
print(answer)
