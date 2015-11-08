#!/usr/bin/python
import requests, json, webbrowser, ast, random, sys
def main(items=None):
    def formatrecipe(json):
        recipe = ast.literal_eval(json)
        foobar=recipe["recipe"]
        webbrowser.open(foobar["source_url"])


    key = "faae5fad87c4e4432cb9437b1773b259"
    ingredients = ",".join(items)
    #ingredients = str(raw_input("Enter an ingredient you have."))

    search = requests.post("http://food2fork.com/api/search?key=" + key + "&q=" + ingredients + "&sort=r")
    json_data=json.loads(search.text)
    # print json_data
    recipies = json_data["recipes"]

    try:
        food_id = recipies[random.randint(0, 30)]["recipe_id"]
        request = requests.post("http://food2fork.com/api/get?key=" + key + "&rId=" + food_id)
        if int(request.status_code) == 200:
            formatrecipe(request.text)
            return "Success!"
        else:
            return "An error occured." , request.status_code, request.reason

    except IndexError:
        return "No recipes could be found."
        #sys.exit()
