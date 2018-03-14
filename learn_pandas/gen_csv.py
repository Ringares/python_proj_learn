import pandas as pd

id = []
name = []

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        id.append(line.split(',')[0].strip())
        name.append(line.split(',')[1].strip())

save = pd.DataFrame({'id': id, 'name': name})
save.to_csv('channel_tag_0312_2.txt', encoding='utf-8')
