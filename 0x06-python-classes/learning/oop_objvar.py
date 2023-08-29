class Robot:
    """Represents a robot, with a name"""

    # A class variable that counts the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the robot"""
        self.name = name
        print("\n***Initializing {}***".format(self.name))

        """When created, the robot population increases"""
        Robot.population += 1

    def die(self):
        """The robot is dying"""
        print("\n{} is being destroyed".format(self.name))
        Robot.population -= 1

        if (Robot.population == 0):
            print("\n{} was the last one".format(self.name))
        else:
            print("\n{:d} robots are still working".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot"""
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print("We have {:d} robots".format(cls.population))

droid1 = Robot("Glass")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("Stone")
droid2.say_hi()
Robot.how_many()

print("\nRobots are working")
print("\nRobots have finished working and can be destroyed")

droid1.die()
droid2.die()

Robot.how_many()
