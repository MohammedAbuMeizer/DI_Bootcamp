import datetime
import flask

class Company():
    def __init__(self,iD,name,planes=[]):
        self.id = iD
        self.name = name
        self.planes = planes


class Airplane():
        def __init__(self,iD,current_location ,company ,next_flights =[]):
            self.id = iD
            self.current_location = current_location
            self.company = company
            self.next_flights = next_flights
        
        def fly(self, destination):
            pass
        def location_on_date(self, date):
            pass
        def available_on_date(self, date, location):
            pass


class Flight():
    def __init__(self,date,destination,origine,plane,iD):
        self.date = date
        self.destination = destination
        self.origine = origine
        self.plane = plane
        self.id = iD

    def take_off(self):
        pass

    def land(self):
        pass
    

class Airport():
    def __init__(self,city,planes,scheduled_departures,scheduled_arrivals):
        self.city = city
        self.planes = planes
        self.scheduled_departures = scheduled_departures
        self.scheduled_arrivals = scheduled_arrivals
    
    def schedule_flight(self, destination, datetime):
        pass

    def info(self, start_date, end_date):
        pass
