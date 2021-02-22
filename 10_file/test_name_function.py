import unittest

def get_formatted_name(first,last):
    """Generate a neatly formatted full name."""
    full_name = first + " " + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

unittest.main()