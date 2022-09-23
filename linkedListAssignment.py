class AccountList:
    # list of bank accounts
    
    class _Account:
        # holds all account information
        __slots__ = '_name', '_address', '_socialSecurity', '_initialDeposit'

        def __init_(self, name, address, socialSecurity, initialDeposit):
            self._name = name
            self._address = address
            self._socialSecurity = socialSecurity
            self._initialDeposit = initialDeposit

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

    def __add_user__(self, name, address, ssn, deposit):
        # adds a new user to the list

        # create an account for the new user
        newAccount = self._Account(name, address, ssn, deposit)

        if(self._size == 0):
            # if the list is empty, make head and tail with ID=1
            newNode = self._Node(newAccount, 1, None)
            self._head = newNode
            self._tail = newNode
            self._size = 1
        elif(self._size == self._tail._uniqueID):
            # if no freed up IDs exist, add to the end of the list
            newNode = self._Node(newAccount, self._size + 1, None)
            self._tail._next = newNode
            self._tail = newNode
            self._size += 1
        else:
            # traverse the list to find the first freed up ID
            currNode = self._head

            while currNode._next._uniqueID == currNode._uniqueID + 1:
                # traverse until there is a gap in the uniqueID
                currNode = currNode._next
            
            # insert the new node after currNode
            newNode = self._Node(newAccount, currNode._uniqueID + 1, currNode._next)
            currNode._next = newNode
            self._size += 1
