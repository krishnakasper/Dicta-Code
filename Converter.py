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

    def optimizeOperation(self, string):
        operations = {"plus": "+",
                      "minus": "-",
                      "times": "*",
                      "quotient": "/",
                      "reminder": "%"}
        for op in operations:
            string = string.replace(op, operations[op])
        return string