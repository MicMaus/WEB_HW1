from abc import abstractmethod, ABC

from error_handl_decorator import error_handling_decorator


class MainStyleClass(ABC):
    def __init__(self, func, *args, **kwargs):
        self.func = func  # function that will be called
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def call_function(self, *args, **kwargs):
        pass

    def display_style(self):
        """here visual style for all subclasses can be defined"""
        return self.call_function()


class ContactStyle(MainStyleClass):
    """intended to serve for functions related to contacts"""

    def call_function(self):
        print(self.func(*self.args, **self.kwargs))


class NotesStyle(MainStyleClass):
    """intended to serve for functions related to notes"""

    def call_function(self):
        print(self.func(*self.args, **self.kwargs))


class GeneralStyle(MainStyleClass):
    """intended to serve for other functions, not related to contacts or notes"""

    def call_function(self):
        print(self.func(*self.args, **self.kwargs))
