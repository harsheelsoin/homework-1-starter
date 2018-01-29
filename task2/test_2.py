from io import open

def checkChar(fileName):
    file1 = open(fileName, encoding="utf-8")
    lineCount=0
    charCount=0
    for line in file1:
        line = line.strip()
        for character in line:
            charCount+=1
        lineCount+=1
    return charCount

def test_characterCount():
    result = checkChar('task2/input.txt')
    assert result==6