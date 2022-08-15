"""This module uses the pymongo driver to deliver CRUD methods.

It first connects to server and asks user to specify project/database name, then it allows
the create, read, update, and delete methods to users while hiding the mongo commands for 
ease of use for end user.
"""

from pymongo import MongoClient

"""The animal shelter class contains the methods to perform aforementioned crud operations
and to connect to to server.
"""
class AnimalShelter:

    """Method: Initialization
       Purpose: This constructor uses 4 parameters to authenticate user
       Input: Host, port, username, and password
       Output: None 
    """
    def __init__(self, host, port, username, password):
        
        self.host = host
        self.port = port
        self.user = username
        self.userpass = password
    
    """Method: Url initialization 
       Purpose: This is an optional alternative constructor using url string to authenticate
       Input: Url string containing 4 parameters from previous method in url format
       Output: Print statement verifying creation - no return value
    """
    def __init__(self, url):
        
        self.url = url
        print('Created')
      
    """Method: Connect to database
       Purpose: Connects to server by specifying database name
       Input: Project name/database name in ['project'] format
       Ouput: Prints the database information to show confirmation of connection
    """
    def connect(self, project):
        
        self.c = MongoClient(self.url)
        self.dbase = self.c[project]       
        print(self.dbase)
       
    """Method: Collections
       Purpose: This is a method to display collections
       Input: None
       Ouput: Prints list of collection names available
    """
    def showCollections(self):
        
        print(self.dbase.list_collection_names())
       
    """Method: Display Databases
       Purpose: Used to display database names
       Input: None
       Output: Prints list of database names
    """
    def showDatabases(self):
        
        print(self.c.list_database_names())

    """Method: Create
       Purpose: This is the create method to add new records
       Input: Data parameter which is the new record to create in key-value format
       Output: Returns True and prints message confirming successful entry on success otherwise
               returns False and displays Exception
    """
    def create(self, data):
        
        # Verify collection exists
        if data is not None:
            self.dbase.animals.insert_one(data, {"_id":0})
            # Inserts record into currently selected database and animals collection
            print('Record Inserted')
            # Displays msg confirming successful insertion  
            return True
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    """Method: Read
       Purpose: This is the read method to find specific record(s)
       Input: Data parameter which is the record(s) to find
       Output: Prints list of data matching data parameter
    """            
    def read(self, data):  
        
        # Verify a parameter to search for is given
        if data is not None:
            animalsCollection = self.dbase.animals.find(data)
            # Return collection as variable
            # Print animalsCollection cursor for dict key/value pairs
            return animalsCollection
            for animal in animalsCollection:
                print(animal)
                
        else:
            raise Exception("No search data provided - please try again")
            
    """Method: Update
       Purpose: This is the update method to alter record(s)
       Input: 2 parameters - 1st is query in key-value pair format for record(s) to find/update
              and 2nd parameter is key-value for desired update
       Output: Returns formatted string with JSON info for number of documents updated and True
               or Exception with False if failure to provide parameters
    """    
    def update(self, query, record):
        
        # Verify a parameter to search for is given
        if (query and record) is not None:
            # Takes two parameters - first query parameter for item you wish to update 
            # Second parameter is the $set command and key-value pair for your desired updated value 
            update_result = self.dbase.animals.update_many(query, record)
            # Return message containing text + variable with modified records count
            result = "Document(s) updated: " + str(update_result.modified_count)
            return result
            return True
        
        else:
            raise Exception("No record or update data provided - please try again")
            
    """Method: Delete
       Purpose: This is the delete method to delete records
       Input: Data parameter which is the key-value pair identifying a record(s) to eliminate
       Output: Returns formatted string containing number of documents deleted and True or 
               Exception with False if failure to provide parameters properly
    """   
    def delete(self, data):       
        
        # Verify a parameter/data is given to delete
        if data is not None:
            # Variable corresponding to command to delete data
            delete_result = self.dbase.animals.delete_many(data)
            # Print msg with # of documents deleted using variable from above
            result = "Document(s) deleted: " + str(delete_result.deleted_count)
            return result
            return True
        
        else:
            raise Exception("No record provided - please try again")