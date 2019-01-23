class Converter:
    str = ''

    def code(self, string):
        self.str = string
        # self.str=input("enter text")
        msg = "not changed"
        strs = ""
        x = 0
        tpy = ""
        strs = self.str.split()
        if strs[x] == "variable" or strs[x] == "var":
            x = x + 1
            if strs[x] == "integer" or strs[x] == "int" or strs[x] == "in":
                msg = "int "
            elif strs[x] == "float":
                msg = "float "

            elif strs[x] == "short":
                msg = "short "

            elif strs[x] == "byte":
                msg = "byte "

            elif strs[x] == "character" or strs[x] == "char":
                msg = "char "

            elif strs[x] == "boolean":
                msg = "bool "

            elif strs[x] == "double":
                msg = "double "

            elif strs[x] == "long":
                msg = "long "

            else:
                print(string)

            x = x + 1
            var = strs[x]
            x = x + 2
            if strs[x] == "to":
                x = x + 1
            value = strs[x]
            msg = msg + var + " = " + value + ";"

        elif strs[x] == "print":
            x = x + 1
            if strs[x] == "variable":
                x = x + 1
                msg = "System.out.println(" + strs[x] + ");"
            elif strs[x] == "string":
                x = x + 1
                ms = ""
                for i in range(x, len(strs)):
                    m = strs[i] + " "
                    ms += m
                msg = 'System.out.println("' + ms + '");'

        elif strs[x] == "for":
            x = x + 1
            msg = "for("
            if strs[x] == "loop":
                x = x + 1
            if strs[x] == "int":
                x = x + 1
                msg += "int "
            var = strs[x]
            msg += var
            x = x + 2
            if strs[x] == "to":
                x = x + 1
            msg = msg + " = " + strs[x] + ";"
            x = x + 1
            if strs[x] == var:
                x += 1
            if strs[x] == "less" and strs[x + 1] == "than":
                x += 2
                if strs[x] == "equal" and strs[x] == "to":
                    x += 2
                    msg = msg + var + " <= " + strs[x] + ";"
                else:
                    msg = msg + var + " < " + strs[x] + ";"
            elif strs[x] == "greater" and strs[x + 1] == "than":
                x += 2
                if strs[x] == "equal" and strs[x] == "to":
                    x += 2
                    msg = msg + var + " >= " + strs[x] + ";"
                else:
                    msg = msg + var + " > " + strs[x] + ";"

            x += 1
            if strs[x] == "increment":
                msg = msg + var + "++)"
            elif strs[x] == "decrement":
                msg = msg + var + "--)"
            msg = msg + """{

}"""
        elif strs[x] == "while":
            x += 1
            var = strs[x]
            x += 1
            if strs[x] == "less" and strs[x + 1] == "than":
                x += 2
                msg = "while(" + var + " < " + strs[x] + """){

}"""
            elif strs[x] == "greater" and strs[x + 1] == "than":
                x += 2
                msg = "while(" + var + " > " + strs[x] + """){

}"""

        elif strs[x] == "if":
            x += 1
            if strs[x] == "loop":
                x += 1

            var = strs[x]
            x += 1
            if strs[x] == "less" and strs[x + 1] == "than":
                x += 2
                msg = "if(" + var + " < " + strs[x] + '''){

}'''
            elif strs[x] == "greater" and strs[x + 1] == "than":
                x += 2
                msg = "if(" + var + " > " + strs[x] + '''){

}'''

        elif strs[x] == "elif":
            x += 1
            if strs[x] == "loop":
                x += 1

            var = strs[x]
            x += 1
            if strs[x] == "less" and strs[x + 1] == "than":
                x += 2
                msg = "elif(" + var + " < " + strs[x] + '''){

}'''
            elif strs[x] == "greater" and strs[x + 1] == "than":
                x += 2
                msg = "elif(" + var + " > " + strs[x] + '''){

}'''

        elif strs[x] == "else":
            msg = """else{

}"""

        print(msg)
        return msg

        '''       
        for x in range(0,len(strs)):
            if strs[x]=="variable":
                for l in range(x,len(strs)):
                    if strs[l]=="type":
                        if strs[l+1]=="integer" or strs[l+1]=="int":
                            msg+="int "
                        elif strs[l+1]=="float":
                            msg+="float "
                        elif strs[l+1]=="character" or strs[l+1]=="char":
                            msg+="char "
                        elif strs[l+1]=="boolean":
                            mas+="boolean "
                        elif strs[l+1]=="byte":
                            msg+="byte "
                        elif strs[l+1]=="short" or (strs[l+1]=="short" and (strs[l+2]=="integer" or strs[l+2]=="int")):
                            msg+="short "
                        elif strs[l+1]=="long" or (strs[l+1]=="long" or (strs[l+2]=="integer" or strs[l+2]=="int")):
                            msg+="long "
                        elif strs[l+1]=="double":
                            msg+="long "
                        elif strs[l+1]=="string":
                            msg+="string "
                    if len(strs[l])==1:
                        var=strs[l]
                    #if ((strs[l]=="equals"or strs[l]=="equal") and strs[l+1]=="to"):
                    if strs[l]=="=":
                        msg+=var+"="+strs[l+1]+";"
        print(msg)
        '''


