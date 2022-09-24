import AccountList
BankOfOC = AccountList.AccountList()
BankOfOC.__add_user__('justin', '5051 First St', 123456, 90001)
BankOfOC.__add_user__('joe', '5052 First St', 223456, 90002)
BankOfOC.__add_user__('john', '5053 First St', 323456, 90003)
BankOfOC.__add_user__('jared', '5054 First St', 423456, 90004)
BankOfOC.__add_user__('jessica', '5055 First St', 523456, 90005)
BankOfOC.__add_user__('justin', '5051 First St', 123456, 90001)
BankOfOC.__add_user__('jazlyn', '5056 First St', 623456, 90006)
BankOfOC.__delete_user__(3)
BankOfOC.__add_user__('jermaine', '5057 First St', 723456, 90007)
BankOfOC.__delete_user__(4)
BankOfOC.__merge_accounts__(1, 6)
BankOfOC.__delete_user__(5)
BankOfOC.__add_user__('Jen', '5051 First St', 123456, 90001)
BankOfOC.__add_user__('Doug', '5051 First St', 123456, 90001)
BankOfOC.__add_user__('Doug', '5051 First St', 123456, 90001)
BankOfOC.__merge_accounts__(4, 5)
BankOfOC.__pay_user_to_user__(1, 3, 90000)

# debug print
currNode = BankOfOC._head 
for x in range(BankOfOC.__len__()):
    print('unique ID: ', currNode._uniqueID)
    print('name: ', currNode._element._name)
    print('address: ', currNode._element._address)
    print('SSN: ', currNode._element._socialSecurity)
    print('balance: ', currNode._element._balance)
    print('\n')
    currNode = currNode._next

print(BankOfOC.__get_median_id__())