from .category import Category

class itmes:
    def __init__(self, name, description, image, price, category,):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.category = category
    
    def get_items_details(self):
        return str(self)

    def __repr__(self):
        str = "Name: {}, Description: {}, Image: {}, Price: {}, Category: {}\n" 
        str =str.format( self.name,self.description,self.image, self.price, self.category,)
        return str