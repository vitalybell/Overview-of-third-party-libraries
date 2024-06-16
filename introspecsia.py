import inspect

type(5)
type([])
type({})

from pprint import pprint

obj = 42
pprint(dir(obj))
pprint(type(obj))
obj_string = 'Hello'
obj_list = [obj, obj_string]
pprint(list(obj_list))
def introspection_info(self, obg):
    pass
introspection_info.obj = True
pprint(callable(introspection_info))
pprint(dir(introspection_info))
pprint(hasattr(introspection_info, 'obj'))