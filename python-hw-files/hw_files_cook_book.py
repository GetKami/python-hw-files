dishes = {}
with open("cook_book.txt") as f:
    for line in f:
        recept = line.strip()
        ingredients_number = f.readline().strip()
        ingredients_list = []
        ingredients_dict = {}
        for lines in range(int(ingredients_number)):
            ingredient = f.readline().strip().split(" | ")
            ingredients_dict["ingredient_name"] = ingredient[0]
            ingredients_dict["quantity"] = ingredient[1]
            ingredients_dict["measure"] = ingredient[2]
            ingredients_list.append(ingredients_dict.copy())
            dishes[recept] = ingredients_list
        f.readline()
    print (dishes, "\n")

print ("Список продуктов:")
def get_shop_list_by_dishes(all_dishes, person_count):
    product_list = {}
    for dish in all_dishes:
        if dish in dishes:
          for i in dishes[recept]:
            dish_number = i["ingredient_name"]
            product_list[dish_number] = {"measure": i["measure"], "quantity": int(i["quantity"]) * person_count}
    print(product_list)

get_shop_list_by_dishes(["Фахитос", "Утка по-пекински"], 3)