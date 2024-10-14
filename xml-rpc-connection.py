import xmlrpc.client

url = 'http://localhost:8069'
username = 'admin'
password = 'admin'
db = 'theodoobd'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
print(common.version())
user_uid = common.authenticate(db, username, password, {})
print(user_uid)

'xmlrpc/2/object' 'execute_kw'
'db, uid, password, model_name, method_name, [], {}'

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

#search function
property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search', [[]])
print("search function ==>", property_ids)

#count function
count_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_count', [[]])
print("count function ==>", count_property_ids)

#read function
read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'read', [property_ids], {'fields': ['name']})
print("read function ==>", read_property_ids)

#read function
search_read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_read', [[]], {'fields': ['name']})
print("search_read function ==>", search_read_property_ids)

#create function
#create_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'create', [{'name': 'Property from RPC', 'sales_id': 2}])
#print("create property ==>", create_property_ids)

#write function
# write_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'write', [[3], {'name': 'Property from RPC Updated 2'}])
# reach_name_get = models.execute_kw(db, user_uid, password, 'estate.property', 'name_get', [[3]])
# print("write property ==>", write_property_ids)
# print("reach_name_get property ==>", reach_name_get)

#unlink function
#unlink_property_id = models.execute_kw(db, user_uid, password, 'estate.property', 'unlink', [[3]])
#print("unlink_property_id property ==>", unlink_property_id)
