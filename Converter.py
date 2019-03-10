class Converter:

    def __init__(self):
        self.variable = {}

    def optimizeInputString(self, input):
        input = str(input)
        if "equals to" in input:
            input = input.replace("equals to", "=", 1)

        elif "equal to" in input:
            input = input.replace("equal to", "=", 1)

        elif "equals" in input:
            input = input.replace("equals", "=", 1)

        elif "equal" in input:
            input = input.replace("equal", "=", 1)

        if "less than" in input:
            input = input.replace("less than", "<", 1)
            if "or" in input:
                input = input.replace(" or ", "", 1)

        elif "greater than" in input:
            input = input.replace("greater than", ">", 1)
            if "or" in input:
                input = input.replace(" or ", "", 1)

        if "pre increment" in input:
            input = input.replace("pre increment", "pre_increment")

        elif "post increment" in input:
            input = input.replace("postincrement", "post_increment")

        elif "pre decrement" in input:
            input = input.replace("pre decrement", "pre_decrement")

        elif "post decrement" in input:
            input = input.replace("post decrement", "post_decrement")

        return input

    def findType(self, input):
        if "." in input:
            return "float"
        elif input.isdecimal():
            return "int"
        elif len(input) == 1:
            return "char"
        elif input == "false" or input == "true":
            return "boolean"
        return "string"

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
                self.variable[words[2]] = variableType
                if variableType == "char":
                    words[-1] = "'" + words[-1] + "'"
                elif variableType == "string":
                    words[-1] = '"' + words[-1] + '"'
                return words[1] + " " + words[2] + " " + words[3] + " " + words[4]

        elif "declare" == words[0]:
            if words[2] in self.variable:
                return "variable already declared"
            if "string" == words[1]:
                self.variable[words[2]] = words[1]
                return "String " + words[2] + ";"
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
                self.variable[words[2]] = words[1]
                return "boolean " + words[2] + ";"


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
