class Stack(object):
    def __init__(self):
        self.items = []
    
    def __iter__(self):
        print(self.items)
    
    def __len__(self):
        print(len(self.items))
    
    def is_Empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def search(self,item):
        return self.items.index(item)
    
def express_match(expression):
    """表达式匹配"""
    left_bracket = '[(<“'
    right_bracket = '])>”'
    match_dict = {"]":"[", "“":"”",">":"<", ")":"("}
    s = Stack()
    for i in expression:
        if i in left_bracket:
            s.push(i)
        elif i in right_bracket:
            if match_dict[i] == s.pop():
                continue
    if s.is_Empty():
        print("match successfully")
    else:
        print("match failed")
    
def divideByN(number,base):
    """
    进制转换
    parameters：n为目标进制
    """
    s = Stack()
    digits = "0123456789ABCDEF"
    rem = 0 # 余数
    new_number = ""

    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base
    
    while not s.is_Empty():
        new_number += digits[s.pop()]
    print(new_number)

def inToPref(calculations):
    """中缀表达式转为前缀"""
    s1 = Stack()
    s2 = Stack()
    prefix = ""
    priority_dict = {"+":0, "-":0, "*":1, "/":1}
    nums = [str(i) for i in range(10)]
    for i in calculations:
        if i in nums:
            s1.push(i)
        elif i == "(" or s2.is_Empty():
            s2.push(i)
        elif i in priority_dict.keys():
            if s2.peek() == "(":
                s2.push(i)
            elif priority_dict[s2.peek()] == priority_dict[i]:
                s2.push(i)
        else:
            while not s2.peek() == "(":
                s1.push(s2.pop())
            s2.pop()
    while not s2.is_Empty():
        s1.push(s2.pop())
    while not s1.is_Empty():
        prefix += str(s1.pop())
    print(prefix)

    
if __name__ == "__main__":
    expression1 = '[(<>)]'
    express_match(expression1)

    expression2 = '(<[]>'
    express_match(expression2)

    divideByN(2001,2)

    inToPref("1+((2+3)*4)-5")

    