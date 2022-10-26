library = [{
	"id": 1,
	"Name": "Amar Chitra Katha",
	"Quantity": 3
}, {
	"id": 2,
	"Name": "Ravana",
	"Quantity": 2
}, {
	"id": 3,
	"Name": "Laxman",
	"Quantity": 4
}]
while (1):
    roll_no = int(input("Enter your roll no "))
    print("This is the list of books")
    for i in library:
        print("id = %d, Name = %s, Quantity = %d" %(i["id"],i["Name"],i["Quantity"]))
    book_to_issue = int(input("Please select the id of book you want to issue "))
    for i in library:
        if i["id"] == book_to_issue:
            print("The book chosen by you is %s" %(i["Name"]))
    #else:
        #print("Sorry this is an invalid id, please select from the above list again")
            if i["Quantity"] > 0:
                i["Quantity"] = i["Quantity"] - 1
            else:
                print("Sorry the book selected by is not available, please try next time")
    print("Thank you and visit again")
