
with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("длина получившейся строки", len(content))
words = content.split()
print('количество слов в тексте :', len(words))
new_content = content.replace('.', '!')

with open ('referat2.txt', 'w') as f:
  f.write(new_content)
