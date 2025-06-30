menu={
    'Pizza':180,
    'Chicken Tikka':200,
    'French Fries':100,
    'Butter Chicken': 250,
    'Paneer Butter Masala': 220,
    'Veg Biryani': 180,
    'Chicken Biryani': 240,
    'Cold Drink': 40,
    'Masala Chai': 30,
    'Coffee': 50
}
print("WELCOME TO THE RESTAURANT")
for key,value in menu.items():
    print(f"{key} Rs.{value}")
menu_lower={key.lower():value for key,value in menu.items()}
order_total=0
while True:
    food1=input("What items do you want to order?").lower()
    if(food1 in menu_lower):
        print("The item is:",food1)
        order_total=order_total+menu_lower[food1]
    else:
        print("The item is not present in the menu.Please order another items listed in the menu.")
    another_order=input("Do you want to order another item?(Yes/No):")
    if another_order.strip().lower() != "yes":
        break;
print("THANK YOU")
print("Total bill is:",order_total)