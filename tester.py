import AccountList
BankOfOC = AccountList.AccountList()
BankOfOC.add_user('justin', '5051 First St', 123456, 90001)
BankOfOC.add_user('joe', '5052 First St', 223456, 90002)
BankOfOC.add_user('john', '5053 First St', 323456, 90003)
BankOfOC.add_user('jared', '5054 First St', 423456, 90004)
BankOfOC.add_user('jessica', '5055 First St', 523456, 90005)
BankOfOC.add_user('justin', '5051 First St', 123456, 90001)
BankOfOC.add_user('jazlyn', '5056 First St', 623456, 90006)
BankOfOC.delete_user(3)
BankOfOC.add_user('jermaine', '5057 First St', 723456, 90007)
BankOfOC.delete_user(4)
BankOfOC.merge_accounts(1, 6)
BankOfOC.delete_user(5)
BankOfOC.add_user('Jen', '5051 First St', 123456, 90001)
BankOfOC.add_user('Doug', '5051 First St', 123456, 90001)
BankOfOC.add_user('Doug', '5051 First St', 123456, 90001)
BankOfOC.merge_accounts(4, 5)
BankOfOC.pay_user_to_user(1, 3, 90000)

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

print(BankOfOC.get_median_id())