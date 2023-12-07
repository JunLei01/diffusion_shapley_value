import json

sum = 0
key_list = []
value_list = []
with open('../result/Increment_FID.json', 'r', encoding='utf-8') as fp:
    compositions = json.load(fp)
    for key, value in compositions.items():
        sum += abs(value)
        key_list.append(key)
        value_list.append(value)

    print(key_list, value_list, sum)
    i = 0
    for value in value_list:
        value = value / sum
        value_list[i] = -value
        i += 1

    dict = {}
    for j in range(len(value_list)):
        dict[key_list[j]] = value_list[j]
    fp.close()
    print(dict)
