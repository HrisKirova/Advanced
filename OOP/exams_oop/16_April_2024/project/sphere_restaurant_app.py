from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    WAITER_CLASSES = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}
    def __init__(self):
        self.waiters = []
        self.clients = []


    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITER_CLASSES:
            return f"{waiter_type} is not a recognized waiter type."
        for waiter in self.waiters:
            if waiter_name == waiter.name:
                return f"{waiter_name} is already on the staff."

        waiter = self.WAITER_CLASSES[waiter_type](waiter_name, hours_worked)

        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."


    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."

        for client in self.clients:
            if client_name == client.name:
                return f"{client_name} is already a client."

        client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        for waiter in self.waiters:
            if waiter_name == waiter.name:
                return waiter.report_shift()
        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        for client in self.clients:
            if client.name == client_name:
                earned_points = client.earning_points(order_amount)
                return f"{client_name} earned {earned_points} points from the order."
        return f"{client_name} is not a registered client."


    def apply_discount_to_client(self, client_name: str):
        for client in self.clients:
            if client_name == client.name:
                discount, points = client.apply_discount()
                return f"{client_name} received a {discount}% discount. Remaining points {points}"

        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_clients_count = len(self.clients)
        total_unused_points = sum(client.points for client in self.clients)

        report = "$$ Monthly Report $$\n"
        report += f"Total Earnings: ${total_earnings:.2f}\n"
        report += f'Total Clients Unused Points: {total_unused_points}\n'
        report += f'Total Clients Count: {total_clients_count}\n'
        waiter_info = '** Waiter Details **\n'

        for waiter in sorted_waiters:
            waiter_info += str(waiter) + "\n"

        report += waiter_info
        return report.strip()



