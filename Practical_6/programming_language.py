class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name="", typing='', reflection='', year=0):
        """Create a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Find out if language is dynamically typed."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)
