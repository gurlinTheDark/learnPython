valid_passports = [
  {"pid": '234322', "name": 'Mark',"citizenship": 'USA', "valid_visas":['India', 'Australia']}, 
  {"pid": 'ret343', "name": 'Sandy',"citizenship": 'USA', "valid_visas":[]}, 
  {"pid": '5y212j', "name": 'John',"citizenship": 'UK', "valid_visas":['Pakistan', 'Thailand']}, 
  {"pid": 'h123813', "name": 'Jane',"citizenship": 'Thailand', "valid_visas":['India', 'Greece']}
]
admin_credentials = {
    "username": "admin",
    "password":"admin"
}
while(1):
    opn = int(input("Please enter the option you want choose? 1) check valid visas on passports, 2) get passsport details 3) Print all passports ids from the given country, 4) Add new Passport details(Only for Admin) 5) Delete a passport record(Only for Admin)"))
    if opn == 1:
        p_id = input("Enter your passport id ")
        is_id = False
        for i in valid_passports:
        	if p_id == i["pid"]:
        	    is_id = True
        	    print("Hey the valid visas on this passport are %s" %(i["valid_visas"]))
        if not is_id:    
    	    print("Hey your passport id is invalid")			
    elif opn == 2:
        p_id = input("Enter your passport id ")
        for i in valid_passports:
    	    if p_id == i["pid"]:
    	        print("Your passport details are %s" % i)
    elif opn == 3:
        country = input("Enter the country")
        citizens_passport_ids = [];
        for i in valid_passports:
            if country == i["citizenship"]:
                citizens_passport_ids.append(i["pid"])
        print("The passport ids belonging to %s are %s" %(country, citizens_passport_ids))
    elif opn ==4 or opn ==5:
        username=input("Enter Admin username");
        if(username == admin_credentials["username"]):
            password = input("Enter Admin Password")
            if(password ==admin_credentials["password"] ):
                if opn ==4:
                    data= input("Enter the new passport id, name, citizenship and valid visas")
                    data = data.split(",") 
                    valid_passports.append({
                        "pid": data[0],
                        "name": data[1],
                        "citizenship": data[2],
                        "valid_visas": data[3:]
                    })
                    print(valid_passports)
                else:
                    id= input("Enter the pid to be deleted")
                    is_id = False
                    for i in valid_passports:
                        if(id == i["pid"]):
                            is_id = True
                            valid_passports.remove(i)
                            print("The record belonging to %s is deleted" %id)
                            print(valid_passports)
                    if not is_id:
                        print("there is no record for this Id")
            else:
                print("Sorry, wrong credentials")
        else:
            print("Sorry, wrong credentials")
    else:
        print("Sorry this option is invalid")
