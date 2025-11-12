class TYMarks:
    def __init__(self, theory, practical):
        self.Theory = theory
        self.Practical = practical
        print("TYMarks constructor called")

    def __del__(self):
        print("TYMarks destructor called")

    def display(self):
        print("Theory Marks:", self.Theory)
        print("Practical Marks:", self.Practical)