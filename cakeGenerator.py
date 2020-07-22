## Write a class with function that will generate an electronic cake
## function will take three argument: number of layers, material (any letter), and 
## a cherry letter

import numpy as np
from termcolor import colored 

class Cake(object):
    def __init__(self, layers, material, cherryletter):
        self.layers = layers
        self.material = material
        self.cherryletter = cherryletter
    
    def getLayer(self, layer):
        return(colored(f"""{''.join(np.repeat(' ', self.layers - layer))}""" + 
               f"""[{''.join(np.repeat(self.material, 2*layer - 1))}]""", 'cyan'))

    def getCherry(self):
        return(colored(f"""{''.join(np.repeat(' ', self.layers))}""" + 
                       f"""{colored(self.cherryletter)}""", 'yellow'))


    def getCake(self):
        cake = self.getCherry()
        for i in range(1, self.layers + 1):
            cake = f"""{cake}\n{self.getLayer(i)}"""
    
        return(cake)
   


cakeFactory = Cake(layers = 10, material = "w", cherryletter = 'V')

print(cakeFactory.getCake())


print(colored('Nandini', 'yellow'))
