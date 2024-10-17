# **Интересные задачи и решения к ним**
## Содержание

1. [Интерпритатор](./tasks.md#интерпритатор)


<br><br>

## Интерпритатор

Условие:

> 
>URL Codewars: https://www.codewars.com/kata/53005a7b26d12be55c000243

>Simpler Interactive interpreter (or REPL)
>You will create an interpreter which takes inputs described below and produces outputs, storing state in between each input. This is a simplified version of the Simple Interactive Interpreter kata >with functions removed, so 
>if you have fun with this kata, check out its big brother to add functions into the mix.
>If you're not sure where to start with this kata, check out ankr's Evaluate Mathematical Expression kata.
>Note that the eval command has been disabled.
>Concepts
>The interpreter will take inputs in the language described under the language header below. This section will give an overview of the language constructs.
>Variables
>Any identifier which is not a keyword will be treated as a variable. 
>If the identifier is on the left hand side of an assignment operator, the result of the right hand side will be stored in the variable. If a variable occurs as part of an expression, the value held in the variable will be substituted when the expression is evaluated.
>Variables are implicitly declared the first time they are assigned to.
>Example: 
>Initializing a variable to a 
constant value and using the variable in another expression (Each line starting with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)
>Input:
>Input will conform to the expression production in the grammar below.
>Output:
>Output for a valid expression will be the result of the expression.
>Output for input consisting entirely 
>of whitespace will be an empty string (null in case of Java).
>All other cases will throw an error.

<details>
<summary><b>Решение:</b></summary>

```python

import re

def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile(r"\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression:str):
        res = expression
        
        # replace all vars
        for k in self.vars.keys():
            res = res.replace(k, str(self.vars[k]))
            
        ls = tokenize(res)
        if not ls:
            return ""
        
        if "(" not in ls and ")" not in ls and False in [ls[i] in "+-=*/%" for i in range(1, len(ls), 2)]:
            raise ValueError(f"input: '{expression}'")
        
        time_ls = ls
        x, y = None, None
        try:
            if "(" in ls or ")" in ls:
                i = 0
            else:
                i = 1

            while len(ls) > 1:
                
                if '(' in ls and ls.count("(")==ls.count(")"):
                    if ls[i]=="(":
                        x = i
                    elif ls[i]==")":
                        y = i
                    
                    if not y is None and not x is None:
                        time_ls = ''.join(ls[x+1:y])
                        res = self.input(time_ls)
                        ls[x:y+1] = [str(res)]
                        i = 0
                        x, y = None, None
                        continue
                # level №1
                elif "*" in ls or "/" in ls or "%" in ls:
                    if ls[i] == "*":
                        new = float(ls[i-1]) * float(ls[i+1])
                        
                        del ls[i-1]
                        del ls[i-1]
                        ls[i-1] = new
                        
                        i = 0
                        
                    elif ls[i] == "/":
                        new = float(ls[i-1]) / float(ls[i+1])
                        
                        del ls[i-1]
                        del ls[i-1]
                        ls[i-1] = new
                        
                        i = 0
                    
                    elif ls[i] == "%":
                        new = float(ls[i-1]) % float(ls[i+1])
                        
                        del ls[i-1]
                        del ls[i-1]
                        ls[i-1] = new
                        i = 0
                
                # level №2
                elif "+" in ls or "-" in ls:
                    if ls[i] == "+":
                        new = float(ls[i-1]) + float(ls[i+1])
                        
                        del ls[i-1]
                        del ls[i-1]
                        ls[i-1] = new
                        
                        i = 0
                    
                    elif ls[i] == "-":
                        new = float(ls[i-1]) - float(ls[i+1])
                        
                        del ls[i-1]
                        del ls[i-1]
                        ls[i-1] = new
                        
                        i = 0

                # level №3
                elif "=" in ls and ls[i] == "=":
                    self.vars[ls[i-1]] = float(ls[i+1])
                    ls = [self.vars[ls[i-1]]]
                    i = 0
                else:
                    break
                # step up
                i += 1

            # return result
            ls[0] = float(ls[0])
            return ls[0] if ls[0] != int(ls[0]) else int(ls[0])
    
        except ValueError as e:
            error = str(e)
            raise ValueError(f"input{error[error.index(': '):]}")
        


if __name__=="__main__":
    inp = Interpreter()
    print(inp.input("(8 - (4 + 2)) * 3"))

```

</details>

Суть задачи сводиться к тому, чтобы реализовать последовательный порядок действий. Мое решение реализуется с использованием библиотеки регулярных выражений и написанию собственного класса "интерпритатора", который вычисляет математические выражения быстрее, чем встроенная в python функция `eval()`.

Важно, что мое решение работает с правилами математических операций, т.е операция в скобках будет выполняться раньше, чем операция вне их. То же самое и с порядком умножения, деления сложения и вычистания.


