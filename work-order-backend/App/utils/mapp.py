class Mapp:
    def toDynamo(data):
        newDynamoJsonObject = {}
        for key in data:
            if ( type(data[key]) is str ):
                newDynamoJsonObject[key] = { 'S' : data[key]}
        
        return newDynamoJsonObject
    

