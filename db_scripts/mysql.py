import time
import pymysql as mc
conn = None
cursor = None
conn = mc.Connect(
    host='10.10.199.87',
    user='mysqlsiud',
    passwd='mysql!@#456',
    db='ssy_dmp',
    charset='utf8'
)
cursor = conn.cursor()
# tags = ['女神', '奇闻', '时尚', '电影', '美文', '趣图', '萌宠', '美图', '京剧']
tags = ['小说']
vals = []
for tag in tags:
    now = int(time.time() * 1000)
    dimension_id = 63
    dimension_name = '用户爱好'
    alias_id = 0
    relevance = 0
    related_tags = '[]'
    reference = 0
    create_time = now
    update_time = now
    status = 1
    vals.append((dimension_id, dimension_name, alias_id, tag, relevance, related_tags, reference, create_time,
                 update_time, status))
sql = '''
        insert into dmp_tag(dimension_id,dimension_name,alias_id,name,relevance,related_tags,reference,create_time,update_time,status)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
cursor.executemany(sql, vals)
conn.commit()




#######################################
# select
######################################
import pymysql as mc
conn = None
cursor = None
try:
    conn = mc.Connect(
        host='10.10.199.87', #192.168.30.245; 10.10.199.87
        user='mysqlsiud',
        passwd='mysql!@#456',
        db='ssy_dmp',
        charset='utf8'
    )
    cursor = conn.cursor()
    # cursor.execute('select id,name from dmp_tag where dimension_id=63 order by id desc')
    cursor.execute('select * from dmp_tag where dimension_id=63 order by id desc')
    tags = cursor.fetchall()
    for tag in tags: print(tag)
finally:
    if conn: conn.close()
    if cursor: cursor.close()
######################################


#######################################
# UPDATE
######################################
import pymysql as mc
conn = None
cursor = None
try:
    conn = mc.Connect(
        host='10.10.199.87',
        user='mysqlsiud',
        passwd='mysql!@#456',
        db='ssy_dmp',
        charset='utf8'
    )
    cursor = conn.cursor()
    cursor.execute('UPDATE dmp_tag SET name=\'奇闻\' WHERE id=1520 AND dimension_id=63')
    conn.commit()
    # tags = cursor.fetchall()
    # for tag in tags: print(tag)
finally:
    if conn: conn.close()
    if cursor: cursor.close()
#######################################



#######################################
# DELETE
######################################
import pymysql as mc
conn = None
cursor = None
try:
    conn = mc.Connect(
        host='10.10.199.87', #192.168.30.245
        user='mysqlsiud',
        passwd='mysql!@#456',
        db='ssy_dmp',
        charset='utf8'
    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dmp_tag WHERE id=1144860 AND dimension_id=63')
    conn.commit()
    # tags = cursor.fetchall()
    # for tag in tags: print(tag)
finally:
    if conn: conn.close()
    if cursor: cursor.close()
#######################################