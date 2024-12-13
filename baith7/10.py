print("đinh văn thiện")
print("235752021610032")
def find_longest_words(text):
  words = text.split()
  max_length = len(max(words, key=len))
  longest_words = [word for word in words if len(word) == max_length]
  return longest_words

text = ("đinh văn thiện trường đại học Vinh.")
longest = find_longest_words(text)
print("Các từ dài nhất là:", longest)
