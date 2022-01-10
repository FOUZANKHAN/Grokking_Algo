from collections import deque
graph = {}
graph["you"] = ['Talha', 'Saif','Asif']
graph['Talha'] = ['Atif','Shami','Mehmood']
graph['Saif'] =['Ovais']
graph['Asif'] = ['Majid','Khaleel','Jabry']
graph['Atif'] = []
graph['Shami'] = []
graph['Mehmood'] = []
graph['Ovais'] = []
graph['Majid'] = []
graph['Khaleel'] = []
graph['Jabry'] = []

def seller(name):
    return name[-1] == 'y' 

def search(name):
    searchlist = deque()
    searchlist += graph[name]
    searched = []
    while searchlist:
        person = searchlist.popleft()
        if not person in searched:
            if seller(person):
                print( "Found the seller " + person)
                return True
            else:
                searchlist = graph[person]
                searchlist.append(person)


def search(name):
    search_list = deque() #create a queue
    search_list += graph[name] #add elements related to THAT particular name
    searched = [] #Unclear
    while search_list: #while elements present in search list
        person =  search_list.popleft() #pop the first element
        print(person) 
        if person not in searched: #if this person is not in searched
            if seller(person): #check for seller
                print( person + " Found seller")
                return True #made no sense
            else:
                search_list += graph[person]  #add the new person's neighbors to the queue
                searched.append(person)
                print(searched)



search('you')








