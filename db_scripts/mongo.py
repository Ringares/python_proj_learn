
# #######################################
# # 查 api_config
# ######################################
import pymongo
import simplejson
source_tag_dic = {}
client = None
try:
    client = pymongo.MongoClient('node1.mongodb.ulike.dmp.com', 27017)
    db = client['ssy_ulike']
    db.authenticate('mongosiud', 'mongo!@#456')
    api_config = db['api_config']
    for doc in api_config.find({}, {'setting': 1, 'desc': 1}):
        setting = simplejson.loads(doc['setting'])
        source = setting['source']
        alias = setting['alias']
        print(source, alias)
        if source in source_tag_dic.keys():
            if alias not in source_tag_dic[source]:
                source_tag_dic[source].append(alias)
        else:
            source_tag_dic[source] = [alias]
except Exception as e:
    print('_id:' + str(doc['_id']) + ' Exception:%s' % repr(e))
for k, v in source_tag_dic.items():print(k,v)
# ######################################
# ######################################

# dmp_tags.find({'desc.alias':'as'})

# dmp_tags.find({'desc.alias':{'$eq':None}}).count()


# #######################################
# # 查 dmp_tags
# ######################################
import pymongo
client = pymongo.MongoClient('node1.mongodb.ulike.dmp.com', 27017)
db = client['ssy_ulike']
db.authenticate('dmp', 'dmp!@#456')
dmp_tags = db['dmp_tags']
######################################
######################################


print(dmp_tags.find({}).count())
for doc in dmp_tags.find({'level':0}): print(doc)
for doc in dmp_tags.find({'name':'小说'}): print(doc)
for doc in dmp_tags.find({}).limit(50): print(doc)
for doc in dmp_tags.find({'type':2}).limit(50): print(doc)
for doc in dmp_tags.find({},{'desc':0}).limit(50).sort('updatetime',pymongo.DESCENDING): print(doc)

docs = dmp_tags.find({'type':0}).limit(10)
for d in docs: print(d)

# print(dmp_tags.find({}).count())
# print(dmp_tags.find({'level':0}).count())
# print(dmp_tags.find({'level':1}).count())
# print(dmp_tags.find({'level':2}).count())
# print(dmp_tags.find({'level':2, 'type':0}).count())
# print(dmp_tags.find({'level':2, 'type':1}).count())
# time_set = set([])
# for doc in dmp_tags.find():
#     time_set.add(doc['createtime'])
#
# print(time_set)
# print(time_set)
