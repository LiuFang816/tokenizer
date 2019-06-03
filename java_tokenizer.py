import javalang

FuncExample = \
"""//这是我随便写的注释
@FuzyAnnotation
private void doParse(String pakageName) throws Exception
{
	if (StringUtils.isBlank(packageName))
	{
		/*
			这是我随便写的注释
		*/
		creatorAnnotationParser.parse();
	} else
	{
		System.out.print("This is a string!");
		creatorAnnotationParser.parse(packageName);
	}
}"""

def tokenize(code, need_type_info=False):
	token_gen = javalang.tokenizer.tokenize(code)
	tokens = []
	while(True):
		try:
			token = next(token_gen)
		except:
			break
		tokens.append(token)

	pure_tokens = [token.value for token in tokens]
	if need_type_info:
		token_types = [str(type(token))[:-2].split(".")[-1] for token in tokens]
		return (pure_tokens, token_types)
	else:
		return pure_tokens

if __name__=="__main__":
	#print("No code/function passed in, function below is used to show you a case:")
	#print()
	#print(FuncExample)
	#print()
	# with open('../data/RejectedPolicyWithReport.java', 'r') as f:
	# 	text = f.read()
	text = FuncExample
	tokens, types = tokenize(text, True)
	print(tokens)
	print(types)