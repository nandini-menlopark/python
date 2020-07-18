# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:01:27 2020

@author: cruise
"""

def getPronoun(gender):
    if(gender in ['boy', 'young man', 'man']):
        return('He')
    
    return('She')



def writeStory(name, age, gender, grade, city, hobby, book, friendName, brotherOrSister):
    story = f"""{name} is a very nice {gender}. 
    {getPronoun(gender)} lives in {city}. 
    {name}'s favorite activity is {hobby}. 
    {name}, who is {age} years old, is going to attend {grade} grade after the summer gets over. 
    {name}'s favorite book is {book}. 
    {name}'s best friend is {friendName}. 
    {name} has a sibling, and it is a {brotherOrSister}."""
    
    return(story)



if __name__ == '__main__':
    story = writeStory('Nandini', '10', 'girl', 
                       '5th', 'Edison', 'Fashion', 
                       'The Famous Five', 'Sami', 'brother')
    #story = writeStory('Mayur', '5', 'boy', 'KG', 'Edison', 'blocks', 'KG Learning', 'Daksh', 'Sister')
    print(story)
