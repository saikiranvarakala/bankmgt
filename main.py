from create import insert
from read import read
from update import update
from delete import delete
objdelete=delete()
obj=insert()
objread=read()
objupdate=update()

print('------------------bank manegement system------------')
print('for inserting the data press 1 :')
print('for read the data press 2 :')
print('for update the data press 3 :')
print('for deleting the data press 4 :')

opr=int(input('please enter your operation :'))
def myopr():
    print('-------for personal  informatin press 1-----')
    print('-------for bank details press 2-----')
    print('-------for transaction details press 3-----')
    print('-------for  bank details press 4-----')
    vr=int(input('please select your table :'))
    if vr==1:
        return 'personal_details'
    elif vr==2:
        return 'bank_details'
    elif vr==3:
        return 'transaction_details'
    elif vr==4:
        return 'account_details'
def cn():
    print('-----------customerid is 1----')
    print('----------transactionid is 2----')
    vh=int(input('please enter which id :'))
    if vh==1:
        return 'customerID'
    if vh==2:
        return 'transactionID'
if opr==1:
    h=myopr()
    if h=='personal_details':
        cid=int(input('please input customer id'))                                                                                
        fname=input('please input first name')
        lname=input('please input last name')
        addr=input('please input address')
        phn=int(input('please phone number'))                                                                                
        adn=input('please input addhar number')                                                                                
        pan=input('please input pan nubmer')

        obj.personal_details(cid,fname,lname,addr,phn,adn,pan)
    elif h=='bank_details':
        acco=int(input('please input account number'))
        cid=int(input('please input customerid'))
        ifsc=input('please input ifsc')
        actype=input('please input account type')
        obj.bank_details(acco,cid,ifsc,actype)
    elif h=='transaction_details':
        tranid=int(input('please input transationid'))
        senderacc=int(input('please input sender account number'))
        receiveracc=int(input('please input reviver account number'))
        amount=int(input('please input amount'))
        method=input('please input method')
        obj.transaction_details(tranid,senderacc,receiveracc,amount,method)
    elif h=='account_details':
        acco=int(input('please input account number'))
        tranid=int(input('please input transationid'))
        amount=int(input('please input amount'))
        closbala=int(input('please input bala'))
        obj.account_details(acco,tranid,amount,closbala)

if opr==2:
    j=myopr()
    column_id=cn()
    id=int(input('please input id for fetcing details :'))
    objread.specific_info(id,j,column_id)

if opr==3:
    k=myopr()
    id=input('please input id')
    new_value=input('please input newvalues')
    column_name=input('please input colunm name')
    column_id=cn()
    objupdate.myupdate(k,column_name,new_value,id,column_id)

if opr==4:
    q=myopr()
    column_id=cn()
    id=input('please input id')
    objdelete.data_delete(q,column_id,id)