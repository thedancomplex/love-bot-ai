import hikari_key_words_weights as hkww
import hikari_key_words as hkw
import hikari_reply_message as hrm
class Hikari_Messages:
  def __init__(self):
    self.weights = hkww.hikari_reply_weights
    self.key_words = hkw.Hikari_Keywords()
    self.reply = hrm.Hikari_Reply_Messages()
    pass
