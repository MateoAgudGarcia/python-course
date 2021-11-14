def sentences_formatter(phrase):
    question_words = ('how','why','what','which','who', 'do')
    capitalized = phrase.capitalize()
    if phrase.startswith(question_words):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
def phrase_constructor():
    secret_stop = "\end"
    whole_text = []
    while True:
        phrase= input("Insert a sentence: ")
        if secret_stop in phrase:
            print(" ".join(whole_text))
            break
        else:
            whole_text.append(sentences_formatter(phrase))
    
phrase_constructor()
