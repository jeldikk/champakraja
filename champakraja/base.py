import abc

class character(abc.ABC):

    @abc.abstractmethod
    def books(self):
        pass

    @abc.abstractmethod
    def hobbies(self):
        pass

    @abc.abstractmethod
    def activities(self):
        pass

    @abc.abstractmethod
    def hairstyle(self):
        pass

    @abc.abstractmethod
    def nature(self):
        pass
