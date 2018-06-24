class Session:

    def __init__(self, session_id, start_time):
        self.session_id = session_id
        self.startTime = start_time
        self.elapsed_time = 0

    def get_session_id(self):
        return self.session_id

    def get_start_time(self):
        return self.startTime

    def get_elapsed_time(self):
        return self.elapsed_time
