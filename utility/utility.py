import json




class Utility():

  def getjsondata(key, value):
        with open("testdata\\testdata.json", "r") as f:
            #data = json.load(f)
            data = json.loads(f.read())
            return(data[key][value])
    



