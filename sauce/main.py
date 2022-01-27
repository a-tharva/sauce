import argparse


def initalise(ddg=False, wiki=False, img=False):
    
    
    if ddg:
        from search.ddg_search import duckduckgo
        duckduckgo(input('Search for: '))
    
    
    if wiki:
        from search.wiki_search import wiki
        wiki(input('Wikipedia: '))
    
    
    if img:
        from search.igm_search import search_that
        search_that(input('Image url: '), input('File name to store result: '))


def main():

    parser = argparse.ArgumentParser(description='Get answer for your question')
    
    parser.add_argument('-ddg', '--duck', help='Search answer on duckduckgo', 
                        action='store_true')
    parser.add_argument('-wiki', '--wiki', help='Wikipedia search', 
                        action='store_true')
    parser.add_argument('-img', '--image', help='Reverce image search', 
                        action='store_true')
    args = parser.parse_args()
    
    initalise(ddg=args.duck, wiki=args.wiki, img=args.image)
    
if __name__ == '__main__':
    main()