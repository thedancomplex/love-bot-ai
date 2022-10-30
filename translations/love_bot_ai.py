import hikari_key_words as hkw
import sys 
import random

hkw = hkw.Hikari_Keywords()
at  = hkw.all_topics

flag_do_all_found = True

def main():
  message = ''
  if len(sys.argv) <= 1:
    mesasge = 'no_topic'
  else:
    message = str(sys.argv[1])
  the_out = getTopicList(message)
#  print(the_out)
#  print(the_out.index(max(the_out)))

  index_list = getTopicIndex(the_out)
#  print(index_list)

  fin = getTopic(index_list)
  print(fin) 

def getTopic(index_list=None):
  L = len(index_list)
  r = random.randint(0,L-1)
  return index_list[r]

  

def getTopicIndex(topic_list=None):
  the_max = max(topic_list)
  the_out = []
  for i in range(len(topic_list)):
    if topic_list[i] == the_max:
      the_out.append(i)
  return the_out


def getTopicList(message=None):
#  f = message.find('アカリ')
  the_out = []

  for i in range(len(at)):
    ati = at[i]
    ot  = 0
    for j in range(len(ati)): 
      wrd = ati[j]
      f = message.find(wrd)
      if f != -1:
        if flag_do_all_found:
          ot = 1
        else:
          ot += 1
    the_out.append(ot)
  if sum(the_out) < 1:
    the_out[len(the_out)-1] = 1

  return the_out

main()
