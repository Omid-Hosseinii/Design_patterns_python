class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler
        return next_handler

    def handle_request(self, request):
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            print("No handler")


class LeaderHandler(Handler):
    def handle_request(self, request):
        if request["type"] == "day_off" and request["during"] <= 2:
            print("Leader approve")
        else:
            super().handle_request(request)


class ManagerHandler(Handler):
    def handle_request(self, request):
        if request["type"] == "day_off" and request["during"] <= 5:
            print("Manager approve")
        else:
            super().handle_request(request)



class HrHandler(Handler):
    def handle_request(self, request):
        if request["type"] == "day_off" and request["during"] <= 9:
            print("Hr approve")
        else:
            super().handle_request(request)

leader = LeaderHandler()
manager = ManagerHandler()
hr = HrHandler()

leader.set_next_handler(manager).set_next_handler(hr)

request = {"type": "day_off", "during": 7}

leader.handle_request(request)

