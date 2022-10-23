import random

class GuessTheNumber:
    
    def __init__(self):
        self.life = 5
        self.score = 0
    
   
    def mainGame(self):
        i=0
        while True:
            NumbertobeGuessed = random.randint(1000,25000)
            n=int(input("Guess a number between 1000 and 25000 :"))
            if(n == NumbertobeGuessed):
                self.ScoreIncrementar()
         
            else :
                self.LifeDecrementar()
                self.ScoreDecrementar()
            if (self.life ==0 or i==4):
                break
            i=i+1
        print("Score :", self.score)
        print("life :",self.life)
    def ScoreIncrementar(self):
        self.score = self.score + 100
    def ScoreDecrementar(self):
        self.score = self.score-10
    def LifeDecrementar(self):
        self.life =self.life-1
     

obj = GuessTheNumber()
obj.mainGame()
                
                
                
        
        
