import sauce

#img address
url = input("Input the url for img search:")
#search result will be stored in txt file
filename = input("Name the file:")
sauce.search_that(url, filename)