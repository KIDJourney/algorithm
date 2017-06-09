class Tire:
    STOP_WORD = "#"
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        word = word + self.STOP_WORD
        tmp = self.root
        for ch in word:
            tmp.setdefault(ch, {})
            tmp = tmp[ch]
        
    def prefix(self, pre):
        tmp = self.root
        for ch in pre:
            if not ch in tmp:
                return False
            tmp = tmp[ch]
        return True
    
    def match(self, word):
        word = word + self.STOP_WORD
        tmp = self.root
        for ch in word:
            if not ch in tmp:
                return False
            tmp = tmp[ch]            
        return True
    
tire = Tire()
tire.insert('helloworld')
print(tire.root)
print(tire.prefix('hello'))
print(tire.match('helloworld'))