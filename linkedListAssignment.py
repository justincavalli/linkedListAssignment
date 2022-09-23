class AccountList:
    # list of bank accounts
    
    class Account:
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

