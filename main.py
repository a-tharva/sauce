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
                wiki = input('>>Input wiki search tearm:')
                sauce.wiki_that(wiki)
                
            
            elif choice == 'company':
                wiki = input('>>Input wiki company to search:')
                
                if 'company' not in wiki:
                    wiki = wiki + ' company'
                
                sauce.wiki_that(wiki)
            
            
            elif choice == 'duck':
                search_for = input('>>Search for: ')
                sauce.duckduckgo(search_for)
                
            
        except KeyboardInterrupt:
            print('\nExit..')
            break
    
    
    
if __name__ == '__main__':
    main()