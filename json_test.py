# -*- coding: utf-8 -*-

import json

# ENCODING _________________________________________________________________

# 변수명으로 저장해서 넣을 수도 있습니다.
dir_message = { 'name' : 'leni' }
print json.dumps(dir_message)


# 직접적으로 값을 바로 넣을 수도 있습니다.
print json.dumps("string")

# dir의 key값을 기준으로 정렬을 시킬 수도 있습니다.
print json.dumps({"c":0, "b":0, "a":0}, sort_keys=True)

# ____________________________________________________________________


# DECODING __________________________________________________________________

# 변수명으로 저장해서 넣을 수도 있습니다.
dir_message = { 'name' : 'leni' }
dir_message = json.dumps(dir_message)
print json.loads(dir_message)

# 직접적으로 값을 바로 넣을 수도 있습니다.
print json.loads(json.dumps("string"))

# 함수를 이용할 수 있습니다.
message = json.dumps({'__com__':True, 'r':1, 'i':2})
def com(d) :
	if '__com__' in d :
		return complex(d['r'], d['i'])
	return d

print json.loads(message, object_hook=com)
# ____________________________________________________________________


