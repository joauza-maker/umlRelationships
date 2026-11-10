from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_content(self):
        pass

class Invoice(Printable):  
    def print_content(self):
        print("Printing invoice details...")

bill = Invoice()
bill.print_content()
