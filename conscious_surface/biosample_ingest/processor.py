class BiosampleProcessor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type

    def ingest_data(self, raw_stream):
        return self._parse_to_standard(raw_stream)

    def _parse_to_standard(self, raw):
        # Hardware SDK mapping logic
        return {"type": self.sensor_type, "value": hash(raw)}
