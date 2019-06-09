from io import BytesIO
from tokenize import tokenize, NUMBER, STRING, NAME

def py_tokenize(code_file, need_type_info):
	code = open(code_file, 'r').read()
	tokens = []
	types = []
	g = tokenize(BytesIO(code.encode('utf-8')).readline)
	for toknum, tokval, _, _, _ in g:
		tokens.append(tokval)
		types.append(toknum)
	# print(tokens)
	# print(types)

	if need_type_info:
		return tokens, types
	else:
		return tokens

if __name__=="__main__":
	tokens, types = py_tokenize('get_data.py', True)
	print(tokens)
	print(types)