def verify_card_number(card_number):
    clean_card_number_list = []
    for i in card_number:
        if i.isdigit():
            clean_card_number_list.append(int(i))
    inverted_clean_card_number_list = clean_card_number_list[::-1]
    n = len(inverted_clean_card_number_list)
    for index in range(1,n):
        if index % 2:
            inverted_clean_card_number_list[index] *= 2
            if inverted_clean_card_number_list[index] > 9:
                inverted_clean_card_number_list[index] -= 9
    sum_all_numbers = sum(inverted_clean_card_number_list)

    if sum_all_numbers % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

#e.g. of usage:
card_number = "453914881"
print(verify_card_number(card_number))
