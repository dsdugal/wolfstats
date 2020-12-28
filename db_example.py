
# mongodb python example for wolfstats (to be done...)

import json


from lib.helpers import db_helper as dbh


x = dbh.DB_Helper()

database = x.client.cookbook
recipes = database.recipes


recipe = {'title': 'chocolate milk',
          'description': 'Yummy drink',
          'ingredients': [
              {'name': 'milk', 'quantity': 8, 'unit of measure': 'ounce'},
              {'name': 'chocolate syrup', 'quantity': 2, 'unit of measure': 'ounce'}
          ],
          'yield': {'quantity': 1, 'unit': 'glass'},
          'prep time': 0,
          'cook time': 0,
          'author': 'Biff Tannen',
          'uploaded_by': 'kenwalger',
          }

recipes.insert_one(recipe)

d = dict((db, [collection for collection in x.client[db].list_collection_names()])
            for db in x.client.list_database_names())

import pprint

print("\nPretty Printed document: \n")
pprint.pprint(recipes.find_one())

recipes.update_one({'title': 'chocolate milk'},
                   {'$set': {'author': 'George McFly'}
                    }
                   )
print("\nShould be George McFly: ")
pprint.pprint(recipes.find_one({'author': 'George McFly'}))

#recipes.delete_one('_id': ObjectId('588541a0146bde28a08217d4'))

