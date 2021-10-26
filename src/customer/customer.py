import uuid
import customer_cmd
import repository

class Customer:

    def __init__(self,cmd:customer_cmd) -> None:
        self.customer_id = None      
        self.create_id()

        customer_name = cmd.customer_name
        address = cmd.address
        email = cmd.email

        if not self.empty_check(customer_name):
            raise Exception('customer name is None')
        self.customer_name = customer_name

        if not self.empty_check(address):
            raise Exception('customer address is None')
        self.address = address

        if not self.empty_check(email):
            raise Exception('customer email is None')
        self.email = email
    
    def create_id(self):
        if self.customer_id is None:
            self.customer_id = str(uuid.uuid4())
    
    def get_id(self):
        return self.customer_id

    def change_info(self,cmd:customer_cmd) -> None:

        customer_name = cmd.customer_name
        address = cmd.address
        email = cmd.email

        if not self.empty_check(customer_name):
            raise Exception('customer name is None')
        self.customer_name = customer_name

        if not self.empty_check(address):
            raise Exception('customer address is None')
        self.address = address

        if not self.empty_check(email):
            raise Exception('customer address is None')
        self.email = email
    
    def empty_check(self,value:str) -> bool:
        if value is None or value == '':
            return False
        return True