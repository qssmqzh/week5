class Home:
    def __init__(self,loc,color):
        self.loc=loc
        self.color=color
    def show_info(self):
        print(f"House located: {self.loc}, and is {self.color} color")
        
home1 = Home("dossor","blue")
home2 = Home("Atyrau","green")

home1.show_info()
home2.show_info()