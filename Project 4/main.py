from functools import cache
from stack import Stack
stk = Stack()

def notGreater(i):
        precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        try:
            a = precedence[i]
            b = precedence[stk.top()]
            return True if a  <= b else False
        except KeyError:
            return False

def eval_postfix(exp):
    if exp == None:
        raise ValueError()
    if len(exp) == 1:
        return float(exp)
    for i in exp:
        if(i.isnumeric()):
            stk.push(i)
        elif(i.isspace()):
            continue
        else:
            try:
                value_one = stk.pop()
                value_two = stk.pop()
                stk.push(str(eval(value_two + i + value_one)))
            except:
                raise SyntaxError()
    return float(stk.pop())

def in2post(exp):
    if(not isinstance(exp,str)):
        raise ValueError("exp not a string")
    output = []
    for i in exp:
        if( i.isnumeric()):
            output.append(i)
        elif i =='(':
            stk.push(i)

        elif i ==')':
            while ((not (stk.size() == 0)) and stk.top() != '(' ):
                temp = stk.pop()
                output.append(temp)
            if ((not (stk.size() == 0)) and (stk.top() != '(')):
                raise SyntaxError("invalid Syntax")
            else:
                try:
                    stk.pop()
                except:
                    raise SyntaxError("invalid Syntax")
        else:
            while((not (stk.size() == 0)) and notGreater(i)):
                output.append(stk.pop())
            stk.push(i)

    while(not (stk.size() == 0)):
        output.append(stk.pop())

    return( " ".join(output))

def main():
    with open('./data.txt') as f:
        lines = f.readlines()

    for line in lines:
        input = line.strip().split(",")
        string_inpt = input[0]
        print("infix: " + string_inpt)
        post_inpt = in2post(string_inpt)
        print("postfix: " + str(post_inpt))
        answer = eval_postfix(post_inpt)
        print("answer: " + str(answer))
        print("")

if __name__ =="__main__":
    main()