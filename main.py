"""Main function for sauce

menu for sauce 
"""

import sauce

def main():

    print('\n\n  welcome to sauce')
    print('\n What do you want to search')
    
    while True:
        try:
            
            print("--Image  \n--Wiki \n--Company")
            choice = input('>').lower()
            
            if choice == 'image':
                #img address
                url = input(">>Input the url for img search:")

                #search result will be stored in txt file
                filename = input(">>Name the file:")

                #function call
                sauce.search_that(url, filename)
                
            elif choice == 'wiki':
                
                wiki = input('>>Input wiki search tearm:')
                sauce.wiki_that(wiki)
                
            elif choice == 'company':
                
                wiki = input('>>Input wiki company to search:')
                
                if 'company' not in wiki:
                    wiki = wiki + ' company'
                sauce.wiki_that(wiki)
            
        except KeyboardInterrupt:
            break
    
if __name__ == '__main__':
    main()
    
