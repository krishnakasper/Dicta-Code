from Converter import Converter


class CpCode(Converter):

    def __init__(self):
        Converter.__init__(self)

    def convert(self, input):
        input = self.optimizeInputString(input).lower()
        words = input.split()
        if words[0] == "add":
            if words[1] == "break" or words[1] == "continue":
                return words[1] + ";"

            if "for loop" in input:
                return """for(  ){

                }"""
            if "while loop" in input:
                return """while(  ){

                }"""
            if "if statement" in input:
                return """if(  ){

                }"""
            if "else if statement" in input:
                return """else if(  ){

                }"""
            if "else statement" in input:
                return """else{

                }"""

            if words[1] == "condition":
                variableType = self.findType(words[-1])
                if words[-1] in self.variable:
                    pass
                elif variableType == 'char':
                    words[-1] = "'" + words[-1] + "'"
                elif variableType == "string":
                    words[-1] = '"' + words[-1] + '"'
                if words[3] == "=":
                    words[3] = words[3] * 2
                return words[2] + " " + words[3] + " " + words[4]

            if words[1] == "variable":
                variableType = self.findType(words[-1])
                words[1] = variableType
                if words[2] in self.variable.keys():
                    words[1] = ""
                self.variable[words[2]] = variableType
                if variableType == "char":
                    words[-1] = "'" + words[-1] + "'"
                elif variableType == "string":
                    words[1] = "char[]"
                    words[-1] = '"' + words[-1] + '"'
                return words[1] + " " + words[2] + " " + words[3] + " " + words[4] + ";"

            if words[1] == "operation":
                ans = ""
                input = self.optimizeOperation(input)
                words = input.split()
                if words[4] not in self.variable or words[6] not in self.variable:
                    return "arg variables are not defined"
                if self.variable[words[4]] == self.variable[words[6]]:
                    if words[2] not in self.variable:
                        ans = self.variable[words[4]] + " "
                        self.variable[words[2]] = self.variable[words[4]]
                    ans = ans + words[2] + words[3] + words[4] + words[5] + words[6] + ";"
                    return ans
                else:
                    return "arg1 and arg2 are not same type"

        elif "declare" == words[0]:
            if words[2] in self.variable:
                return "variable already declared"
            if "string" == words[1]:
                self.variable[words[2]] = words[1]
                return "char[] " + words[2] + ";"
            elif "int" == words[1] or "integer" == words[1]:
                self.variable[words[2]] = "int"
                return "int " + words[2] + ";"
            elif "float" == words[1]:
                self.variable[words[2]] = words[1]
                return "float " + words[2] + ";"
            elif "char" == words[1] or "character" == words[1]:
                self.variable[words[2]] = "char"
                return "char " + words[2] + ";"
            elif "boolean" == words[1]:
                self.variable[words[2]] = "int"
                return "int " + words[2] + ";"

        elif words[0] == "print":
            if words[1] == "variable":
                if words[2] in self.variable:
                    return "count << " + words[2] + ";"
                else:
                    return "variable not declared"
            elif words[1] == "string":
                word = ""
                for i in range(len(words) - 2):
                    word += words[i + 2]
                return 'count << "' + word + '";'

        elif "increment" in words[0] or "decrement" in words[0]:
            if words[1] in self.variable:
                if self.variable.get(words[1]) == "int" or self.variable.get(words[1]) == "float":
                    if "pre_increment" in input:
                        return "++" + words[1] + ";"
                    if "post_increment" in input or "increment" in input:
                        return words[1] + "++;"
                    if "pre_decrement" in input:
                        return "--" + words[1] + ";"
                    if "post_decrement" in input or "decrement" in input:
                        return words[1] + "--;"
                else:
                    return "type error"
            else:
                return "variable error"
