def mutate_string(string, position, character):
    li = list(string)
    li[position] = character
    out = ''.join(map(str,li))
    return out

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
