import config
import mirrorbase

if config.file != "":
    with open(config.file,"r") as f:
        code = f.read()
else:
    code = input()

to_num = {(1,-2) : 0, (-1,-2) : 1, (2,-1) : 2, (2,1) : 3, (1,2) : 4, (-1,2) : 5, (-2,-1) : 6, (-2,1) : 7}
to_dir = [(1,-2), (-1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,-1), (-2,1)]
ncode = [[]]
for i in code:
    if i == "\n":
        ncode.append([])
        continue
    ncode[-1].append(i)
code = ncode

width = len(max(code,key=lambda a: len(a)))
for i in code:
    while len(i) < width:
        i.append(" ")
height = len(code)

def get_num(code,pos, back=None):
    if back == None: back = []
    back.append(pos)

    if (npos := ( (pos[0]-1)%width, (pos[1]-1)%height )) not in back\
        and code[npos[1]][npos[0]] in [str(x) for x in range(10)]:
        return code[pos[1]][pos[0]] + get_num(code, npos, back)
    
    if (npos := ( (pos[0]+1)%width, (pos[1]-1)%height )) not in back\
        and code[npos[1]][npos[0]] in [str(x) for x in range(10)]:
        return code[pos[1]][pos[0]] + get_num(code, npos, back)
    
    if (npos := ( (pos[0]+1)%width, (pos[1]+1)%height )) not in back\
        and code[npos[1]][npos[0]] in [str(x) for x in range(10)]:
        return code[pos[1]][pos[0]] + get_num(code, npos, back)
    
    if (npos := ( (pos[0]-1)%width, (pos[1]+1)%height )) not in back\
        and code[npos[1]][npos[0]] in [str(x) for x in range(10)]:
        return code[pos[1]][pos[0]] + get_num(code, npos, back)
    
    return code[pos[1]][pos[0]]

def execute(code):
    stack = []
    pos = (0,0)
    enc = 0
    direction = (1,2)
    cc = code[pos[0]][pos[1]]
    while cc != "@":
        cc = code[pos[1]][pos[0]]

        if cc in mirrorbase.mb: direction = to_dir[mirrorbase.change_dir(to_num[direction],cc)]
        elif cc == "$": stack.append(stack[-1])
        elif cc == "\\": stack[-1],stack[-2] = stack[-2],stack[-1]
        elif cc == "%": stack.pop()
        elif cc in [str(x) for x in range(10)]: stack.append(int(get_num(code,pos)))
        elif cc == "+": stack.append(stack.pop()+stack.pop())
        elif cc == "-": stack.append(stack.pop()-stack.pop())
        elif cc == "*": stack.append(stack.pop()*stack.pop())
        elif cc == "/": stack.append(stack.pop()/stack.pop())
        elif cc == "^": stack.append(stack.pop()**stack.pop())
        elif cc == ">": stack.append(int(stack.pop()>stack.pop()))
        elif cc == "<": stack.append(int(stack.pop()<stack.pop()))
        elif cc == "=": stack.append(int(stack.pop()==stack.pop()))
        elif cc == ":": stack.append(int(input()))
        elif cc == ";": print(stack[-1])
        elif cc == "?": stack.append(ord(input()))
        elif cc == "!": print(chr(stack[-1]), end="")
        elif cc == "#":
            for i,v in enumerate(code):
                for j,w in enumerate(v):
                    code[i][j] = "~" if w == "~" else chr(ord(w)+stack[-1])
                    enc = stack.pop()
        elif cc == "~":
            for i,v in enumerate(code):
                for j,w in enumerate(v):
                    code[i][j] = "~" if w == "~" else chr(ord(w)-enc)
                    enc = 0
        elif cc == "&":
            stack = stack[-1]
        pos = ((pos[0] + direction[0]) % width, (pos[1] + direction[1]) % height)

execute(code)
