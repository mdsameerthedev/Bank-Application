# IMPORTING THE PACAKGES
import mysql.connector as sql

global accno

accno = None


# CLASS FOR DATABASE
class DataBase:
    def __init__(self,host,usname,psswd):
        self.holdername = None
        self.host = host
        self.usname = usname
        self.psswd = psswd
        self.conn = sql.connect(host=self.host,username=self.usname,password=self.psswd)
        self.cursor = self.conn.cursor()
        self.cursor.execute('use Bank')

    # METHOD TO ENSURE THE CONNECTION
    def is_connected(self):
        if self.conn.is_connected():
            print('Connected Successfully!')
        else:
            print('Connection Unsuccessful!')

    # METHOD TO ADD USER TO THE DATABASE
    def user_register(self,user_data):
        query = "insert into Account_Holders (`Account_Number`,`Holder's Name`,`Holder's Email`,`Holder's Address`,`Account's PIN`) values(%s,%s,%s,%s,%s)"
        check = 'select * from Account_Holders'
        self.cursor.execute(check)
        got = self.cursor.fetchall()
        if user_data not in got:
            self.cursor.execute(query,user_data)
            self.conn.commit()
            print()
            print('Registered Successfully!')
            return True
        else:
            raise Exception('Registration failed!')
            return False

    # METHOD TO GET USER DETAILS TO LOG IN INTO THEIR ACCOUNTS
    def get_user(self,username):
        query = "select `Account_Number`,`Account's PIN`,`Holder's Name` from Account_Holders where `Account_Number` = %s"
        self.cursor.execute(query,(username,))
        user = self.cursor.fetchall()
        self.holdername = user [0] [2].upper()
        self.conn.commit()
        return user [0] [0],user [0] [1]

    # METHOD TO GET DETAILS TO DISPLAY IT
    def get_details(self,username):
        query = "select * from Account_Holders where `Account_Number` = %s"
        self.cursor.execute(query,(username,))
        data = self.cursor.fetchall()
        return data

    # METHOD TO GET HOLDER'S NAME TO DISPLAY WELCOME MESSAGE
    def win_name(self):
        return self.holdername

    # METHOD TO ADD AMOUNT TO THE HOLDER'S ACCOUNT
    def addAmt(self,accno,amount):
        try:
            query = 'update Account_Holders set balance = balance + %s where Account_Number = %s'
            self.cursor.execute(query,(amount,accno))
            self.conn.commit()
            print('PAYMENT SUCCESSFULLY DEPOSITED!')
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    # METHOD TO WITHDRAW AMOUNT FROM THE HOLDER'S ACCOUNT
    def minusAmt(self,accno,amount):
        try:
            query = 'update Account_Holders set balance = balance - %s where Account_Number = %s'
            self.cursor.execute(query,(amount,accno))
            self.conn.commit()
            print('AMOUNT SUCCESSFULLY WITHDRAWN!')

            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    # METHOD TO TRANSFER THE AMOUNT FROM ONE'S ACCOUNT TO OTHER'S ACCOUNT
    def transferAmt(self,gaccno,raccno,amount):
        try:
            # Update balance for the source account (withdraw)
            query1 = 'update Account_Holders set balance = balance - %s where Account_Number = %s'
            self.cursor.execute(query1,(amount,gaccno))

            # Update balance for the destination account (deposit)
            query2 = 'update Account_Holders set balance = balance + %s where Account_Number = %s'
            self.cursor.execute(query2,(amount,raccno))
            self.conn.commit()
            print('AMOUNT TRANSFER COMPLETED!')
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


# CALLING THE DATABASE CONNECTION
db = DataBase(host='localhost',usname='root',psswd='root@123')
# CHECKING THE CONNECTION
db.is_connected()


# CLASS CONTAINING THE LOGIC FOR LOGIN SYSTEM
class UserAlgo:
    # METHOD FOR OPENING OF ACCOUNT
    @staticmethod
    def open_account(acc_no,holder_name,holder_email,holder_address,acc_pin):
        acc = (acc_no,holder_name,holder_email,holder_address,acc_pin)
        result = db.user_register(acc)

    # METHOD FOR LOGIN INTO THE ACCOUNT
    @staticmethod
    def login(acc_no,acc_pin):
        try:
            acc = (acc_no,acc_pin)
            result = acc [0]
            bin = db.get_user(result)
            print(bin)
            if bin [0] == acc_no and bin [1] == acc_pin:
                print('Success!')
                accno = acc_no
                return True
        except:
            return False


# CLASS FOR ARRANGING THE RAW DATA FROM THE USER SUITABLE TO LOGIN
class LoginUser:
    def __init__(self,username,passwrd):
        self.username = username
        self.password = passwrd

    def print_user(self):
        user = [self.username,self.password]
        return user


## CLASS FOR ARRANGING THE RAW DATA FROM THE USER SUITABLE TO OPEN ACCOUNT
class RegisterUser:
    def __init__(self,user):
        self.accno = user [0]
        self.name = user [1]
        self.email = user [2]
        self.pin = user [3]

    def print_user(self):
        user = (self.accno,self.name,self.email,self.pin)
        return user


