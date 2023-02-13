class Converter():
    def __init__(self):
        self.convertionTableLength = {"mm":25.4, "cm":2.54, "m":0.0254, "feet":0.0833, "inch":1 } 
        self.convertionTableVolume ={"pint":1.759754, "dl":10, "ml":1000, "quart": 0.8798771, "L":1}

    def convert(self, numberToConvert, fromm, to):
        lengthUnits = ["mm", "cm", "m", "feet", "inch"]
        volumeUnits = ["pint", "dl", "ml", "quart", "L"]
        if fromm in lengthUnits and to in lengthUnits:
            answer = numberToConvert * 1/self.convertionTableLength[fromm] * self.convertionTableLength[to]
            print(answer)
            return answer

        if fromm in volumeUnits and to in volumeUnits:
            answer = numberToConvert * 1/self.convertionTableVolume[fromm] * self.convertionTableVolume[to]
            print(answer)
            return answer
        else:
            print("Error could not convert from " + fromm)

numberToConvert = float(input("Convert: "))
unitFrom = input("-inn: ")
unitTo = input("-out: ")

converter = Converter()
converter.convert(numberToConvert, unitFrom, unitTo)
