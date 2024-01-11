class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer.")
        space_left = self._capacity - self._size
        if n <= space_left:
            self._size += n
        else:
            raise ValueError("Not enough space in the jar.")

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdrawal amount must be a non-negative integer.")
        if n <= self._size:
            self._size -= n
        else:
            raise ValueError("Not enough cookies in the jar.")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


