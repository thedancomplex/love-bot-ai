import hikari_key_words as hkw
import sys 

hkw = hkw.Hikari_Keywords()

at = hkw.all_topics

if len(sys.argv) <= 1:
  exit()

#print(len(sys.argv))
#print(str(sys.argv[1]))

message = str(sys.argv[1])

f = message.find('アカリ')
#f = message.find('いい天気')
print(f)

if f != -1:
  print('found')
else:
  print('not found')


#print(at)
#print(len(at))
the_out = []

for i in range(len(at)):
  ati = at[i]
  ot  = 0
  for j in range(len(ati)): 
    wrd = ati[j]
    f = message.find(wrd)
    if f != -1:
      ot += 1
  the_out.append(ot)

print(the_out)
print(len(the_out))
print(len(at))
