class Gym:
    """Manages multiple gym memberships and applies discounts."""
    def _init_(self):
        self.memberships = {}
        self.group_discount = 0.10
        self.special_discounts = [
            (400, 50),
            (200, 20)
        ]
        self.premium_surcharge = 0.15

    def add_membership(self, membership):
        """Adds a membership plan to the gym."""
        self.memberships[membership.name] = membership

    def calculate_total_cost(self, membership_name, num_members=1, apply_premium=False):
        """Calculates the total cost of a membership including any discounts and surcharges."""
        if membership_name not in self.memberships:
            raise ValueError(f"Membership {membership_name} not found.")

        membership = self.memberships[membership_name]
        total_cost = membership.calculate_cost()

        if num_members > 1:
            total_cost -= total_cost * self.group_discount

        for threshold, discount in self.special_discounts:
            if total_cost > threshold:
                total_cost -= discount
                break

        if apply_premium:
            total_cost += total_cost * self.premium_surcharge

        return total_cost