'''
            elif strs[x]=="for":
                for l in range(x,len(strs)):
                    if strs[l]=="ranges":
                        var=strs[l-1]
                        upr=strs[l+4]
                        lwr=strs[l+2]
                        msg+="for(int "+var+"="+lwr+";"+var+"<="+upr+";"+var+"""++)
{

}"""
            elif strs[x]=="if":
                con=strs[x+1]
                if (strs[x+2]=="equals"or strs[x+2]=="equal") and strs[x+3]=="to":
                    con+="=="+strs[x+4]
                elif strs[x+2]=="not":
                    con+="!="+strs[x+5]
                elif strs[x+2]=="less" and len(strs[x+4])==1:
                    con+="<"+strs[x+4]
                elif strs[x+2]=="greater" and len(strs[x+4])==1:
                    con+=">"+strs[x+4]
                elif strs[x+2]=="less" and (strs[x+5]=="to"or strs[x+6]=="to"):
                    con+="<="+strs[x+7]
                elif strs[x+2]=="greater" and (strs[x+5]=="to"or strs[x+6]=="to"):
                    con+=">="+strs[x+7]
                for l in range (x,len(strs)):
                    while strs[l]=="and" or strs[l]=="or":
                        if strs[l]=="and":
                            con+=" && "
                        elif strs[l]=="or":
                            con+=" || "
                        con+=strs[l+1]
                        if (strs[l+2]=="equals"or strs[l+2]=="equal") or strs[l+3]=="to":
                            con+="=="+strs[l+4]
                        elif strs[l+2]=="not":
                            con+="!="+strs[l+5]
                        elif strs[l+2]=="less" and len(strs[l+4])==1:
                            con+="<"+strs[l+4]
                        elif strs[l+2]=="greater" and len(strs[l+4])==1:
                            con+=">"+strs[l+4]
                        elif strs[l+2]=="less" and (strs[l+5]=="to"or strs[l+6]=="to"):
                            con+="<="+strs[l+7]
                        elif strs[l+2]=="greater" and (strs[l+5]=="to"or strs[l+6]=="to"):
                            con+=">="+strs[l+7]
                msg+="if("+con+""")
{

}"""
            elif strs[x]=="else if":
                con=strs[x+1]
                if (strs[x+2]=="equals"or strs[x+2]=="equal") and strs[x+3]=="to":
                    con+="=="+strs[x+4]
                elif strs[x+2]=="not":
                    con+="!="+strs[x+5]
                elif strs[x+2]=="less" and len(strs[x+4])==1:
                    con+="<"+strs[x+4]
                elif strs[x+2]=="greater" and len(strs[x+4])==1:
                    con+=">"+strs[x+4]
                elif strs[x+2]=="less" and (strs[x+5]=="to"or strs[x+6]=="to"):
                    con+="<="+strs[x+7]
                elif strs[x+2]=="greater" and (strs[x+5]=="to"or strs[x+6]=="to"):
                    con+=">="+strs[x+7]
                for l in range (x,len(strs)):
                    while strs[l]=="and" or strs[l]=="or":
                        if strs[l]=="and":
                            con+=" && "
                        elif strs[l]=="or":
                            con+=" || "
                        con+=strs[l+1]
                        if (strs[l+2]=="equals"or strs[l+2]=="equal") or strs[l+3]=="to":
                            con+="=="+strs[l+4]
                        elif strs[l+2]=="not":
                            con+="!="+strs[l+5]
                        elif strs[l+2]=="less" and len(strs[l+4])==1:
                            con+="<"+strs[l+4]
                        elif strs[l+2]=="greater" and len(strs[l+4])==1:
                            con+=">"+strs[l+4]
                        elif strs[l+2]=="less" and (strs[l+5]=="to"or strs[l+6]=="to"):
                            con+="<="+strs[l+7]
                        elif strs[l+2]=="greater" and (strs[l+5]=="to"or strs[l+6]=="to"):
                            con+=">="+strs[l+7]
                msg+="if("+con+""")
{

}"""
            elif strs[x]=="else":
                msg+="""else
{

}"""
            elif strs[x]=="while":
                con=strs[x+1]
                if (strs[x+2]=="equals"or strs[x+2]=="equal") or strs[x+3]=="to":
                    con+="=="+strs[x+4]
                elif strs[x+2]=="not":
                    con+="!="+strs[x+5]
                elif strs[x+2]=="less" and len(strs[x+4])==1:
                    con+="<"+strs[x+4]
                elif strs[x+2]=="greater" and len(strs[x+4])==1:
                    con+=">"+strs[x+4]
                elif strs[x+2]=="less" and (strs[x+5]=="to"or strs[x+6]=="to"):
                    con+="<="+strs[x+7]
                elif strs[x+2]=="greater" and (strs[x+5]=="to"or strs[x+6]=="to"):
                    con+=">="+strs[x+7]
                for l in range (x,len(strs)):
                    while strs[l]=="and" or strs[l]=="or":
                        if strs[l]=="and":
                            con+=" && "
                        elif strs[l]=="or":
                            con+=" || "
                        con+=strs[l+1]
                        if (strs[l+2]=="equals"or strs[l+2]=="equal") or strs[l+3]=="to":
                            con+="=="+strs[l+4]
                        elif strs[l+2]=="not":
                            con+="!="+strs[l+5]
                        elif strs[l+2]=="less" and len(strs[l+4])==1:
                            con+="<"+strs[l+4]
                        elif strs[l+2]=="greater" and len(strs[l+4])==1:
                            con+=">"+strs[l+4]
                        elif strs[l+2]=="less" and (strs[l+5]=="to"or strs[l+6]=="to"):
                            con+="<="+strs[l+7]
                        elif strs[l+2]=="greater" and (strs[l+5]=="to"or strs[l+6]=="to"):
                            con+=">="+strs[l+7]

                msg+="while("+con+""")
{

}"""
            elif strs[x]=="print":
                for l in range(x+1,len(strs)):
                    con+=strs[l]
                    if l!=len(strs):
                        con+=" "
                msg+="Sysyem.out.print("+con+")"
            elif strs[x]=="print" and strs[x+1]=="output":
                for l in range(x+2,len(strs)):
                    con+=strs[l]
                    if l!=len(strs):
                        con+=" "
                msg+="Sysyem.out.print("+con+")"
        if "variable" not in self.str and "for" not in self.str and "if" not in self.str and "else if" not in self.str and "else" not in self.str and "while" not in self.str and "print" not in self.str:
            for x in range(0,len(strs)):
                if (strs[x]=="equals" or strs[x]=="equal")and strs[x+1]=="to":
                    msg+="="
                elif strs[x]=="plus":
                    msg+="+"
                elif strs[x]=="minus":
                    msg+="="
                elif strs[x]=="into" or strs[x]=="star":
                    msg+="*"
                elif strs[x]=="by":
                    msg+="/"
                elif strs[x]=="devided by":
                    msg+="%"
                elif strs[x]!="to":
                    msg+=strs[x]
'''
# print(msg)
# return msg
