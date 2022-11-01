import hikari_messages
#import hikari_key_words as hkw
import sys 
import random

hm = hikari_messages.Hikari_Messages()
at  = hm.key_words.all_topics

flag_do_all_found = True

# All weights
#print(hkw.weights)

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

  # The topic that was received
  the_topic = getTopic(index_list)
##  print("Received Topic = ",end='')
##  print(the_topic) 

  # The topic that we will reply with
  reply_topic = getReplyTopic(the_topic)
##  print("Reply Topic = ", end='')
##  print(reply_topic)

  # The reply message
  reply_message = getReplyMessage(reply_topic)
##  print("Reply Message = ", end='')
  print(reply_message)

def getReplyMessage(reply_topic=None):
  msgs = hm.reply.all_topics[reply_topic]
  L = len(msgs)
  index = random.randint(0,L-1)
  return msgs[index]

  
def getReplyTopic(the_topic=None):
  if the_topic == None:
    return None
  
  weights = hm.weights[the_topic]

  total = sum(weights)
 
  the_indexes = []
  the_index_values = []
  the_weight_thresh = []
  for i in range(len(weights)):
    the_out = 0
    if weights[i] > 0.000001:
      the_out = 1
      the_index_values.append(i)
      the_weight_thresh.append(sum(weights[0:i]))
    the_indexes.append(the_out)

  the_rand_val = random.random()*total
  for j in range(len(the_weight_thresh)):
    i = len(the_weight_thresh) - 1 - j
    if the_rand_val >= the_weight_thresh[i]:
      return the_index_values[i]
  return None


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
