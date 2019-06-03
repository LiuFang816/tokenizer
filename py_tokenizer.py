from io import StringIO
from tokenize import generate_tokens

Example = '''def run():


	maxNum = max(1, -1.7) # 注释1
	# 注释2

	if maxNum > 0:
		print(maxNum)
	else:
		print("you guess what")
		print('I am iron man!')'''

# 以下token的类别和确切类别一致
# type 4: '\n' 表示本行语句后的换行
# type 56: '\n' 表示本行是空行，包括该行为注释，注释后的那个换行（siton上是55）
# type 5: '\t' '\t\t' ... 表示当前缩进等级，只在缩进等级增加时出现
# type 6: '' 表示本行减小一级缩进
# type 0: '' 表示文件结束，即 EOF
# type 55: 注释（siton上是54）

# 总结：4是有意义的换行不能删；5表示新的高缩进等级不能删；6表示缩进等级的减小不能删；0表示文件结束不能删
# ==> '\n'总是有用的代码行换行；而增缩进和减缩进我分别表示为：<_indent_xx> 和 <_dedent>
# ==> 通过栈维护依次出现的 <_indent_xx>，并根据 <_dedent> 弹栈，那么栈顶元素就是当前缩进
def tokenize(code, need_type_info=False, filterComment=True, filterBlankLine=True):
	strio = StringIO(code)
	gen = generate_tokens(strio.readline)

	indents = []

	tokens = []
	types = []
	exact_types = []
	while True:
		try:
			t = next(gen)
			token_ = t.string
			type_ = t.type
			extype_ = t.exact_type
			if filterComment and type_==54:
				continue
			if filterBlankLine and type_==55:
				continue
		except:
			break

		# 增缩进，减缩进，EOF
		if type_==6:
			tokens.append('<_dedent_>')
			indents.pop()
		elif type_==5:
			indents.append(token_)
			tokens.append('<_indent_' + str(len(indents)) + '>') # 当前缩进等级
		elif type_==0:
			tokens.append('<EOF>')
		elif type_==4:
			tokens.append('<NL>')
		else:
			tokens.append(token_)

		types.append(type_)
		exact_types.append(extype_)

	if need_type_info:
		return tokens, types, exact_types
	else:
		return tokens

if __name__=="__main__":
    print("No code/function passed in, function below is used to show you a case:")
    print()
    print(Example)
    print()
    tokens, types, extypes = tokenize(Example, True)
    for i,j,k in zip(tokens, types, extypes):
    	print(i, "||", j, "||", k)
    	print('~~~~~~~~~~~~~~~~~~~')
    print(tokens)