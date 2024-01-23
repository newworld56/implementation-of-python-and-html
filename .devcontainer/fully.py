
def care():
    lahnam_pharmacy = {"pharmacy_lahnam": [38.9763367139673, -76.84633706392094]}
    lahnam_hospital =  {"hospital" : [38.99341791355472, -76.83585532498573]}
    care_option = input("Enter option?: ")
    if care_option == "lahnam_pharmacy":
        print(lahnam_pharmacy)
    elif care_option == "lahnam_hospital":
        print(lahnam_hospital)
    

def food():
    burger_1 ={"mcdonals":[ 38.99127813678243, -76.82297682387052],"burger_king"  : [38.99328843930225, -76.85594727945355],"wendys":[38.967127889910415, -76.84719862734983]}
    #mcdonals = 
    pizza_2 = {"pizza_hut":[38.96405965683579, -76.85543887048078],"little_caesar" :[38.96726079000406, -76.84462368514454], "dominos":[38.98571335386769, -76.84552582292122] }

    chicken_3 = {"kfc":[38.99958424159445, -76.8310764189335], "chick_fill_a" : [38.96433697021441, -76.8256383624257],"popey":[38.96010425278661, -76.87577666821684] }

    ice_cream_4 = {"baskin_robins" :[38.98296280171231, -76.77270429673653],"coldstone_creamery" :[38.98296280171231, -76.77270429673653],"sweetfrog" : [38.92644323069435, -76.84491986283884]}
    food_option1 = input("Enter option?: ")
    if food_option1 == "burger_1":
        print("The options for burger are mcdonals,burger_king,wendys")
        print(burger_1)
    elif food_option1 == "pizza_2":
        print("For pizza the options are pizza_hut,dominos,little_caesar")
        print(pizza_2)
    elif food_option1 == "chicken_3":
        print("for chicken the options are kfc,chick_fill_a, and popey")
        print(chicken_3)
    elif food_option1 == "ice_cream_4":
        print("For ice cream the options are baskin_robins,sweetfrog,coldstone_creamery")
        print(ice_cream_4)


def hotels(room):
    room = {"marriott": [38.99883253335523, -76.95337604152616],"metro_point":[38.97103140320565, -76.8744441119544],"staybridge_suits" :[38.99719638794863, -76.83241485504377]}
    print(room)
def atm():
    atm = {"bank_of_america" : [38.974123191741555, -76.84609170833552],"city_bank" : [38.97416343417292, -76.84520979493679],"capital_one" : [38.95705063433509, -76.82297662782256]}
    print(atm)
def entertainment():
    museum = {"nasa_m":[38.99523404438928, -76.84750580278325],"aviation":[38.98148577930689, -76.92179106326404],"american_history":[38.89428023946104, -77.02961956284994]}
    cinema = {"land_mark":[38.8981983152081, -77.02777793775905],"amc":[38.90462391155985, -77.06246586477553],"alamon_cinema":[38.930052979689684, -76.9979808240611]}
    park = {"riverdale_park":[38.97129455639388, -76.92649005336953],"capital_park":[38.974516179477476, -76.91679895512905],"goodluck_community_center":[38.982025883545525, -76.86051956106806]}
    store = {"beltway_plaz":[39.00465359023599, -76.90986750539751],"seabrook_station":[38.97806826657087, -76.84714517398268],"eastgate_centre":[38.99942007886587, -76.82175178527072]}
#{:[],:[],:[]}
    entertainment_option = input("Enter option?: ")
    if entertainment_option == "museum":
        print("The options of museum are the americaan history,aviation, and nasa ")
        print(museum)
    elif entertainment_option == "cinema":
        print("For cinema the options are land mark,amc, and alamon cinema")
        print(cinema)
    elif entertainment_option == "park":
        print("for parks the options are riverdale,goodluck comminity center,and capital park")
        print(park)
    elif entertainment_option == "store":
        print("For stores the best options are seabrook station,beltway plaza, and eastgate centre")
        print(store)
    
def home():
    house = {"home": [39.002752461145825, -76.87626352856076]}
    print("your house is at point")
    print(house, "please copy this")


def work():
    job = {"amazon":[38.98718334933465, -76.86919542427974]}
    print(job, "please copy this")
def school():
    study = {"duval_high" : [39.00893171990677, -76.83578943964497]}
    print(study, "please copy this")
