

def convertIdMongo(objs):
    if type(objs) != type(list()):
        obj_aux = objs
        objs = [obj_aux]

    for obj in objs:
        id = str(obj['_id'])
        obj['id'] = id
        del obj['_id']

    return objs
