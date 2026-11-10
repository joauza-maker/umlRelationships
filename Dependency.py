class Key:
    def get_code(self):
        return "1234"

class Lock:
    def unlock(self, key_source):
        print("Opening lock with code: " + key_source.get_code())

house_key = Key()
front_door = Lock()
front_door.unlock(house_key)
