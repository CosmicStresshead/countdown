import random, time

class Game:
    
  def __init__(self, *args, **kwargs) -> None:
   ...


  def load_dictionary(self, *args, **kwargs) -> dict:
    ''' Returns a dict object containing words from the prepared dictionary.
        Dictionary keys are word lengths. '''
    ...


  def generate_letter(self, vowel:bool=False, *args, **kwargs) -> str:
    ''' Returns a random selection from either vowels or consonants. '''
    ...

  def match_guess(self, letters:str, word:str, *args, **kwargs) -> bool:
    ''' Returns true if the word can be made using the letters. '''
    ...

  def dictionary_lookup(self, candidate:str, *args, **kwargs) -> bool:
    ''' Simply checks for the presence of a word in the dictionary. '''
    ...

  def draw_number(self, large:bool=True, *args, **kwargs) -> int:
    ''' Draws one number from the specified deck. '''
    ...

  def generate_calculation(self, numbers:list[int], *args, **kwargs) -> tuple[str, int]:
    ''' Calculates an integer from a list of numbers, via randomised
        arithmetic operations.  Returns a 2-tuple containing an evaluable
        statement string and its integer solution. '''
    ...

  def numbers_selection(self, *args, **kwargs) -> None:
    ...

  def start_clock(self):  
    ...

  def numbers_round(self, *args, **kwargs) -> None:
    ...
    
  
  def valid_eval(n:int|float, *args, **kwargs) -> bool:
    ...
    
