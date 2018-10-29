import csv
#null = None
#false = False
#true = Ture
with open('twwettext.csv', 'r') as csvfile:
    with open('matching_train.csv', 'w') as trainfile:
	fieldname1 = ['ins', 'tw', 'text','location1','location2']
	with open('matching_testre.csv', 'w') as testrefile:
    	    fieldname2 = ['ins', 'tw', 'text','location1','location2']
    	    with open('matching_test.csv', 'w') as testfile:
                fieldname3 = ['ins', 'text','location1','location2']
	        le =[]
	        reader = csv.reader(csvfile) 
                writer1 = csv.DictWriter(trainfile, fieldnames=fieldname1)
	        writer2 = csv.DictWriter(testrefile,fieldnames=fieldname2)  
	        writer3 = csv.DictWriter(testfile,fieldnames=fieldname3)  
	        for line in reader:
	            ins,tw,text,location1,location2 = line
                #print ins
		    if ins not in le:
		        le.append(ins)
		        writer2.writerow({'ins': ins, 'tw': tw, 'text': text,'location1':location1,'location2':location2}) 
		        writer3.writerow({'ins': ins, 'text': text,'location1':location1,'location2':location2}) 
		    else:
	                writer1.writerow({'ins': ins, 'tw': tw, 'text': text,'location1':location1,'location2':location2})
