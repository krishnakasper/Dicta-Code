class Converter:
    speechString = ''
    seperatedString = None
    i = 0
    s = ''
    newString = ''

    def putString(self, string):
        self.speechString = string
        self.splitString()

    def splitString(self):
        self.seperatedString = self.speechString.split()
        # print(self.seperatedString[self.i])
        self.choose()

    def choose(self):
        if self.seperatedString[self.i] == 'integer':
            self.newString = "int "
            self.datatype()

        elif self.seperatedString[self.i] == 'float':
            self.newString = "float "
            self.datatype()

        elif self.seperatedString[self.i] == 'short':
            self.newString = "short "
            self.start()


        elif self.seperatedString[self.i] == 'long':
            self.newString = "long "
            self.datatype()


        elif self.seperatedString[self.i] == 'double':
            self.newString = "double "
            self.datatype()

        elif self.seperatedString[self.i] == 'byte':
            self.newString = "byte "
            self.datatype()

    def datatype(self):
        self.i += 1
        if self.seperatedString[self.i]:
            self.newString = self.newString + self.seperatedString[self.i] + ' = '
            self.i += 1
            s = self.seperatedString[self.i]
            if s.isdigit():
                self.newString += str(s)

            elif s == "equalto":
                self.i += 1
                self.newString = self.newString + self.seperatedString[self.i]
        self.i = 0

        print(self.newString)
        return self.newString
