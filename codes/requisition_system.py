class requisitionsystem:
    def __init__(self):
        self.requisition = []
        self.counter = 10000
    
    def addrequisition(self):
        print("+++++++++ Add Requisition +++++++++")
        date = input("Date : ")
        stuff_id = input(" Stuff Id  : ")
        stuff_name = input("Stuff Name : ") 
        self.counter += 1 
        requisition_id = self.counter 


        items = []
        total = 0

        print("Add Items: ")

        while True:
            item_name = input("Item Name: ")
            item_price = float(input("Price($):"))
            item = {
                "item_name": item_name,
                "item_price": item_price
            }
            items.append(item)
            total += item_price
            more = input("Add Another Item (yes/no): ")
            if more.lower() == "no":
                break
        status, approval_ref = self.approverequisition(total, stuff_id, requisition_id)
        requisition = {
            "date": date,
            "staff_id": stuff_id,
            "staff_name": stuff_name,
            "requisition_id": requisition_id,
            "items": items,
            "total": total,
            "status": status,
            "approval_ref": approval_ref
        }
        self.requisition.append(requisition)
        print("\nRequisition add sucess")
        print("Requisition ID:", requisition_id)
        print("Total($): ", total)
        print("Status:", status)
        print("Approval Reference Number:", approval_ref)
    def approverequisition(self, total, stuff_id, requisition_id):
        status = "Pending"
        approval_ref = "Not available"
        if total < 500:
            status = "Approved"
            approval_ref = stuff_id + str(requisition_id)[-3:]
        return status, approval_ref
    def respondRequisition(self):
        if len(self.requisition) == 0:
            print("Requisition dont founded")
        else:
            print("\n======= PENDING REQUISITIONS =======")
            found = False
            for index, requisition in enumerate(self.requisition):
                if requisition["status"] == "Pending":
                    found = True
                    print(index + 1, "| Requisition ID:", requisition["requisition_id"], "| Staff Name:", requisition["staff_name"], "| Total: $", requisition["total"])
            if found == False:
                print("No pending requisitions available.")
            else:
                choice = input("Enter requisition number to respond: ")
                if choice.isdigit():
                    req_number = int(choice)
                    if req_number >= 1 and req_number <= len(self.requisition):
                        selected_requisition = self.requisition[req_number - 1]
                        if selected_requisition["status"] == "Pending":
                            print("1. Approved")
                            print("2. Not approved")
                            print("3. Leave as Pending")
                            response = input("Enter your response: ")
                            if response == "1":
                                selected_requisition["status"] = "Approved"
                                selected_requisition["approval_ref"] = selected_requisition["staff_id"] + str(selected_requisition["requisition_id"])[-3:]
                                print("Requixition approv successfull.")
                            elif response == "2":
                                selected_requisition["status"] = "Not approved"
                                selected_requisition["approval_ref"] = "Not available"
                                print("Requisition not approv.")
                            elif response == "3":
                                print("Requisition pending.")
                            else:
                                print("No response.")
                        else:
                            print("This requisition not pending.")
                    else:
                        print("Invalid requisition number")
                else:
                    print("Invalid input. Please enter right number.")
    def displayRequisitions(self):
        if len(self.requisition) == 0:
            print("No requisitions found.")
        else:
            print("\n========== PRINTING REQUISITIONS ==========")
            for requisition in self.requisition:
                print("Date:", requisition["date"])
                print("Requisition ID:", requisition["requisition_id"])
                print("Staff ID:", requisition["staff_id"])
                print("Staff Name:", requisition["staff_name"])
                print("Total: $", requisition["total"])
                print("Status:", requisition["status"])
                print("Approval Reference Number:", requisition["approval_ref"])
                print("=====================================")
    def requisitionStatistics(self):
        total_submitted = len(self.requisition)
        total_approved = 0
        total_pending = 0
        total_not_approved = 0
        for requisition in self.requisition:
            if requisition["status"] == "Approved":
                total_approved += 1
            elif requisition["status"] == "Pending":
                total_pending += 1
            elif requisition["status"] == "Not approved":
                total_not_approved += 1            
        print("\n========== REQUISITION STATISTICS ==========")
        print("The total number of requisitions submitted:", total_submitted)
        print("The total number of approved requisitions:", total_approved)
        print("The total number of pending requisitions:", total_pending)
        print("The total number of not approved requisitions:", total_not_approved)
    def displayMenu(self):
        print("\n========== REQUISITION SYSTEM MENU ==========")
        print("1. Add Requisition")
        print("2. Respond to Pending Requisition")
        print("3. Display Requisitions")
        print("4. Display Statistics")
        print("0. Exit")
    def run(self):
        while True:
            self.displayMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addrequisition()
            elif choice == "2":
                self.respondRequisition()
            elif choice == "3":
                self.displayRequisitions()
            elif choice == "4":
                self.requisitionStatistics()
            elif choice == "0":
                print("Thank you for using the Requisition System.")
                break
            else:
                print("Invalid choice. Please choose from 0 to 5.")


system = requisitionsystem()
system.run()    

