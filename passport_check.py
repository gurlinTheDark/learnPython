valid_passports = [
  {"pid": '234322', "name": 'Mark',"citizenship": 'USA', "valid_visas":['India', 'Australia']}, 
  {"pid": 'ret343', "name": 'Sandy',"citizenship": 'USA', "valid_visas":[]}, 
  {"pid": '5y212j', "name": 'John',"citizenship": 'UK', "valid_visas":['Pakistan', 'Thailand']}, 
  {"pid": 'h123813', "name": 'Jane',"citizenship": 'Thailand', "valid_visas":['India', 'Greece']}
]
while(1):
    opn = int(input("Please enter the option you want choose? 1) check valid visas on passports, 2) get passsport details "))
    p_id = input("Enter your passport id ")
    if opn == 1:
        is_id = False
        for i in valid_passports:
        	if p_id == i["pid"]:
        	    is_id = True
        	    print("Hey the valid visas on this passport are %s" %(i["valid_visas"]))
        if not is_id:    
    	    print("Hey your passport id is invalid")			
    elif opn == 2:
        for i in valid_passports:
    	    if p_id == i["pid"]:
    	        print("Your passport details are %s" % i)
    else:
        print("Sorry this option is invalid")
