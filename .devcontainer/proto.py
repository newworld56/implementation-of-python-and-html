import fully


def intro():
     
     name  = str(input("What is your name?: "))
     age = int(input("How old are you?: "))
     #where = input("What are you up to today?: ")
     print("Hello ",name," thanks for chosing us!, how come you are turning ",age+1)
     print(""" 
               1.care
               2.food
               3.hotel
               4.atm
               5.entertainment
               6.home
               7.work
               8.school """)
     selection = input("please select an option of your choice?: ")
     #selection.save([])
     if selection == "care": 
          print(""""care has been selected:
                     1.lahnam hospital
                     2. lahnam pharmacy
                     """)
          print("The options are","lahnam_pharmacy","and","lahnam_hospital")
          fully.care()
     elif selection == "food":
          print(""""food has been selected:
                     1.burger
                     2. pizza
                     3.chicken
                     4.ice cream
                     """)
          print("The options are burger_1,pizza_2,chicken_3,ice_cream_4")
          fully.food()
     elif selection == "hotel":
          print(""""hotel has been selected:
                     1.marriott
                     2.metro point
                     3.stay bridge suits
                     """)
          print("The options are being calculated ../")
          fully.hotels()
     elif selection == "atm":
          print(""""atm has been selected:
                     1.bank of america
                     2. city bank
                     3. capital one
                     """)
          print("The options are bank_of_america,city_bank, and capital_one")
          fully.atm()
     elif selection == "entertainment":
          print(""""entertainment has been selected:
                     1.museum
                     2.cinema
                     3. park
                     4.store
                     """)
          print("The options are museum,cinema,park,store ")
          fully.entertainment
     elif selection == "home":
          print("calculating house")
          fully.home()
          
     elif selection =="work":
          print("calculating work")
          fully.work()

     elif selection == "school":
          print("calculating school")
          fully.school()
     else:
          
          return "your choice is not in our options"







     
     







     










   