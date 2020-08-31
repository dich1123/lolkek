#from mutagen.easyid3 import EasyID3

#lol = EasyID3(r'C:\Users\chere\Downloads\whiterabbit.mp3')



data = """
10011111 10100111 10111110 10111101 11011111 11111101 11011111 11011010
 11111111 10010100 11001110 11011110 11111111 11111110 11101100 10111100
  11110001 10011100 11001111 11111110 10010000 11111110"""
data = data.replace('\n', '')
data = data.split()
answ = ''
for i in data:
    a = i[:4]
    b = i[4:]
    lol = int(a, 2) ^ int(b, 2)
    answ += chr(lol)
print(answ)