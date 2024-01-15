#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:21:26 2023

@author: oussamahabachi
"""
import sys
from datetime import datetime
from icalendar import Calendar
import csv
import re

# CONFIG


ICS_FILE_LOCATION = sys.argv[1]
CSV_FILE_LOCATION = sys.argv[2]

# ICAL2CSV

class Convert2CSV():
    def __init__(self):
        self.csv_data = []

    def read_ical(self, ical_file_location):
        with open(ical_file_location, 'r', encoding='utf-8') as ical_file:
            data = ical_file.read()
        self.cal = Calendar.from_ical(data)
        return self.cal

    def make_csv(self):
        for event in self.cal.subcomponents:
            if event.name != 'VEVENT':
                continue
            #if datetime.combine(event.get('DTSTART').dt, datetime.min.time()) >= datetime.fromisoformat(START_DATE) and datetime.combine(event.get('DTEND').dt, datetime.min.time()) <= datetime.fromisoformat(END_DATE):
            row = [
                # Date
                event.get('DTSTART').dt.strftime("%Y-%m-%d:"),
                # HStart
                event.get('DTSTART').dt.strftime("%H:%M:%S"),
                # HEnd 
                event.get('DTEND').dt.strftime("%H:%M:%S"),
                # Summary
                ' : '.join(str(event.get('SUMMARY')).splitlines()),
                # Location
                str(event.get('LOCATION')),
                # Description
                ' : '.join(str(event.get('DESCRIPTION')).splitlines()),
            ]
            row = [x.strip() for x in row]
            self.csv_data.append(row)

    def save_csv(self, csv_location):  # type: (str) -> None
        schema = ["Date", "HStart", "HEnd", "Summary", "Location", "Description"]
        with open(csv_location, 'w', encoding='utf-8') as csv_handle:
            writer = csv.writer(csv_handle)
            writer.writerow([h for h in schema])
            for row in self.csv_data:
                writer.writerow([r.strip() for r in row])


Convert2CSV = Convert2CSV()
Convert2CSV.ICS_FILE_LOCATION = ICS_FILE_LOCATION
Convert2CSV.CSV_FILE_LOCATION = CSV_FILE_LOCATION

Convert2CSV.read_ical(Convert2CSV.ICS_FILE_LOCATION)
Convert2CSV.make_csv()
Convert2CSV.save_csv(Convert2CSV.CSV_FILE_LOCATION)

