from letter_state import LetterState
class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
       self.secret: str = secret.upper()
       self.attempts = []
       self.color = [] 
    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
    def guess(self, word: str):
        word = word.upper()
        result = []
        letcolor = []
        usedletters = []
        for i in range(self.WORD_LENGTH):
            character = word[i]
            
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character in self.secret[i]
            letter.is_in_word_twice = character in usedletters
            if letter.is_in_position:
                usedletters.append(character)
                letcolor.append("Green")
            elif letter.is_in_word and not letter.is_in_position and not letter.is_in_word_twice:
                usedletters.append(character)
                letcolor.append("Orange")
            else:
                letcolor.append("LightSteelBlue4")
            result.append(letter)
        self.color.append(letcolor)
        return result
    
    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
        

    @property    
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved