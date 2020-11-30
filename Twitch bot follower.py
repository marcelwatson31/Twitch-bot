import random,csv
import pandas as pd

generator_values = 'abcdefghijklmnopqrstuvwxyz'
generator_phone_number_values = "0123456789"
generator_birth_day_values = []
generator_birth_month_values = []
generator_birth_year_values = []

def birth_generator():
    for days in range(29):
        generator_birth_day_values.append(days)
    for months in range(13):
        generator_birth_month_values.append(months)
    for years in range(1950,2000):
        generator_birth_year_values.append(years)
birth_generator()



random_range_for_k_value = None
email_end = None
dummy_generator_for_credentials = None
seperator = ""
dummy_names = None
dummy_email = None
dummy_phone_number = None


dummy_rand_birthmonth = None
dummy_rand_birthday =None

dummy_rand_birthyear = None
dummy_birthday = None

dummy_first = None
dummy_last = None
dummy_password = None 


class User:
    def __init__(self,first_name, last_name, username, password, email_address, birth_day, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email_address = email_address
        self.birth_day = birth_day
        self.phone_number = phone_number

        def __repr__(self):
            return str(self)


#Problem is trying to get objects back and creating a loop of them

'''bot_dictionary_list = [User(dummy_names,dummy_names,dummy_names,dummy_names,dummy_email,dummy_birthday,dummy_phone_number) for i in range(0, 10)]

print(bot_dictionary_list[1])
bot = User(dummy_names,dummy_names,dummy_names,dummy_names,dummy_email,dummy_birthday,dummy_phone_number)
x = 0
for x in range(10):
    bot = User(dummy_names,dummy_names,dummy_names,dummy_names,dummy_email,dummy_birthday,dummy_phone_number)

print(bot.username)'''





'''a_dictionary = {}
for number in range(1,4):
    a_dictionary["Bot%s" % number] = "abc", dummy_names, dummy_names, dummy_names

print(a_dictionary)'''
bot_num = []
bot_user = []
bot_firstname = []
bot_lastname = []
bot_email = []
bot_phone = []
bot_password = []
bot_birthday = []

bot_dict={}
for number in range(1,5):
    random_range_for_k_value = random.randint(9, 17)
    email_end = "@aol.com"
    dummy_generator_for_credentials = random.choices(generator_values, k=random_range_for_k_value)
    seperator = ""
    dummy_names = seperator.join(dummy_generator_for_credentials)
    dummy_password = dummy_names
    dummy_email = dummy_names+email_end
    dummy_phone_number =  seperator.join(random.choices(generator_phone_number_values, k=10))

    dummy_rand_birthmonth = str(random.choice(generator_birth_month_values))
    dummy_rand_birthday = str(random.choice(generator_birth_day_values))

    dummy_rand_birthyear = str(random.choice(generator_birth_year_values))
    dummy_birthday = (seperator.join(dummy_rand_birthday+dummy_rand_birthmonth+dummy_rand_birthyear))
    dummy_first_un = random.choices(generator_values, k=random_range_for_k_value)
    dummy_last_un = random.choices(generator_values, k=random_range_for_k_value)
    dummy_password_un = random.choices(generator_values, k=random_range_for_k_value)

    dummy_first_fil = seperator.join(dummy_first_un)
    dummy_last_fil = seperator.join(dummy_last_un)
    dummy_password_fil = seperator.join(dummy_password_un)

    bot_dict = {"Bot numbers" : number, "Username":f"{dummy_names}", "Password": f"{dummy_password_fil}", "Last Name":f"{dummy_last_fil}", "First Name":f"{dummy_first_fil}", "Email Address": f"{dummy_email}", "Birth day":f"{dummy_birthday}", "Phone Number":f"{dummy_phone_number}"}
    

    bot_user.append(dummy_names)
    bot_num.append(number)
    bot_firstname.append(dummy_first_fil)
    bot_lastname.append(dummy_last_fil)
    bot_birthday.append(dummy_birthday)
    bot_password.append(dummy_password_fil)
    bot_phone.append(dummy_phone_number)
    bot_email.append(dummy_email)

    bot_dict.update({'Bot numbers' : bot_num, "Username": bot_user, 'Password': bot_password, 'Last Name': bot_lastname, "First Name": bot_firstname, "Email Address": bot_email, "Birth day": bot_birthday, "Phone Number": bot_phone})



    
    #Next step is to group dictornary elements together by position [0] and make the in a zip() list together 
    #then pass them to a CSV file to write the dummy data in corresponding rows
print(bot_dict)


'''with open('dict.csv', 'w') as csv_file:  
    
    
    for key, value in bot_dict.items():
        writer.writerow([key, value])
       
with open('dict.csv') as csv_file:
    reader = csv.reader(csv_file)'''


a_file = open("twitchbot.csv", "w")



writer = csv.DictWriter(f=a_file,fieldnames=["Bot Number", "Username","Password", "Last Name", "First Name", "Email","Birthday", "Phone"])

writer.writeheader()
writer = csv.writer(a_file)
for key, value in bot_dict.items():
    writer.writerow([key])
    writer.writerows([key,value])
    
    



a_file.close()













        

