class Airline:
    def __init__(self,amount_of_planes,destinations,workers,max_planes=30,max_workers=100) -> None:
        self.amount_of_planes = amount_of_planes
        self.destinations = destinations
        self.workers = workers