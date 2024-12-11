import mysql.connector as myl
from colorama import init, Fore, Back, Style
from tabulate import tabulate
from termcolor import colored

# Initialize colorama
init(autoreset=True)

# Database connection
mydb = myl.MySQLConnection(host="localhost", user="root", passwd = "tiger", database="test")

mycursor = mydb.cursor()

# Create table if not exists
cr = ("""CREATE TABLE IF NOT EXISTS customer2bz (
    rno INTEGER(10),
    ccname CHAR(50),
    phoneno DECIMAL(10,0),
    pickuplocation CHAR(100),
    wheretolocation CHAR(20),
    tenure INTEGER(3),
    numberoftravellers INTEGER(200),
    modeoftransportation CHAR(55),
    modeofpayment CHAR(50)
);""")
mycursor.execute(cr)

# Main program loop
ch = "y"
lst = 0
m = " "
mop = 0
print(Fore.GREEN + "WELCOME")

while ch == "y" or ch == "Y":
    print(Fore.RED + "1. REGISTER for your trip ")
    print(Fore.RED + "2. REVISIT the details to rectify")
    print(Fore.RED + "3. INVALIDATE or scrap your trip ")
    print(Fore.WHITE + "")
    a = int(input("Specify your desired options -"))

    if a == 1:
        # Registration logic
        print(Fore.YELLOW + "")
        name = input("enter your NAME- ")
        ph = int(input("enter your PHONE NUMBER- "))
        initial = input("enter your RESIDENTIAL ADDRESS- ")
        final = input("enter your LANDING PLACE- ")
        time = int(input("enter NUMBER OF DAYS OF STAY- "))
        num = int(input("enter NUMBER OF PEOPLE ON TRIP- "))
        print(Fore.BLACK + "")
        print(Back.GREEN + "CHOOSE YOUR CONVENIENT MODE OF PAYMENT- ")
        print(Back.BLACK + "")
        print(Fore.BLUE + "1. credit card")
        print(Fore.BLUE + "2. PAYTM")
        print(Fore.BLUE + "3. UPI")
        print(Fore.BLUE + "4. debit card")
        mop = int(input("enter your favourable mode of payment number-"))

        if mop == 1:
            m = "creditcard"
            ccn = input("enter credit card number-")
            while len(ccn) != 16:
                print(Fore.WHITE + "")
                print("ERROR FOUND!!!! TYPE YOUR CREDIT CARD NUMBER AGAIN")
                ccn = input("enter your CREDIT CARD NUMBER -")
            cvv = input("enter your CVV -")
            while len(cvv) != 3:
                print(Fore.WHITE + "")
                print("ERROR FOUND! TYPE YOUR CVV NUMBER AGAIN")
                cvv = input("enter your CVV -")
            exp = input("enter EXPIRATION OF CREDIT CARD")
            while len(exp) != 4:
                print(Fore.WHITE + "")
                print("ERROR FOUND! TYPE YOUR EXPIRATION OF CREDIT CARD AGAIN")
                exp = input("enter EXPIRATION OF CREDIT CARD -")

        elif mop == 2:
            m = "paytm"
            paytmno = input("enter your PAYTM NUMBER- ")
            while len(paytmno) != 10:
                print("ERROR FOUND! type your paytm number again")
                paytmno = input("enter your PAYTM NUMBER- ")

        elif mop == 3:
            m = "UPI"
            upino = input("enter your UPI NUMBER- ")
            while len(upino) != 10:
                print(Fore.CYAN + "ERROR FOUND! enter your UPI number again")
                upino = input("enter your UPI NUMBER- ")

        elif mop == 4:
            m = "debitcard"
            ccn = input("enter DEBIT CARD NUMBER- ")
            while len(ccn) != 16:
                print(Fore.CYAN + "ERROR FOUND!!!! TYPE YOUR DEBIT CARD NUMBER AGAIN")
                ccn = input("enter DEBIT CARD NUMBER- ")
            cvv = input("enter your CVV NUMBER- ")
            while len(cvv) != 3:
                print("ERROR FOUND! type your cvv number again")
                cvv = input("enter your CVV NUMBER- ")
            exp = input("enter EXPIRATION OF DEBIT CARD -")
            while len(exp) != 4:
                print("ERROR FOUND! type your Expiration of debit card again")
                exp = input("enter EXPIRATION OF DEBIT CARD- ")

        print(Style.RESET_ALL)
        print(" CHOOSE MODE OF TRANSPORTATION- ")
        print("1. by air (money according to ticket)")
        print("2. by road")
        tr = int(input("Specify your choice "))
        transport = " "
        mon = 0

        if tr == 1:
            transport = "by air"
            print("Your departing dates will be notified earliest in a week ")
        elif tr == 2:
            print("1. car (Rs 8,000 per day)")
            print("2. bus")
            rt = int(input("enter your choice"))
            if rt == 1:
                transport = "car"
                print("1. Celerio (Rs 8,000 per day)")
                print("2. Innova (Rs 10,000 per day)")
                print("3. Fortuner (Rs 10,600 per day)")
                print("4. Swift Dzire (Rs 1,000)")
                print("5. XUV (Rs 13,000)")
                cars = 0
                while cars not in [1, 2, 3, 4, 5]:
                    cars = int(input("Select from them (1, 2, 3, 4, 5)"))
                if cars == 1:
                    mon = 8000
                elif cars == 2:
                    mon = 10000
                elif cars == 3:
                    mon = 10600
                elif cars == 4:
                    mon = 1000
                elif cars == 5:
                    mon = 13000
                else:
                    print("Wrong input")
            elif rt == 2:
                transport = "bus"
                print("1. Mini")
                print("2. Deluxe")
                bus = int(input("enter your choice"))
                if bus == 1:
                    mon = 15000
                    transport = "by road (mini bus)"
                elif bus == 2:
                    mon = 20000
                    transport = "by road (deluxe bus)"

        tg = input("Do you need a tour guide? (Rs 8,000 per day): ")

        print(Fore.WHITE + "")
        print("AVAILABLE HOTELS")
        print("1: 3 star")
        print("2: 5 star")
        print("3: 7 star")
        hotm = 0
        hot = 0
        while hot not in [1, 2, 3]:
            hot = int(input("Choose among 1, 2, 3: "))
            if hot == 1:
                hotm = 4000
                break
            elif hot == 2:
                hotm = 7000
                break
            elif hot == 3:
                hotm = 10000
                break
            else:
                print("Wrong input")

        hotmt = hotm * time
        mycursor.execute("SELECT * FROM customer2bz")
        data = mycursor.fetchall()

        for i in data:
            if i[0] > lst:
                lst = i[0]

        lst += 1
        print("YOUR REFERENCE CODE IS - ", lst)
        print("*************************")
        print("*************************")
        print("TOUR AND TRAVELS")
        print(Fore.CYAN + "CUSTOMER NAME:", name)
        print(Fore.CYAN + "PHONE NUMBER:", ph)
        print(Fore.CYAN + "MODE OF PAYMENT:", m)
        print(Fore.CYAN + "NUMBER OF PEOPLE:", num)
        print(Fore.CYAN + "FROM:", initial, "TO:", final)

        if tg.lower() == "yes":
            tgm = 8000
        else:
            tgm = 0

        print(Fore.CYAN + "HOTEL CHARGES:", hotmt)
        if mon == 0:
            print(Fore.CYAN + "TRANSPORTATION CHARGES: Will be according to tickets")
        else:
            print(Fore.CYAN + "TRANSPORTATION CHARGES:", mon)
            total_sum = hotmt + mon + tgm
            half1 = total_sum / 2
            print(Fore.WHITE + "")
            print("TOTAL MONEY:", total_sum)
            print("PAID:", half1)
            print("DUE:", half1)
            print(Fore.CYAN + "REFERENCE CODE NUMBER:", lst)

        print(Back.BLACK + "")
        print(Fore.RESET + "")
        print("*************************")
        print("*************************")

        # Insert customer data into the database
        r = (lst, name, ph, initial, final, time, transport, m, num)
        add1 = """INSERT INTO customer2bz(rno, ccname, phoneno, pickuplocation, wheretolocation, tenure,
            modeoftransportation, modeofpayment, numberoftravellers)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        mycursor.execute(add1, r)
        mydb.commit()

    elif a == 2:
        # Rectify details logic
        print(Fore.WHITE + "")
        rno1 = int(input("Enter your REFERENCE CODE- "))
        print("You can rectify the following details:")
        print("1. Name")
        print("2. Phone Number")
        print("3. Address")
        print("4. Destination")
        print("5. Tenure")
        print("6. Number of People")
        print("Which detail do you want to rectify?")

        doubt = input("Enter the detail to rectify (name, phone number, address, etc.): ").lower()

        if doubt == "name":
            new_name = input("Enter the new name: ")
            u1 = "UPDATE customer2bz SET ccname = %s WHERE rno = %s"
            mycursor.execute(u1, (new_name, rno1))
            print("Name updated!!!")
            mydb.commit()
        elif doubt == "phone number":
            new_phone = input("Enter the new phone number: ")
            u1 = "UPDATE customer2bz SET phoneno = %s WHERE rno = %s"
            mycursor.execute(u1, (new_phone, rno1))
            print("Phone number updated!!!")
            mydb.commit()
        elif doubt == "address":
            new_address = input("Enter the new address: ")
            u1 = "UPDATE customer2bz SET pickuplocation = %s WHERE rno = %s"
            mycursor.execute(u1, (new_address, rno1))
            print("Address updated!!!")
            mydb.commit()
        elif doubt == "destination":
            new_destination = input("Enter the new destination: ")
            u1 = "UPDATE customer2bz SET wheretolocation = %s WHERE rno = %s"
            mycursor.execute(u1, (new_destination, rno1))
            print("Destination updated!!!")
            mydb.commit()
        elif doubt == "tenure":
            new_tenure = int(input("Enter the new tenure: "))
            u1 = "UPDATE customer2bz SET tenure = %s WHERE rno = %s"
            mycursor.execute(u1, (new_tenure, rno1))
            print("Tenure updated!!!")
            mydb.commit()
        elif doubt == "number of people":
            new_people = int(input("Enter the new number of people: "))
            u1 = "UPDATE customer2bz SET numberoftravellers = %s WHERE rno = %s"
            mycursor.execute(u1, (new_people, rno1))
            print("Number of people updated!!!")
            mydb.commit()
        else:
            print("Invalid input! Please ensure you typed the correct option.")

    elif a == 3:
        # Delete record logic
        print(Fore.WHITE + "")
        number = int(input("Enter your Reference Code: "))
        query = "DELETE FROM customer2bz WHERE rno = %s"
        mycursor.execute(query, (number,))
        mydb.commit()
        print("Record deleted successfully!")

    else:
        print("Wrong input! Press 'y' to continue.")
        ch = input("DO YOU WANT TO CONTINUE? (y/n): ").lower()
