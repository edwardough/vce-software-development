phobia = input("What's your phobia? ")
sentence = input("Text: ")

if phobia in sentence:
  print("True")
  sentence = sentence.replace(phobia,"fave")
  print(sentence)
else:
  print("False")
  print(sentence)
