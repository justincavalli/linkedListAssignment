Consider a commercial bank, Bank of Orange County where anyone can open bank accounts. To open a bank account the following information is needed: 

- Name 
- Address
- Social Security
- An initial deposit amount. 

Whenever a user opens up an account, the bank assigns a unique ID. The unique ID is assigned to new users in an incremental manner, meaning if the last new user’s ID is x, the user who is currently signing up will have a unique ID (x + 1). If a user closes their account, the unique ID can be re-claimed and will be re-assigned to future new users. 

Now, write a class for the Bank of Orange County with the following features:

- Model the list of users as a linked list where each account is a node in the list. Users must be sorted by their ID in the linked list. [2 pt]
- Write a function add_user(Name, Address, SSN, Deposit Amount) that adds a new user. Notice that the new user should have a unique ID that is either 1 more than the last unique ID or equal to the first freed up unique ID (by a user closing up their account), whichever comes first.  [4 pt]
- Write a function delete_user(ID) that deletes an existing user. Free up the unique ID while deleting the user. This unique ID can be re-assigned to a future new user.  [4pt]
- Write a function pay_user_to_user(payer ID, payee ID, amount) that lets the user with ID1 pay the user with ID3 by amount.  [5 pt]
- Write a function get_median_id() that returns the median of all the account IDs i.e. the middle node of the linked list.  [5 pt]
- Write a function merge_accounts(ID1, ID2) that merges two accounts into one. This function only merges two accounts if they are owned by the same person, and identified by the same name, address, and SSN. While merging, sum the two balances, delete the account with the biggest unique ID of the two and keep the account with the smallest unique ID with the new balance.  [5 pt]
- [Bonus] Imagine another bank, Bank of Los Angeles which has the same banking protocol and uses the same class as Bank of Orange County. These two banks have decided to merge into a new bank, Bank of Southern California. Merge the two linked lists into one. If both the list has a node with the same ID then create a new ID for one of the duplicates and add it to the new list. While creating the new ID you have to maintain the incremental property. [5 pt]
