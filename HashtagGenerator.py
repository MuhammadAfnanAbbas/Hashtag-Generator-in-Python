
sentence = input()

def hashtag_Generator(sentence):
    if(len(sentence) == 0):
        print("Warning! You entered an empty String")
        return False
    else:
        hash= sentence.replace(" ", "")
        hashtag= '#'+hash
        print(hashtag)

hashtag_Generator(sentence)      