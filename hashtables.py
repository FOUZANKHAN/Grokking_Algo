#using hashtable for lookups
phonebook = dict()
phonebook["Ryan Reynolds"] = 7868897711
phonebook["Jessica Alba"] = 8566693251
phonebook["Elizabeth"] = 85556937441
print (phonebook["Ryan Reynolds"])

#using hashtable for duplicates
voters = dict()
def checkvoters(name):
    if voters.get(name):
        print("Kick them out")
    else:
        voters[name] = True
        print("Let them vote")

checkvoters("Mike")
checkvoters("Peyter")
checkvoters("Peyter")
print(voters)

#using for caching