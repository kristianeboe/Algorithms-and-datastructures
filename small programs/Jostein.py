def old_key_to_new_key(old_key): #Funksjonen som transformerer hexakoden til RCO
    old_key = old_key[0:9] #Fjerner 0ene
    temp_list = [] #Setter opp variable
    new_key = ""
    for i in range(0,len(old_key)-1,2): #Lager en templiste
        temp_list.append(str(old_key[i])+str(old_key[i+1]))
    for j in range(len(temp_list)): #Reverserer lisa manuelt, .reverse() fungerte ikke?
        new_key += str(temp_list.pop())
    i = int(new_key, 16) #Omgjør fra hexa til deci
    new_key = str(i)
    return new_key[1:] #Fjerner det første tallet


old_keys = [] #Setter opp liste som skal leses til
with open("jostein1.txt","r") as openfileobject:
    for line in openfileobject: #Leser inn hexakoder fra fil
        old_keys.append(str(line))

output = open("output.txt", "w")
for old_key in old_keys:
    output.write(str(old_key_to_new_key(old_key))+"\n") #Skriver til fil
