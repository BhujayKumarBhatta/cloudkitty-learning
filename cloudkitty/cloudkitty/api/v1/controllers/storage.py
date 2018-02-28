import pecan
from pecan import expose

class DataFramesController(object):
   
    @expose()
    def index(self):
        dataframes = []
        dataframe = "Testing DataFramesController class"
        dataframes = dataframes.append(dataframe)
        return  "dataframe home page"



class StorageController(object):

    @expose()
    def index(self):
        return "Storage Controller Home page"

    dataframes = DataFramesController()
