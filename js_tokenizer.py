from slimit.lexer import Lexer

CodeExample = \
"""// 这是我随便写的注释
var browser=navigator.appName
var b_version=navigator.appVersion
var version=parseFloat(b_version)
document.write("浏览器名称："+ browser)
document.write("<br />")
document.write("浏览器版本："+ version)"""

def tokenize(code, need_type_info=False):
    lexer = Lexer()
    lexer.input(code)

    tokens = []
    types = []
    for token in lexer:
        #print(token)
        tokens.append(token.value)
        types.append(token.type)

    if need_type_info:
        return tokens, types
    else:
        return tokens

if __name__=="__main__":
    print("No code/function passed in, function below is used to show you a case:")
    print()
    print(CodeExample)
    print()
    tokens, types = tokenize(CodeExample, True)
    print(tokens)
    print(types)