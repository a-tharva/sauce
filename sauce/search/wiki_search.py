import wikipedia


def wiki(search_term):
    wikipage = wikipedia.summary(search_term, sentences=50)
    print(f'{wikipage}\n\n')