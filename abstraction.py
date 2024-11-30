from abc import ABC, abstractmethod
class abstraction(ABC):

    @abstractmethod
    def generate_matches(self):
        pass

    @abstractmethod
    def schedule_matches(self):
        pass
    @abstractmethod
    def view_matches(self):
        pass
    @abstractmethod
    def update_match(self):
        pass
    @abstractmethod
    def cancel_match(self):
        pass
    @abstractmethod
    def check_conflicts(self):
        pass
