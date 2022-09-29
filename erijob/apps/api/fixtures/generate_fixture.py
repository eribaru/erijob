# coding:utf-8
import json

MODEL_NAME = "api.cidade"

with open('brazil-cities-states-en.json', encoding="utf8") as data_file:
    data = json.load(data_file)
    fixtures = []
    city_pk = 0

    for state_object in data['states']:
        state = state_object['uf']
        for city in state_object['cities']:
            city_pk = city_pk + 1
            fixture_object = {
                "model": MODEL_NAME,
                "pk": city_pk,
                "fields": {
                    "nom_cidade": city,
                    "cod_estado": state
                }
            }

            fixtures.append(fixture_object)

    fixture_data = json.dumps(fixtures)
    fixtures_file = open("city.json", "w")
    fixtures_file.write(fixture_data)
    fixtures_file.close()
