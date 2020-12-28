import pymongo

# basic crud wrapper for mongodb

class DB_Helper(object):

    def __init__(self):
        
        # these could be passed in
        self.host = 'localhost'
        self.port = 27017
        self.pool_size = 50
        #
        self.client = pymongo.MongoClient(self.host, self.port, maxPoolSize=self.pool_size)
        print('im db helper and i will initialize your db connection')

    ## CREATE (c)
    # op - defines scope of operation
    # collection - defines the 'table' to work on
    # entry - defines the entry you want to 'create'
    #           - if 'table', you can ascribe initial attributes the table has, etc.
    #           - if anything else, you should follow that table's convention regarding available fields

    def create(self, op, collection, entry):
        print(f'creating {op}...')
        if op == 'table':
            print(f'creating table... {collection}')
        else:
            print(f'creating entry in table {collection}')

    ## READ (r)
    # op - defines scope of operation
    # collection - defines the 'table' to work on
    # query - defines the set of entries you want to 'read'
    #           - if 'all', you can query for cross-cutting entries
    #           - if an entry, you should follow that table's convention regarding available fields

    def read(self, op, collection, query):
        print(f'reading {op}...')
        if op == 'all':
            collection = self.client[collection]
            cursor = collection.find({})
            for document in cursor:
                print(document)
        else:
            print(f'reading entry in specific table {collection}...')
        
    ## UPDATE (u)
    # op - defines scope of operation
    # collection - defines the 'table' to work on
    # query - defines the set of entries you want to 'update'
    #           - if 'all', you can update cross-cutting entries using queries
    #           - if an entry, you should follow that table's convention regarding available fields

    def update(self, op, collection, query, new_data):
        print(f'updating {op}...')
        if op == 'all':
            print(f'updating all tables in... {collection}')
        else:
            print(f'updating entry in table {collection}')

    ## DELETE (u)
    # op - defines scope of operation
    # collection - defines the 'table' to work on
    # query - defines the set of entries you want to 'delete'
    #           - if 'all', you can update cross-cutting entries using queries
    #           - if an entry, you should follow that table's convention regarding available fields

    def delete(self, op, collection, query):
        print(f'delete {op}...')
        if op == 'all':
            print(f'deleting all tables in... {collection}')
        else:
            print(f'deleting entry in table {collection}')