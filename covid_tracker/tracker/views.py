from django.shortcuts import render
import requests
from django.db import models
import json
from requests import get
from datetime import timedelta, date
import datetime
# Create your views here.


def index(request):
    world_data_latest= get_world_data()

    uk_countries_data= get_uk_countries_data()
    uk_historical_data = get_uk_historical_data()
    uk_regions_data = get_uk_regions_data()


    scotland_data = get_scotland_data()
    scotland_ca = get_ca_names()

    scotland_historical_data_1 = get_scotland_historical_data()
    scotland_historical_data = []
    for i in range(len(scotland_historical_data_1)-1, 0, -1):
        scotland_historical_data.append(scotland_historical_data_1[i])


    england_historical_data_1 = get_england_historical_data()
    england_historical_data = []
    for i in range(len(england_historical_data_1)-1, 0, -1):
        england_historical_data.append(england_historical_data_1[i])
    england_female_cases = get_england_female_cases()
    england_male_cases = get_england_male_cases()

    wales_historical_data_1 = get_wales_historical_data()
    wales_historical_data = []
    for i in range(len(wales_historical_data_1)-1, 0, -1):
        wales_historical_data.append(wales_historical_data_1[i])

    time_dict = make_time_dict()

    capitals = get_capitals()


    return render(request, 'index.html', {'world_data_latest': world_data_latest, 'uk_countries_data' : uk_countries_data, 'uk_historical_data' : uk_historical_data, 'uk_regions_data' : uk_regions_data,  'scotland_ca' : scotland_ca, 'scotland_data': scotland_data,
                                              'england_historical_data': england_historical_data, 'time_dict' : time_dict, 'scotland_historical_data' : scotland_historical_data, 'england_male_cases' : england_male_cases,
                                              'england_female_cases' : england_female_cases, 'wales_historical_data' : wales_historical_data,})



def get_world_data():
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "51896eb81amsh2a57d7238e4a57ep137532jsn106ff7f478ab"
        }

    response = requests.request("GET", url, headers=headers).json()

    return response['response']

def get_uk_countries_data():
    url = "https://covid-19-uk-data-by-zt.p.rapidapi.com/GetUKCountryWiseData"

    headers = {
        'x-rapidapi-host': "covid-19-uk-data-by-zt.p.rapidapi.com",
        'x-rapidapi-key': "51896eb81amsh2a57d7238e4a57ep137532jsn106ff7f478ab"
        }

    response = requests.request("GET", url, headers=headers).json()

    return response['data']

def get_uk_historical_data():
    url = "https://covid-19-uk-data-by-zt.p.rapidapi.com/GetAllHistoricalDataForEngland"

    headers = {
        'x-rapidapi-host': "covid-19-uk-data-by-zt.p.rapidapi.com",
        'x-rapidapi-key': "51896eb81amsh2a57d7238e4a57ep137532jsn106ff7f478ab"
        }

    response = requests.request("GET", url, headers=headers).json()

    return response['records']


def get_uk_regions_data():
    import requests

    url = "https://covid-19-uk-data-by-zt.p.rapidapi.com/GetUKRegionWiseData"

    headers = {
        'x-rapidapi-host': "covid-19-uk-data-by-zt.p.rapidapi.com",
        'x-rapidapi-key': "51896eb81amsh2a57d7238e4a57ep137532jsn106ff7f478ab"
        }

    data = requests.request("GET", url, headers=headers).json()

    return data['data']

def get_scotland_data():
    url = "https://www.opendata.nhs.scot/api/3/action/datastore_search?resource_id=e8454cf0-1152-4bcb-b9da-4343f625dfef&limit=32&q"


    response = get(url).json()
    r = response['result']['records']

    return r




def get_ca_names():
    url = "https://www.opendata.nhs.scot/api/3/action/datastore_search?resource_id=967937c4-8d67-4f39-974f-fd58c4acfda5&limit=44&q"


    response = get(url).json()
    r = response['result']['records']

    return r

def get_england_historical_data():
    def get_data(url):
        response = get(endpoint, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

        return response.json()
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation;areaName=england&'
        'structure={"date":"2020-08-23","cases":"newCasesByPublishDate"}'
    )
    data = get_data(endpoint)

    return data['data']

def make_time_dict():
    x = datetime.datetime.now()
    def daterange(date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + timedelta(n)

    dict = {}
    start_dt = date(2020, 1, 4)
    end_dt = date(x.year, x.month, x.day)
    for dt in daterange(start_dt, end_dt):
        dict[dt.strftime("%Y-%m-%d")]= dt.strftime("%Y-%m-%d")

    return dict

def get_scotland_historical_data():
    def get_data(url):
        response = get(endpoint, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

        return response.json()
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation;areaName=scotland&'
        'structure={"date":"2020-08-23","cases":"newCasesByPublishDate"}'
    )
    data = get_data(endpoint)

    return data['data']

def get_wales_historical_data():
    def get_data(url):
        response = get(endpoint, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

        return response.json()
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation;areaName=wales&'
        'structure={"date":"2020-08-23","cases":"newCasesByPublishDate"}'
    )
    data = get_data(endpoint)

    return data['data']

def get_england_male_cases():
    def get_data(url):
        response = get(endpoint, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

        return response.json()
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation;areaName=england&'
        'structure={"date":"2020-08-23","cases":"maleCases"}'
    )
    data = get_data(endpoint)

    return data['data'][0]['cases']

def get_england_female_cases():
    def get_data(url):
        response = get(endpoint, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

        return response.json()
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation;areaName=england&'
        'structure={"date":"2020-08-23","cases":"femaleCases"}'
    )
    data = get_data(endpoint)

    return data['data'][0]['cases']

def get_capitals():
    url = "http://techslides.com/demos/country-capitals.json"


    response1 = get(url).json()
