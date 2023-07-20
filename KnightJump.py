with(open(input(),"r") as f): code = f.read()
if code[0]=="\n": code = code[1:]

width = 0
while code[width]!="\n": width+=1
height = code.count('\n')
x = 0
y = 0
direction = "S"

stack = []
dtable = {"S":[2,1],"s":[2,-1],\
          "N":[-2,1],"n":[-2,-1],\
          "W":[-1,2],"w":[1,2],\
          "E":[-1,-2],"e":[1,-2]}
enc = 0
def check(x,y,d):
    return  ([x,y] not in d) and (chrat(x,y) in [str(z) for z in range(0,10)])

def getnum(x,y,d):
    for b in [[-1,-1],[1,-1],[1,1],[-1,1]]:
        [cx,cy] = [wx(x+b[0]),wy(y+b[1])]
        if(check(cx,cy,d)):
            d.append([x,y])
            return chrat(x,y)+getnum(cx,cy,d)
    return chrat(x,y)

def chrat(x,y):
    return chr(ord(code[x+width*y+y])+enc)

def wx(num):
    if (num >= 0):
        return (num % width)
    else: 
        return width - (num % width)
        
def wy(num):
    if (num >= 0):
        return (num % height)
    else: 
        return height - (num % height)

while True:
    c = chrat(x,y)
    if c=="@": 
        break
    elif c=="$":
        stack.append(stack[-1])
    elif (c in ["N","n","S","s","W","w","E","e"]):
        direction = c
    elif c=="\\":
        [ stack[-2], stack[-1] ] = [ stack[-1], stack[-2] ]
    elif c=="%":
        stack.pop()
    elif c=="H":
        direction = {"N":"W","n":"E","S":"w","s":"e",\
                     "E":"S","e":"N","W":"s","w":"n"}[direction]
    elif c=="+":
        stack.append(stack.pop()+stack.pop())
    elif c=="-":
        [ stack[-2], stack[-1] ] = [ stack[-1], stack[-2] ]
        stack.append(stack.pop()-stack.pop())
    elif c==">":
        [ stack[-2], stack[-1] ] = [ stack[-1], stack[-2] ]
        stack.append(int(stack.pop()>stack.pop()))
    elif c=="<":
        [ stack[-2], stack[-1] ] = [ stack[-1], stack[-2] ]
        stack.append(int(stack.pop()<stack.pop()))
    elif c=="=":
        stack.append(int(stack.pop()==stack.pop()))
    elif c=="/":
        [ stack[-2], stack[-1] ] = [ stack[-1], stack[-2] ]
        stack.append(stack.pop()/stack.pop())
    elif c=="^":
        [ stack[-2], stack[-1] ] = [ stack[-1], stack[-2] ]
        stack.append(stack.pop()**stack.pop())
    elif c=="*":
        stack.append(stack.pop()*stack.pop())
    elif c==";":
        print(stack[-1],end="")
    elif c==":":
        stack.append(int(input()))
    elif c=="?":
        stack.append(ord(input()))
    elif c=="!":
        print(chr(stack[-1]),end="")
    elif c=="#":
        enc = stack.pop()
    elif chr(ord(c)-enc) == "~":
        enc = 0
    elif c in [str(x) for x in range(0,10)]:
        stack.append( int(getnum(x,y,[])) )
    
    x = wx(x+dtable[direction][1])
    y = wy(y+dtable[direction][0])