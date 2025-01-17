from models.owner import Owner
from models.shoe import Shoe

# lib/helpers.py


def exit_program():
    print("Goodbye!")
    exit()

def create_owner():
    name = input("Enter owner name: ")
    try:
        owner = Owner.create(name)
        print(f'Success: {owner}')
    except Exception as exc:
        print("Error creating owner: ", exc)
        
def list_owners():
    return Owner.get_all()
    # owners = Owner.get_all()
    # for owner in owners:
    #     print(owner) 
    # return Shoe.get_all() # Creates shoe table

def update_owner(id_):
    if owner := Owner.find_by_id(id_):
        try:
            name = input("Enter owner's new name: ")
            owner.name = name

            owner.update()
            #print(f'Success: {owner}')
        except Exception as exc:
            print("Error updating owner: ", exc)
    else:
        print(f'Owner {id_} not found')

def delete_owner(id_):
    if owner := Owner.find_by_id(id_):
        owner.delete()
        #print(f'Owner {id_} deleted')
    else:
        print(f'Owner {id_} not found')


def find_owner_by_id(id_):
    owner = Owner.find_by_id(id_)
    return(owner) if owner else print(f'Owner {id_} not found')

def create_shoe(owner_id):
    print("")
    for shoe in Shoe.shoe_brands:
        print(shoe)
    print("")

    brand = input("Enter a brand from above: ").title()
    while brand not in Shoe.shoe_brands:
        brand = input("Brand entered not in list above. Try again: ").title() 

    size = input("Enter the shoe size: ")
    while size == type(str):
        try:
            int(size)
        except:
                size = input("Shoe size entered was not a number. Try again: ")
    Shoe.get_all() #Creates the table if not yet created
    try:
        shoe = Shoe.create(brand, size, owner_id)
        # print(f'Success: {shoe}')
    except Exception as exc:
        print("Error creating shoe: ", exc)


def list_shoes():
    shoes = Shoe.get_all()
    for shoe in shoes:
        print(shoe) 

def update_shoe(owner):
    shoe_number = input("Enter the shoe's number: ")
    shoe_id = owner.shoes()[int(shoe_number) -1].id
    if shoe := Shoe.find_by_id(shoe_id):
        try:
            print("")
            for brand in Shoe.shoe_brands:
                print(brand)
            print("")
            new_brand = input("Enter the new shoe brand: ")
            shoe.brand = new_brand
            size = input("Enter the new shoe size: ")
            shoe.size = int(size)
            # owner_id = input("Enter the shoe's owner id: ")
            # shoe.type = owner_id

            shoe.update()
            # print(f'Success: {shoe}')
        except Exception as exc:
            print("Error updating shoe: ", exc)

def delete_shoe(owner):
    shoe_number = input("Enter the shoe number: ")
    id_ = owner.shoes()[int(shoe_number) -1].id
    if shoe := Shoe.find_by_id(id_):
        shoe.delete()
        print(f'Shoe {id_} deleted')
    else:
        print(f'Shoe {id_} not found')

def list_shoes_by_owner_id(owner_id):
    owner = Owner.find_by_id(owner_id)
    if owner:
        return owner.shoes()