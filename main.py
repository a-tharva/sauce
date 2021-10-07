"""Main function for sauce

menu for sauce 
"""

import sauce

def main():

    print('\n\n  welcome to sauce')
    
    #img address
    url = input(">>Input the url for img search:")
    
    #search result will be stored in txt file
    filename = input(">>Name the file:")
    
    #function call
    sauce.search_that(url, filename)
    
if __name__ == '__main__':
    main()
    
