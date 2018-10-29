import csv
null = None
false = False
true = True
with open('dictionary_hotspot.csv','r') as dh:
    with open('matching_testre.csv','r') as mt:
	with open('predict.csv', 'w') as op:
	    dich = {}
	    dicm = {} 
	    reader1 = csv.reader(dh)
	    reader2 = csv.reader(mt)
            fieldnames = ['ins',  'location1','location2','tw1','tw2','tw3']
	    writer1 = csv.DictWriter(op, fieldnames=fieldnames)
	    for line in reader1:
                tw,location1,location2 = line
                if dich.has_key(tw) == False:
                    dich[tw] = [[location1,location2]]
                else:
                    dich[tw].append([location1,location2])
#                print len(dich)
	    count =0.0
	    count0 = 0.0
            tot = 0.0
	    for line in reader2:
		ins,tw0,text0,location10,location20 = line 
               # if dicm.has_key(tw) == False:
                dicm[tw0] = [[location10,location20]]
               # else:
                  #  dicm[tw0].append([location10,location20])
	     #   print len(dicm)
	    for key in dicm:
                tw1 = key
                el0 = dicm[key]
                for i in range(0,len(el0)):
		    la0,lo0 = el0[i]
		    if dich.has_key(tw1) == True:
                        distance1 = 0.00501 
                        distance2 = 0.003001 
                        distance3 = 0.003 
		        tot = tot+1
		#	print tot
		        matchname1 = None
		        matchname2 = None
		        matchname3 = None
	                for key in dich:
			#print tw1
			    el = dich[key]
		#	print el
                            for i in range(0,len(el)):
			        lo,la = el[i]
			   # print lo
		                distancetest = abs(float(la) - float(la0))+abs(float(lo) - float(lo0))
			       # print distancetest
			        if distancetest < distance1:
				    diatance1 = distancetest
				    matchname3 = key
				    if distance3 < distance2:
                                        diatancetest = distance3 
				        distance3 = distance2
				        distance2 = distancetest		
                                        m = matchname3
					matchname3 = matchname2
					matchname2 = m
					if distance2 < distance1:
                                            diatancetest = distance2
                                            distance2 = distance1
                                            distance1 = distancetest
                                            m = matchname2
                                            matchname2 = matchname1
                                            matchname1 = m

		        writer1.writerow({'ins': tw1, 'location1': lo0, 'location2': la0,'tw1' : matchname1,'tw2' : matchname2,'tw3' : matchname3}) 
			j = cmp(tw1,matchname1) 
			k = cmp(tw1,matchname2) 
			l = cmp(tw1,matchname3) 
		        if j == 0:
		            count = count +1	
                        else:
			    if k == 0:
                                count = count +1
                            else:
				 if l == 0:
                            	    count = count +1
                        if matchname1 is None and matchname2 is None and matchname3 is None:
			    a=0
			else:
                            count0 = count0 +1
	    print "total massage"
            print tot 
	    print "accuracy="
            print (count/tot)
	    print "accuracy_without_null="
            print (count/count0) 
