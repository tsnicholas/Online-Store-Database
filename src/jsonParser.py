import json

class JsonParser:
    def getFileData(filePath):
        fileData = ""
        with open(filePath, encoding = "utf8") as file:
            fileData = json.load(file)
        return fileData
    