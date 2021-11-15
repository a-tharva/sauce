"""Main function for sauce

menu for sauce 
"""
import argparse
import search_functions as search


def main():
    parser = argparse.ArgumentParser(description='Get answer for your question')
    parser.add_argument('function',
                        nargs='?',
                        choices=['answer', 'image', 'wiki'],
                        help='answer for duckduckgo quick answer, image for google image search, wiki for wikipedia search'
                       )
    args = parser.parse_args()
    
    function = args.function
    
    # If there are no arguments passed
    if function is None:
        print('Choose search option')
    # For answer choice
    elif function == 'answer':
        search_for = input('>>Search for: ')
        search.duckduckgo(search_for)
    # For image choice
    elif function == 'image':
        # Img address
        url = input(">>Input the url for img search:")  
        # Search result will be stored in txt file
        filename = input(">>Name the file:")            
        search.search_that(url, filename)
    # For wiki choice
    elif function == 'wiki':
        wiki_search = input('>>Input wiki search tearm:')
        search.wiki(wiki_search)
    
if __name__ == '__main__':
    main()
    
    
    
    

    
    
    
    
    
# Old main function
'''
def main():
    print('\n\n                 welcome to sauce')
    print('\n              What do you want to search')
    while True:
        try:
            print("\n--Image  \n--Wiki \n--Company \n--Duck   Go DuckDuckGo it")
            choice = input('>').lower()
            if choice == 'image':
                url = input(">>Input the url for img search:")  #img address
                filename = input(">>Name the file:")            #search result will be stored in txt file
                sauce.search_that(url, filename)    
            elif choice == 'wiki':
                wiki_search = input('>>Input wiki search tearm:')
                sauce.wiki(wiki_search)
            elif choice == 'company':
                wiki_search = input('>>Input wiki company to search:')
                if 'company' not in wiki_search:
                    wiki_search = wiki_search + ' company'
                sauce.wiki(wiki_search)
            elif choice == 'duck':
                search_for = input('>>Search for: ')
                sauce.duckduckgo(search_for)
        # Keyboard interrupt ctrl+c        
        except KeyboardInterrupt:
            print('\nExit..')
            break
'''
