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

issuers = []
while (1):
    roll_no = int(input("Enter your roll no "))
    if any(i["Roll_No"]==roll_no for i in issuers):
        print("Sorry you have already issued a book, please return the issued book before reissuing a new book")
    else:
        print("This is the list of books")
        for i in library:
            print("id = %d, Name = %s, Quantity = %d" %(i["id"],i["Name"],i["Quantity"]))
        book_to_issue = int(input("Please select the id of book you want to issue "))
        is_book_found = False
        for i in library:
            if i["id"] == book_to_issue:
                print("The book chosen by you is %s" %(i["Name"]))
                is_book_found = True
                if i["Quantity"] > 0:
                    i["Quantity"] = i["Quantity"] - 1
                    issuers.append({"Roll_No": roll_no, "id": book_to_issue,"Name": i["Name"] })
                else:
                    print("Sorry the book selected by is not available, please try next time")
                
        if not is_book_found:
            print("Sorry this is an invalid id, please select from the above list again")
    print("Thank you and visit again")
