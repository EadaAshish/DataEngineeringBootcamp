class Meter:
    meter_id: str
    plant_id: str
    is_active: bool

    def __init__(
        self, 
        meter_id: str,
        plant_id: str, 
        is_active: bool
    ):
        self.meter_id = meter_id
        self.plant_id = plant_id
        self.is_active = is_active