
input_1 = ['words', 'in', 'thing']
k_1 = 10

input_2 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k_2 = 16


def split_text(input, k):
    lines = []
    str = ''
    lineLength = 0
    i = 0
    for word in input:
        lineLength += len(word)
        if lineLength < k:
            if i == 0:
                str += word
            else:
                str += ' ' + word
                lineLength += 1
        else:
            lines.append(str)
            str = word
            lineLength = len(word)
        i += 1
    lines.append(str)
    print_lines(lines)
    justify_text(lines, k)
    print_lines(lines)

def justify_text(lines, k):
    i = 0
    for line in lines:
        while len(line) <= k:
            lst = find_all(' ', line)
            p = 0
            for index in lst:
                line = insert_space(line, index + p)
                p += 1
        lines[i] = line
        i += 1
    return lines

def insert_space(string, index):
    return string[:index] + ' ' + string[index:]

def find_all(needle, hay):
    lst = []
    for pos,char in enumerate(hay):
        if(char == needle):
            lst.append(pos)
    return lst

def print_lines(lines):
    for line in lines:
        print(line)


split_text(input_2, k_2)
