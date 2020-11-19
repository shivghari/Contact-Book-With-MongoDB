from pymongo import MongoClient

myclient = MongoClient('localhost',27017)
mydb = myclient['ContactBook']
mycol = mydb['ContactBook']

def AddContact():
    name = input('Enter Contact Name : ')
    address = input('Enter Contact Address : ')
    mobile = input('Enter Contact Mobile-No : ')
    email = input('Enter Contact Email : ')
    info = input('Enter Contact Bio : ')
    dict1 = {
        'name' : name,
        'address' : address,
        'mobile' : mobile,
        'email' : email,
        'info' : info
        }
    mycol.insert_one(dict1)

def FindContact():
    name = input('Enter Contact Name To Find : ')
    qry = {'name' : name}
    result = mycol.find(qry)
    for i in result:
        print(i)

def UpdateContact():
    name = input('Entre Contact Name To Update : ')
    qry = {'name' : name}
    result = mycol.find(qry)
    for i in result:
        print(i)
    print('This Contact IS Now In Process OF Updating.....')
    mycol.delete_one(qry)
    
    name = input('Enter Contact Name To Update : ')
    address = input('Enter Contact Address To Update : ')
    mobile = input('Enter Contact Mobile-No To Update : ')
    email = input('Enter Contact Email To Update : ')
    info = input('Enter Contact Bio To Update : ')
    dict1 = {
        'name' : name,
        'address' : address,
        'mobile' : mobile,
        'email' : email,
        'info' : info
        }
    mycol.insert_one(dict1)
    print('Contact Successfully Updated.....')

def DeleteContact():
    name = input('Enter the Contact Name To be Deleted : ')
    qry = {'name' : name}
    check = input('Do you Want To delete contact ...? (Y/N)')
    if check == 'y' or check == 'Y':
        mycol.delete_one(qry)
        print('Contact Successfully Deleted....')
    else:
        print('Contact is Safe...!')

def ShowAllContact():
    for i in mycol.find({},{"_id":0}):
        print(i)
        
choise = 0
while choise != 6:
    print('--------------------------')
    print('CONTACT BOOK MANAGER')
    print('--------------------------')
    print('1. Add Contact')
    print('2. Find Contact')
    print('3. Update Contact')
    print('4. Show All Contact')
    print('5. Delete Contact')
    print('6. Exit Phone Book')
    print('--------------------------')
    
    choise = int(input('Enter Choise : '))

    if choise == 1:
        AddContact()
    elif choise == 2:
        FindContact()
    elif choise == 3:
        UpdateContact()
    elif choise == 4:
        ShowAllContact()
    elif choise == 5:
        DeleteContact()
    elif choise == 6:
        print('Visit Again...!')
    else:
        print('Entre Valid Choise...!')
    
    

    
    
    
    
