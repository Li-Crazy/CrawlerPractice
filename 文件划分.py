def split_file(file_name):
    f = open(file_name)
    print(f)
    boy = []
    girl = []
    count = 1
    for f_line in f:
        if f_line[:6] != '======':
            (role, line_spoken) = f_line.split('：', 1)
            if role == '李':
                boy.append(line_spoken)
            elif role == '王':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)
            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)
    f.close()


def save_file(boy, girl, count):
    file_boy_name = 'boy_' + str(count) + '.txt'
    file_girl_name = 'girl_' + str(count) + '.txt'

    boy_file = open(file_boy_name, 'w')
    girl_file = open(file_girl_name, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

path = 'second.txt'
split_file(path)