class TV:
    def __init__(self):
        self.päällä = False
        self.kanava = 1
        self.ääni = 0

    def painaNappia(self):
        self.päällä = not self.päällä

    def kanavaYlos(self):
        if self.päällä == True:
            if self.kanava < 2:
                self.kanava += 1

    def kanavaAlas(self):
        if self.päällä == True:
            if self.kanava > 1:
                self.kanava -= 1

    def ääniYlos(self):
        if self.päällä == True:
            if self.ääni < 5:
                self.ääni += 1

    def ääniAlas(self):
        if self.päällä == True:
            if self.ääni > 0:
                self.ääni -= 1