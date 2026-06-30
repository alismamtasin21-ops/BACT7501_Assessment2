class requisitionsystem:
    def __init__(self):
        self.requisition_s = []
        self.counter = 10000
    
    def addrequisition(self):
        print("+++++++++ Add Requisition +++++++++")
        date = input("Date : ")
        stuff_id = input(" Stuff Id  : ")
        stuff_name = input("Stuff Name : ") 
        self,counter += 1 
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
            item.append(item)
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
        self.requisitions.append(requisition)
        print("\nRequisition add sucess")
        print("Requisition ID:", requisition_id)
        print("Total($): ", total)
        print("Status:", status)
        print("Approval Reference Number:", approval_ref)
    def approveRequisition(self, total, stuff_id, requisition_id):
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
                    if req_number >= 1 and req_number <= len(self.requisitions):
                        selected_requisition = self.requisitions[req_number - 1]
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
                


