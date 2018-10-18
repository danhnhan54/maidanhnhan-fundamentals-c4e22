def get_even_list(checking_lists):
    new_lists = []
    for i in range (len(checking_lists)):
        if checking_lists[i]%2 == 0:
            new_lists.append(checking_lists[i])
    return new_lists