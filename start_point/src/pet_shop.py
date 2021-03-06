# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]


def get_total_cash(shop_cash):
    return shop_cash["admin"]["total_cash"]


def add_or_remove_cash(shop_cash, add_cash):
    shop_cash["admin"]["total_cash"] += add_cash


def get_pets_sold(shop_cash):
    return shop_cash["admin"]["pets_sold"]


def increase_pets_sold(pet_sold, num_pets):
    pet_sold["admin"]["pets_sold"] += num_pets


def get_stock_count(store_pets):
    return len(store_pets["pets"])


def get_pets_by_breed(store_pets, name_breed):
    found_pet_by_breed = []
    # pets = store_pets["pets"]
    # for pet in pets:
    for pet in store_pets["pets"]:
        if pet["breed"] == name_breed:
            found_pet_by_breed.append(pet["breed"])
                #it's adding the name of the breed to the list
                #found_pet_by_breed.append(pet) -> this will add the dictionaries with the specific.
    return found_pet_by_breed


def find_pet_by_name(store_pets, name_pet):
    for pet in store_pets["pets"]:
        if pet["name"] == name_pet:
            return pet


def remove_pet_by_name(store_pets, name_pet):
    for pet in store_pets["pets"]:
        if pet["name"] == name_pet:
            store_pets["pets"].remove(pet)


def add_pet_to_stock(store_pets, new_pet):
    new_pet == {}
    store_pets["pets"].append(new_pet)
    

def get_customer_cash(list_customers):
    return list_customers["cash"]


def remove_customer_cash(list_customers, customer_cash):
    list_customers["cash"] -= customer_cash


def get_customer_pet_count(list_customers):
    return len(list_customers["pets"])


def add_pet_to_customer(name_customer, new_pet):
    return name_customer["pets"].append(new_pet)

def customer_can_afford_pet(name_customer, new_pet):
    if name_customer["cash"] >= new_pet["price"]:
        return True
    else: 
        return False


# def sell_pet_to_customer(store_pets, pet, name_customer):
#         # return name_customer["pets"].append(pet)
#         # store_pets["admin"]["pets_sold"] += 1
#         # name_customer["cash"] -= pet["price"]
#         # store_pets["admin"]["total_cash"] += pet["price"]