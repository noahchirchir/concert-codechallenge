class Band:
    def __init__(self, name, hometown):
        self.name = name  
        if not isinstance(hometown, str):
            raise Exception("Hometown must be a string")
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Band name must be a non-empty string")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if hasattr(self, '_hometown'):
            raise Exception("Hometown cannot be changed")
        self._hometown = value

    def concerts(self):
        return self._concerts if self._concerts else None

    def venues(self):
        if not self._concerts:
            return None
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        if concert not in self._concerts:
            self._concerts.append(concert)
            venue.add_concert(concert)
        return concert

    def all_introductions(self):
        introductions = []
        for concert in self._concerts:
            venue_city = concert.venue.city
            introduction = f"Hello {venue_city}!!!!! We are {self.name} and we're from {self.hometown}"
            introductions.append(introduction)
        return introductions


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        band._concerts.append(self)
        venue.add_concert(self)
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Date must be a non-empty string")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise Exception("Band must be of type Band")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise Exception("Venue must be of type Venue")
        self._venue = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
     return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        self.name = name  
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Venue must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("City must be a non-empty string")
        self._city = value

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        if not self._concerts:
            return None
        return list(set(concert.band for concert in self._concerts))

    def add_concert(self, concert):
        if not isinstance(concert, Concert):
            raise Exception("Concert must be of type Concert")
        self._concerts.append(concert)