import calendar

class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year = map(int, date.split("."))
        month_name_str = calendar.month_name[month]
        return cls(name, id, year, month_name_str, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}")

