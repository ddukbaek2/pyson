#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from __future__ import annotations
import json


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
null : object = None
true : bool = True
false : bool = False


# # 생성 및 불러오기, 저장하기 등.
# # document : dict = pyson.CreatePYSON()
# # pysonText : str = pyson.ConvertJSONTextToPYSONText(jsonText)
# # document : dict = pyson.CreatePYSONFromPYSONFile("data.pyson")
# # document : dict = pyson.CreatePYSONFromPYSONText("document = { \"isTrue\": false }")
# # pysonText : str = pyson.WritePYSONToPYSONText(document)
# # pyson.WritePYSONToPYSONFile(document, "data.pyson")

# # json 으로 변환 및 불러오기, 저장하기 등.
# # jsonText : str = pyson.ConvertPYSONTextToJSONText(pysonText)
# # document : dict = pyson.CreatePYSONFromJSONFile("data.json")
# # document : dict = pyson.CreatePYSONFromJSONText("{ \"isTrue\": false }")
# # jsonText : str = pyson.WritePYSONToJSONText(document)
# # pyson.WritePYSONToJSONFile(document, "data.json")

# # 객체화.
# # obj = pyson.Deserialize(document)
# # obj.a == 1.0

# # 검색.
# # value = document["data.e[data.e.count - 1]"] # value is 9

# # 주석달기.
# document : dict = {
# 	"data": { # object
# 		"a": 1.0, # a is number
# 		"b": null, # b is null
# 		"c": true, # c is true
# 		"d": "tsawsdfasdfasdfasdfasdfasdfasdfasdf", # d is string
# 		"e": [1, 2, 3, 4, 5, 6, 7, 8, 9], # array
# 		"f": {

# 		}
# 	}
# }

# #------------------------------------------------------------------------
# # JSON 데이터.
# #	- JSONData는 dict와 동일하다.
# #------------------------------------------------------------------------
# class JSONData:

# 	def HasField(self, name : str) -> bool:
# 		return hasattr(self, name)

# 	def GetField(self, name : str) -> object:
# 		return getattr(self, name, None)

# 	def SetField(self, name : str, value : object):
# 		setattr(self, name, value)

# 	def RemoveField(self, name : str):
# 		delattr(self, name)


# #------------------------------------------------------------------------
# # JSON 변환기.
# #------------------------------------------------------------------------
# class JSONConverter:
# 	@staticmethod
# 	def Create(data : dict) -> JSONData:
# 		jsonData = JSONData()
# 		for name, value in data.items():
# 			if isinstance(value, dict):
# 				jsonData.SetField(name, JSONData.Create(value))
# 			elif isinstance(value, list):
# 				newValue = list()
# 				for val in value:
# 					if isinstance(value, dict, list):
# 						newValue.append(JSONData.Create(val))
# 					else:
# 						newValue.append(val)
# 				jsonData.SetField(name, newValue)
# 			else:
# 				jsonData.SetField(name, value)
# 		return jsonData
	
# 	@staticmethod
# 	def ToDictionary(jsonData : JSONData) -> dict:
# 		dictionary = dict()
# 		for name in dir(jsonData):
# 			if not name.startswith("__") and not callable(getattr(jsonData, name)):
# 				value = getattr(jsonData, name)
# 				if isinstance(value, JSONData):
# 					dictionary[name] = value.ToDictionary()
# 				elif isinstance(value, list):
# 					dictionary[name] = [val.ToDictionary() if isinstance(val, JSONData) else val for val in value]
# 				else:
# 					dictionary[name] = value
# 		return dictionary

# 	@staticmethod
# 	def Serialize(jsonData : JSONData) -> str:
# 		jsonDictData = jsonData.ToDictionary()
# 		jsonTextData = json.dumps(jsonDictData, indent = 4, ensure_ascii = False)
# 		return jsonTextData
	
# 	@staticmethod
# 	def Deserialize(jsonTextData : str) -> JSONData:
# 		jsonDictData = json.loads(jsonTextData)
# 		return JSONData.Create(jsonDictData)