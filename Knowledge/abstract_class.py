from abc import ABC, abstractmethod

class ValidatorInterface(ABC):
    @abstractmethod
    def validate():
        pass



class Validator(ValidatorInterface):
    def validate():
        pass

validator = Validator()