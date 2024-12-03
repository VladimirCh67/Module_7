
def custom_write(file_name, strings):
    st_ = 0
    bt_ = 0
    strings_positions = {}
    file = open(file_name, "a", encoding = 'utf-8')
    for i in range(len(strings)):
        st_ = i + 1
        bt_ = file.tell()
        s_b = (st_,bt_)
        strings_positions[s_b] = strings[i]
        file.write(strings[i]+"\n")

    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)