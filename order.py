from .items import Items

class Order:
    def __init__(self, status, firstname, surname, email, phone, items, total_cost):
        self.status = status
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.items = items
        self.total_cost = total_cost
    
    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Items: {}, Total Cost: {}\n" 
        str =str.format( self.status,self.firstname,self.surname, self.email, self.phone, self.items, self.total_cost)
        return str
