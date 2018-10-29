import csv
null = None
false = False
true = True
with open ('namepairs.csv','r') as oldp:
    reader = csv.reader(oldp)
    with open ('instagram.json','r') as js:
	with open ('findpairs.csv', 'w') as op:  
	    fieldname1 = ['ins','tw']
	    with open ('instagram.csv', 'w') as oi:
		fieldnames = ['ins', 'tw', 'text', 'location1','location2']
		with open ('instagram_suit.csv','w') as si:
		    writer1 = csv.DictWriter(op, fieldnames=fieldname1)
		    writer2 = csv.DictWriter(oi, fieldnames=fieldnames)
		    writer3 = csv.DictWriter(si, fieldnames=fieldnames)
       	    	    pair = {}
		    npair = {}
        	    for line in reader:
            	        tw,ins = line
		        ins = ins.lower()
		        tw = tw.lower()
            	        if pair.has_key(tw) == False:
                            pair[ins] = tw 
		#           print ins,tw
		    for line in js:
		        try:
		#           print line	
			    instagram = eval(line)
			    username = instagram[0]["doc"]["user"]["full_name"]
	#		    print username
			    username = username.lower()
	#		    print username
			    location1,location2 = instagram[0]["doc"]["coordinates"]["coordinates"]
			    city =  instagram[0]["doc"]["location"]
			    text = instagram[0]["doc"]["caption"]["text"]	
			   #print username
			    if location1 > -40:
				writer3.writerow({'ins': username, 'text': city , 'location1': location1, 'location2': location2})
			    if pair.has_key(username) == True:
			   #    print username
			        if npair.has_key(username) == False:
	#			    print username
				    npair[username] == pair[username]
				    print npair[username]
				    writer1.writerow({'ins': username, 'tw':  npair[username]})
				    writer2.writerow({'ins': username, 'tw':  npair[username], 'text': text , 'location1': location1, 'location2': location2})
		


		        except Exception as e:

               		    pass



