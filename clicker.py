"""
The clicker holder itself. Built to be flexible and allow for modularity.
"""
import upgrades as ups


class Clicker:
    def __init__(self):
        self.Name = ''
        self.Buildings = {}
        self.BoughtBuildings = {}
        self.Upgrades = {}
        self.BoughtUpgrades = []  # This is just a T/F value, so it's existence in here markes it true.
        self.Curr = []

        # Math division, this may be altered and overridden by specific rules in the Buildings.
        self.Scaling = 1.01  # The scaling from one buy to the next (floor and power is used to maintain int values)
        return

    def run_cycle(self):
        """
        This method runs through a cycle of addition to the currency. All buildings and upgrades are added together
        and added to the appropriate Curr value. If it attempts to add to something that doesn't exist it throws a 
        runtime error.
        """
        pass

    def create_upgrade(self, name, bonusTo, bonusOf, **kwargs):
        self.Upgrades = ups.Upgrades()
        return
