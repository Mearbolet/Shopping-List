def whatever(my_str):
    """This function receives a string as it's parameter,
    representing a shopping list separated by commas and no spaces,
    and according to an input by the user (numbers 1-9), does
    something for each input.
    Unless 9 is the chosen input, the function loops back and requests another input.
    :param my_str: the string input by the user
    :type my_str: str
    :return: the function doesn't return a value as it always loops back."""

    shopping_list = my_str.split(",")
    chosen_number = 0
    while chosen_number != 9:
        chosen_number = int(input("Please enter a number between 1 and 9: "))

        if chosen_number == 1:
            print(shopping_list)

        elif chosen_number == 2:
            print(len(shopping_list))

        elif chosen_number == 3:
            product = input("Is this product on the list? : ")
            if product in shopping_list:
                print(True)
            else:
                print(False)

        elif chosen_number == 4:
            product = input("How many times does your item appear on your list? : ")
            count = 0
            for item in shopping_list:
                if item == product:
                    count = count + 1
            print(str(product) + " appears " + str(count) + " times in your list")

        elif chosen_number == 5:
            product_to_delete = input("Please enter a product to delete from your list: ")
            shopping_list.remove(product_to_delete)
            print(shopping_list)

        elif chosen_number == 6:
            product_to_add = input("Please enter a product to add to your list: ")
            shopping_list.append(product_to_add)
            print(shopping_list)

        elif chosen_number == 7:
            bad_items = []
            for item in shopping_list:
                if len(item) < 3:
                    bad_items.append(item)
                    print(bad_items)

                elif item.isalpha():
                    continue
                else:
                    bad_items.append(item)
                    print(bad_items)

        elif chosen_number == 8:
            no_dupes_list = []
            for item in shopping_list:
                if item not in no_dupes_list:
                    no_dupes_list.append(item)
            print(no_dupes_list)

        if chosen_number == 9:
            return ("Exiting the program")



def main():
    whatever()
    if __name__ == "__main__":
        main()


print(whatever("Milk,Cottage,Tomatoes,Carrots,Milk,$$$$"))