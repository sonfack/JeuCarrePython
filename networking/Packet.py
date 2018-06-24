class Packet:
    def __init__(self, header, payload):
        self._packetHeader = header
        self._payload = payload

    def get_header(self):
        return self._packetHeader

    def get_payload(self):
        return self._payload
