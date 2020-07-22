# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:01:27 2020

@author: cruise
"""

class Story(object):
    def __init__(self, name, age, gender, grade, city, hobby, book, friendName, brotherOrSister):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.city = city
        self.book = book
        self.hobby = hobby
        self.friendName = friendName
        self.brotherOrSister = brotherOrSister
        

    def getPronoun(self):
        if(self.gender in ['boy', 'young man', 'man']):
            return('He')
    
        return('She')

    def writeStory(self):
        story = f"""{self.name} is a very nice {self.gender}. 
        {self.getPronoun()} lives in {self.city}. 
        {self.name}'s favorite activity is {self.hobby}. 
        {self.name}, who is {self.age} years old, is going to attend {self.grade} grade after the summer gets over. 
        {self.name}'s favorite book is {self.book}. 
        {self.name}'s best friend is {self.friendName}. 
        {self.name} has a sibling, and it is a {self.brotherOrSister}."""
    
        return(story)



if __name__ == '__main__':
    
    mystory = Story('Nandini', '10', 'girl', 
                       '5th', 'Edison', 'Fashion', 
                       'The Famous Five', 'Sami', 'brother')
    
    story = mystory.writeStory()
    #story = writeStory('Mayur', '5', 'boy', 'KG', 'Edison', 'blocks', 'KG Learning', 'Daksh', 'Sister')
    print(story)
