'''
references in
http://stackoverflow.com/questions/5087903/python-tuple-to-json-output
http://stackoverflow.com/questions/8230315/python-sets-are-not-json-serializable
'''


from dict_object import rows_all
from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle



class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}




id_list = {int(x[4]) for x in rows_all} # gives unique ID's
# id_list = [x[4] for x in rows_all] # gives all the ID's
print id_list



some_dict= {}
for id in id_list:
    some_dict.update({
                        id: {
                            'name': list({ str(x[1]) for x in rows_all if x[4]==id }),   #take out unique names from database and convert it to list
                            'checkin_date': [ str(x[2]) for x in rows_all if x[4]==id ],
                            'checkin_time': [ str(x[3]) for x in rows_all if x[4]==id ]
                            }
                      }
                     )


j= dumps(some_dict, cls=PythonObjectEncoder )

print j
