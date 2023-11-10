# installed library mysql-connector-python
import mysql.connector


#creating connection
class insert:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",
            password='root',
            database="bank"
        )
    #create cursor
    def personal_details(self,cid,fname,lname,addr,phn,adn,pan):
        cur=self.connection.cursor()
        cur.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{addr}',{phn},'{adn}','{pan}')") # inserting data in personal_details table
        self.connection.commit() # after inserting the data we need to commit changes
        print('----------personal details saved-----------')

    def bank_details(self,acco,cid,ifsc,actype):
        cur=self.connection.cursor()
        cur.execute(f"insert into bank_details values({acco},{cid},'{ifsc}','{actype}')")
        self.connection.commit()
        print('----------details are saved--------')

    def transaction_details(self,tranid,senderacc,reviveracc,amount,methon):
        cur=self.connection.cursor()
        cur.execute(f"insert into transaction_details values({tranid},{senderacc},{reviveracc},{amount},'{methon}')")
        self.connection.commit()
        print('-------transaction have entered--------')

    def account_details(self,acco,tranid,amount,closbala):
        cur=self.connection.cursor()
        cur.execute(f"insert into account_details values({acco},{tranid},{amount},{closbala})")
        self.connection.commit()
        print('-----details are saved--------')