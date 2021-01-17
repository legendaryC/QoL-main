from .models import *
import datetime


class ImportData:
    def __init__(self):
        super().__init__()

    def get_data(self):
        new_entry = Albumin(patient_ID='pa0001',
                            date_time=datetime.datetime(2020, 5, 17), value=1.2)
        new_entry.save()
