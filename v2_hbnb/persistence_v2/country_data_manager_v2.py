from .IPersistenceManager import IPersistenceManager
from models.country import Country

class CountryDataManager(IPersistenceManager):
    def __init__(self):
        self.data = []

    def save(self, country):
        self.data.append(country)
        return country

    def get_all(self):
        return self.data

    def get(self, country_code):
        for country in self.data:
            if country.code == country_code:
                return country
        return None

    def update(self, country_code, new_name):
        for country in self.data:
            if country.code == country_code:
                country.name = new_name
                return country
        return None

    def delete(self, country_code):
        for idx, country in enumerate(self.data):
            if country.code == country_code:
                del self.data[idx]
                return True
        return False
