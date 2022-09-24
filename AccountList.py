# Name: Justin Cavalli
# Date: last edit 9/24/2022
# Description: This program implements a Linked list of Bank Accounts with functionalities
#              to add users, delete users, merge users, and pay from one user to another 
#              as outlined in Assignment 1 of SWE 240.

class AccountList:
    # list of bank accounts
    
    class _Account:
        # holds all account information
        __slots__ = '_name', '_address', '_socialSecurity', '_balance'

        def __init__(self, name, address, socialSecurity, initialDeposit):
            self._name = name
            self._address = address
            self._socialSecurity = socialSecurity
            self._balance = initialDeposit

    class _Node:
        # each node contains an element, ID, and reference to next node
        __slots__ = '_element', '_uniqueID', '_next'

        def __init__(self, element, uniqueID, next):
            self._element = element
            self._uniqueID = uniqueID
            self._next = next
    
    # constructor for the Linked list of Accounts
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        # returns the number of elements in the list
        return self._size

    def is_empty(self):
        # return true if the stack is is_empty
        return self._size == 0
    
    def add_user(self, name, address, ssn, deposit):
        # adds a new user to the list

        # create an account for the new user
        newAccount = self._Account(name, address, ssn, deposit)

        if(self.is_empty()):
            # if the list is empty, make head and tail with ID=1
            newNode = self._Node(newAccount, 1, None)
            self._head = newNode
            self._tail = newNode
        elif(self._size == self._tail._uniqueID):
            # if no freed up IDs exist, add to the end of the list
            newNode = self._Node(newAccount, self._size + 1, None)
            self._tail._next = newNode
            self._tail = newNode
        elif(self._head._uniqueID != 1):
            # the first ID has been freed up
            newNode = self._Node(newAccount, 1, self._head)
            self._head = newNode
        else:
            # traverse the list to find the gap in ID
            currNode = self._head

            while currNode._next._uniqueID == currNode._uniqueID + 1:
                currNode = currNode._next
            
            # insert the new node after currNode
            newNode = self._Node(newAccount, currNode._uniqueID + 1, currNode._next)
            currNode._next = newNode
        
        # update the size
        self._size += 1

    def delete_user(self, ID):
        # delete the user with the given ID

        if(self.is_empty()):
            raise Exception('stack is empty')

        currNode = self._head

        if(self._head._uniqueID == ID):
            # special case deleting the head
            nodeToDelete = self._head
            self._head = self._head._next
            nodeToDelete._next = None
        else:
            # traverse the list to find the Node with the given ID
            prevNode = None
            currNode = self._head
            while currNode != None and currNode._uniqueID != ID:
                if(currNode._uniqueID > ID):
                    raise Exception('ID not found')
                else:
                    prevNode = currNode
                    currNode = currNode._next
            
            if(currNode == None):
                raise Exception('ID not found')
            
            # update Node references to delete the given node
            prevNode._next = currNode._next
            currNode._next = None
            nodeToDelete = currNode
        self._size -= 1

        return nodeToDelete._element

    def pay_user_to_user(self, payerID, payeeID, amount):
        # pay 'amount' from one user to another user

        payer = None
        payee = None
        currNode = self._head

        # traverse the list to identify payer and payee
        while payer == None or payee == None:
            if(currNode == None):
                raise Exception('ID(s) does not exist')
            if(currNode._uniqueID == payerID):
                payer = currNode
            elif(currNode._uniqueID == payeeID):
                payee = currNode
            
            currNode = currNode._next
        
        # adjust balances based on amount
        payer._element._balance -= amount
        payee._element._balance += amount

    def get_median_id(self):
        # returns the median ID in the list

        if(self.is_empty()):
            raise Exception('the list is empty')

        elif(self._size == 1):
            # list of 1 -> median is the head's ID
            return self._head._uniqueID
        
        middle = (int) (self._size / 2)
        currNode = self._head

        # traverse the list until the middle is reached
        for x in range(middle-1):
            currNode = currNode._next

        if(self._size % 2 == 0):
            # median is the avg of the two middle elements
            median = (currNode._uniqueID + currNode._next._uniqueID) / 2
        else:
            # median is the middle element
            median = currNode._next._uniqueID
        return median

    def merge_accounts(self, ID1, ID2):
        # merges two accounts into one, deleting the account with smaller ID

        currNode = self._head
        firstNode = None
        secondNode = None
        
        # traverse until both nodes are found based on ID
        while(firstNode == None or secondNode == None):
            # error if you have traversed the entire list, still in the loop
            if(currNode == None):
                raise Exception('ID(s) not found')
            
            if(currNode._uniqueID == ID1):
                firstNode = currNode
            elif(currNode._uniqueID == ID2):
                secondNode = currNode
            currNode = currNode._next
        
        if(firstNode._element._name == secondNode._element._name and firstNode._element._address == secondNode._element._address and firstNode._element._socialSecurity == secondNode._element._socialSecurity):
            # if it is the same person, merge
            totBalance = firstNode._element._balance + secondNode._element._balance
            if ID1 > ID2:
                firstNode._element._balance = totBalance
                self.delete_user(ID2)
            else:
                secondNode._element._balance = totBalance
                self.delete_user(ID1)
        else:
            raise Exception('IDs are not the same person')