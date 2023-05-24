from global_variables import GlobalVariables


class AllRegistersClosedException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Message = f"All registers are closed"


class Register:
    Customers: list[str]
    Number: int
    IsOpen = True

    def __init__(self) -> None:
        self.Customers = []

    def Open(self) -> None:
        self.IsOpen = True

    def Close(self) -> None:
        self.IsOpen = False
        self.Customers.clear()

    def AddPerson(self, name: str) -> None:
        if self.IsOpen:
            self.Customers.append(name)

    def Transact(self) -> None:
        if len(self.Customers) > 0 and self.IsOpen:
            self.Customers.pop(0)


class Shop:
    Registers: list[Register]

    def __init__(self) -> None:
        self.Registers = [Register() for _ in range(GlobalVariables.RegisterAmount)]

    def FindLowestCustomersInRegisters(self) -> int:
        indexes = [num for num in range(len(self.Registers))]

        indexes.sort(key=lambda i: len(self.Registers[i].Customers))

        for i in indexes:
            if self.Registers[i].IsOpen:
                return i

    def AddNewCustomer(self, name: str) -> None:
        i = self.FindLowestCustomersInRegisters()
        if i is None:
            raise AllRegistersClosedException
        self.Registers[i].AddPerson(name)

    def CloseRegister(self, registerNum: int) -> None:
        customers = []
        customers.extend(self.Registers[registerNum].Customers)
        self.Registers[registerNum].Close()

        for customer in customers:
            self.AddNewCustomer(customer)
