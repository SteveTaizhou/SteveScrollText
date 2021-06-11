class TooLongTextError(Exception):
    pass


class scrolledText:
    def __init__(self, text, long, add=1):
        self.text = text
        self.long = long
        self.start = 0
        self.end = long
        self.add = add
        if long > len(text):
            raise TooLongTextError("The text is too short")

    def __next__(self):
        start = self.start
        end = self.end
        text = self.text + self.text
        back = text[start:end]
        self.end += self.add
        self.start += self.add
        if self.start >= len(self.text):
            self.start -= len(self.text)
            self.end -= len(self.text)
        return back

    def __iter__(self):
        return self

if __name__ == "__main__":
    import os,time
    a=scrolledText("Steve made史帝夫制造  ",8)
    for t in iter(a):
        os.system("cls")
        print(t)
        time.sleep(1)
        
