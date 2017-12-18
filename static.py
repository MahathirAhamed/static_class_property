'''
Created on Dec 18, 2017

@author: mahathir.ahamed
'''

class Methods():
    """
    Defines the Class and Static Method Difference
    """
    message = ''
    def __init__(self,msg):
        Methods.message = msg
        self.message = msg +"However I am good"

    @staticmethod
    def test_static():
        """
        Tests the static method and its actual benefits
        """
        print "Message of the class variable in static {}".format(Methods.message)

    @classmethod
    def test_class(cls):
        """
        Displays the class attribute and the class methods benefits
        """
        print "Message of the class variable in class {}".format(cls.message)
    
    @property
    def set_classmessage(self):
        """
        Here we sets the class attribute with the property type
        """
        return self.message
    @set_classmessage.setter
    def set_classmessage(self,new_msg):
        """
        Here we are using property method setter
        """
        self.message = new_msg
        
if __name__ == "__main__":
    met = Methods("Hey I am gonna tossed")
    Methods.test_class()
    Methods.test_static()
    print met.set_classmessage
    met.set_classmessage = "I am done"
    print met.set_classmessage
