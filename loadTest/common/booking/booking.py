from json import JSONDecodeError
import random
from common.utils import random_word
import common.inventory.workspaces as inventory_workspaces
from datetime import datetime, timedelta

bookings_base_url = '/api/booking/bookings'
availability_base_url = '/api/booking/availability/workspaces'
history_base_url = '/api/booking/history'


def list_bookings(self):
    return self.client.get(catch_response=True)


def get_booking_by_id(self):
    with self.client.get(bookings_base_url, catch_response=True) as response:
        try:
            booking = random.choice(response)
            return self.client.get(
                f'{bookings_base_url}/{booking._id}', name=f"{bookings_base_url}/booking_id", catch_response=True)
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key booking.id")


def add_booking(self):
    booking_data = get_random_booking_data(self)
    self.client.post(bookings_base_url, json=booking_data)


def delete_booking(self):
    with self.client.get(bookings_base_url, catch_response=True) as response:
        try:
            booking = random.choice(response)
            self.client.delete(
                f'{bookings_base_url}/{booking._id}', name=f"{bookings_base_url}/booking_id")
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key booking.id")


# def get_available_workspaces(self):
#     return self.get(availability_base_url, catch_response=True)


def get_bookings_history(self):
    return self.get(history_base_url, catch_response=True)


def check_in(self):
    return self.post('/api/booking/check-in', json={ "rfid": random_word(30) })

def check_out(self):
    return self.post('/api/booking/check-out', json={ "rfid": random_word(30) })


def get_random_booking_data(self):
    workspace = inventory_workspaces.get_workspace_by_id(self)
    start_datetime = datetime.now()
    end_datetime = datetime.now() + timedelta(minutes=1)

    return {"workspace": workspace['_id'], "start_datetime": start_datetime, "end_datetime": end_datetime}
