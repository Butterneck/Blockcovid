from json import JSONDecodeError
import random
from common.utils import random_word

rooms_base_url = '/api/inventory/rooms'

def list_rooms(self):
    self.client.get()


def get_room_by_id(self):
    with self.client.get(rooms_base_url, catch_response=True) as response:
        try:
            room = random.choice(response)
            self.client.get(
                f'{rooms_base_url}/{room._id}', name=f"{rooms_base_url}/room_id")
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key room.id")


def get_room_by_rfid(self):
    with self.client.get(rooms_base_url, catch_response=True) as response:
        try:
            room = random.choice(response)
            self.client.get(
                f'{rooms_base_url}/{room.rfid}', name=f"{rooms_base_url}/room_id")
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key room.id")


def add_room(self):
    room_data = get_random_room_data()
    self.client.post(rooms_base_url,
                     json={"name": room_data['name'], "rfid": room_data['rfid']})


def patch_room(self):
    with self.client.get(rooms_base_url, catch_response=True) as response:
        try:
            room = random.choice(response)
            patch_data = get_random_room_data()
            self.client.patch(
                f'{rooms_base_url}/{room._id}', data=patch_data, name=f"{rooms_base_url}/room_id")
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key room.id")


def delete_room(self):
    with self.client.get(rooms_base_url, catch_response=True) as response:
        try:
            room = random.choice(response)
            self.client.delete(
                f'{rooms_base_url}/{room._id}', name=f"{rooms_base_url}/room_id")
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure(
                "Response did not contain expected key room.id")


def get_random_room_data():
    name = random_word(30)
    rfid = random_word(30)
    enabled = bool(random.getrandbits(1))

    return {"name": name, "rfid": rfid, "enabled": enabled}
