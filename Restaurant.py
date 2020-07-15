import pandas
class Restaurant(object):
    def __init__(self, name, address, phone):
        self.menuId = 0
        self.empId = 0
        self.name = name
        self.address = address
        self.phone = phone
        self.menuData = {'Name': {}, 'Price':{}, 'Spicy': {}, 'Quantity': {}, 'VegOrNonVeg': {}}
        self.employeeData = {'Name': {}, 'Phone':{}, 'Role': {}, 'Gender': {}}
    
    def getName(self):
        return(self.name)
    
    def getAddress(self):
        return(self.address)
    
    def getPhone(self):
        return(self.phone)
    
    def addMenuItem(self, name, price, spicyOrNot, qty, VegOrNonVeg):
        self.menuId = self.menuId + 1
        self.menuData['Name'][self.menuId] = name
        self.menuData['Price'][self.menuId] = price
        self.menuData['Spicy'][self.menuId] = spicyOrNot
        self.menuData['Quantity'][self.menuId] = qty
        self.menuData['VegOrNonVeg'][self.menuId] = VegOrNonVeg
    
    def removeMenuItem(self, menuId):
        self.menuData = pandas.DataFrame(self.menuData).drop(menuId, axis = 0).to_dict()
    
    def getMenuData(self):
        return(pandas.DataFrame(self.menuData))

    def getEmployeeData(self):
        return(pandas.DataFrame(self.employeeData))

    
    def addEmployee(self, name, phone, role, gender):
        self.empId = self.empId + 1
        self.employeeData['Name'][self.empId] = name
        self.employeeData['Phone'][self.empId] = phone
        self.employeeData['Role'][self.empId] = role
        self.employeeData['Gender'][self.empId] = gender
        
    def removeEmployee(self, empId):
        self.employeeData = pandas.DataFrame(self.employeeData).drop(empId, axis = 0).to_dict()
    
    
if __name__ == "__main__":
    rest = Restaurant(name = 'Hindustani Cuisine', address = '9 Parkwood Ct., Edison, NJ 00837', phone = '512-657-8678')
    rest.getName()
    rest.getAddress()
    rest.getPhone()
    rest.getMenuData()
    rest.getEmployeeData()

    rest.addMenuItem('Dal Makhani', 7, 'Yes', 2, 'Veg')
    rest.addMenuItem('Jalebi', 5, 'No', 4, 'Veg')
    rest.addMenuItem('Mango Lassi', 3, 'No', 1, 'Veg')
    rest.addMenuItem('Rice', 4, 'No', 2, 'Veg')
    rest.addMenuItem('Roti', 8, 'No', 1, 'Veg')
    rest.addMenuItem('Sabzi', 2, 'Yes', 2, 'Veg')
    rest.addMenuItem('Plain Dal', 10, 'No', 2, 'Veg')
    rest.addMenuItem('Achaar', 11, 'Yes', 4, 'Veg')
    rest.addMenuItem('Chicken Curry', 11, 'Yes', 2, 'NonVeg')
    rest.addMenuItem('Duck Soup', 11, 'Yes', 2, 'NonVeg')
    rest.addMenuItem('Mutton Kebab', 11, 'Yes', 2, 'NonVeg')

    rest.addEmployee(name = 'John', phone = '512-654-9089', role = 'Chef', gender = 'Male')
    rest.addEmployee(name = 'Peter', phone = '512-654-9089', role = 'Cook', gender = 'Male')
    rest.addEmployee(name = 'Roli', phone = '512-654-9089', role = 'Waitress', gender =  'Female')
    rest.addEmployee(name = 'Romi', phone = '512-654-9089', role = 'Waitress', gender =  'Female')
    rest.addEmployee(name = 'Michelle', phone = '512-654-9089', role = 'Waitress', gender =  'Female')
    rest.addEmployee(name = 'Julia', phone = '512-654-9089', role = 'Waitress', gender =  'Female')
    rest.addEmployee(name = 'Robert', phone = '512-654-9089', role = 'Cashier', gender =  'Male')
    rest.addEmployee(name = 'Mike', phone = '512-654-9089', role = 'Cleaner', gender =  'Male')


    rest.getEmployeeData()
    df = rest.getMenuData()
    df.plot.barh(x = 'Name', rot = 0) 
