class PacketHeader:

    def __init__(self, version, type, joueur_id, payload_type, time, elapsed_time, payload_size, code):
        self._version = version
        self._code = code
        self._type = type
        self._joueur_id = joueur_id
        self._payloadType = payload_type
        self._time = time
        self._elapsedTime = elapsed_time
        self._payloadSize = payload_size

    def get_version(self):
        return self._version

    def get_code(self):
        return self._code

    def get_type(self):
        return self._type

    def get_joueur_id(self):
        return self._joueur_id

    def get_payload_type(self):
        return self._payloadType

    def get_elapsed_time(self):
        return self._elapsedTime

    def get_payload_size(self):
        return self._payloadSize
