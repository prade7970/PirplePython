from collections import Counter,OrderedDict


if __name__ == '__main__':
    s = input()
    slist= sorted(list(s))
    print(Counter(slist))
    print()
    od=OrderedDict(Counter(slist).most_common(3))
    for key,value in od.items():
        print(key,value)


