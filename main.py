"""Main function for sauce

menu for sauce 
"""
import sauce


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
    
    
    
if __name__ == '__main__':
    main()