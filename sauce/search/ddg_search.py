import requests


def duckduckgo(search_for):
    response = requests.get(f'http://api.duckduckgo.com/?q={search_for}&format=json')
    response = response.json()
    # Print data
    print('Heading:',response['Heading'])
    print('Abstract:',response['Abstract'])
    print('Abstract source:',response['AbstractSource'])
    print('Abstract text:',response['AbstractText'])
    print('Definition:',response['Definition'])
    # No of related topics from result
    related_no = 2
    print('Related Topic:')
    for i in response['RelatedTopics']:
        if related_no <= 0:
            break
        print(i['Text'])
        related_no-=1