# CLASS WHICH CONTAIN THE CODE TO DISPLAY THE MAIN MENU OF THE APPLICATION
class main:
    def __init__(self,accno):  # IN __init__ I HAVE ONLY CALLED THE ACCOUNT NO VARIABLE TO GET DEATILS
        self.accno = accno

    # METHOD SHOW THE MENUS
    def menu(self):
        self.details = db.get_details(self.accno)
        print(self.details)
        print('|$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|')
        print(f"VPS BANK WELCOME'S YOU {db.win_name()}")
        print('|$$$$$$$$| MAIN MENU |$$$$$$$$|')
        print('1.ACCOUNT DETAILS')
        print('2.ACCOUNT BALANCE')
        print('3.TRANSFER')
        print('4.WITHDRAW')
        print('5.DEPOSIT')
        print('X.LOGOUT')
        choice = input('Enter Your Choice: ')

        # IF-ELIF STATEMENTS FOR CHOOSING THE MENU
        if choice == '1':
            self._acc_det()

        elif choice == '2':
            db.get_details(accno)
            self._acc_bal()

        elif choice == '3':
            self._transfer()

        elif choice == '4':
            self._withdraw()

        elif choice == '5':
            self._deposit()

        elif choice == 'X' or choice == 'x':
            self._logout()

    # METHOD TO DISPLAY THE ACCOUNT DETAILS
    def _acc_det(self):
        print()
        print('|$$$$$$| ACCOUNT DETAILS |$$$$$$|')
        print()
        details = self.details
        print(f'NAME: {details [0] [2]}')
        print(f'ACCOUNT NO: {details [0] [1]}')
        print(f'E-MAIL: {details [0] [3]}')
        print(f'ADDRESS: {details [0] [4]}')
        print(f'TYPE: {details [0] [5]}')
        quiti = input()
        if quiti == '':
            self.menu()

    # METHOD TO DISPLAY THE ACCOUNT BALANCE
    def _acc_bal(self):
        print()
        print('|$$$$$$$$| ACCOUNT BALANCE |$$$$$$$$|')
        print()
        print(f'YOUR ACCOUNT BALANCE: {self.details [0] [7]}')
        choice = input()
        if choice == '':
            main(self.accno).menu()

    # METHOD TO SHOW PROMPTS FOR WITHDRAW
    def _withdraw(self):
        print()
        print('|$$$$$$$$$$| WITHDRAW |$$$$$$$$$$|')
        print()
        wdmount = int(input('AMOUNT: '))
        db.minusAmt(self.accno,wdmount)
        print()
        choice = input()
        if choice == '':
            main(self.accno).menu()

    # METHOD TO SHOW PROMPTS FOR DEPOSIT
    def _deposit(self):
        print()
        print('|$$$$$$$$$$| DEPOSIT |$$$$$$$$$$|')
        print()
        dmount = int(input('AMOUNT: '))
        db.addAmt(self.accno,dmount)
        print()
        choice = input()
        if choice == '':
            main(self.accno).menu()

    # METHOD TO SHOW PROMPTS FOR TRANSFER
    def _transfer(self):
        print()
        print('|$$$$$$$$$$| TRANSFER AMOUNT |$$$$$$$$$$|')
        print()
        raccno = input("RECIVER'S ACCOUNT NUMBER: ")
        amount = int(input('AMOUNT: '))
        db.transferAmt(accno,raccno,amount)
        choice = input()
        if choice == '':
            main(self.accno).menu()

    # METHOD FOR LOGING OUT OF THE ACCOUNT AND CLOSE THE ACCOUNT
    def _logout(self):
        choose().choice()


class OPEN:
    def __init__(self):
        print()
        print('|$$$$$$$$| OPEN ACCOUNT |$$$$$$$$|')
        self.accno = input('ACCOUNT NUMBER: ')
        self.name = input('NAME: ')
        self.email = input('E-MAIL: ')
        self.addres = input('ADDRESS: ')
        self.pin = int(input('PIN: '))
        us = [self.accno,self.name,self.email,self.addres,self.pin]

        UserAlgo().open_account(self.accno,self.name,self.email,self.addres,self.pin)
        print()

        LOGIN()


class LOGIN:
    def __init__(self):
        print()
        print('|$$$$$$$$| LOGIN |$$$$$$$$|')
        self.accno = input('ACCOUNT NUMBER: ')
        self.pin = input('ACCOUNT PIN: ')
        self.login()

    def login(self):
        try:
            res = UserAlgo.login(self.accno,self.pin)
            if res:
                print('LOGIN SUCCESS!')
                print()
                main(self.accno).menu()
            else:
                print('LOGIN FAILED. TRY AGAIN!')
                LOGIN()
        except ValueError:
            LOGIN()



class choose:
    def __init__(self):
        print('|$$$$$$$$$$$$$$$$$$$$| BANK APPLICATION |$$$$$$$$$$$$$$$$$$$$|')
        print('1. LOGIN')
        print('2. OPEN ACCOUNT')
        print('Q. QUIT')
        print()

    def choice(self):
            choice = input('Enter your choice : ')

            if choice == '1':
                LOGIN()
            elif choice == '2':
                OPEN()
            elif choice == 'q' or choice == 'Q':
                exit()
            else:
                self.choice()



choose().choice()
