import requests
from clarifai.errors import ApiError
from ast import literal_eval
import uuid
from datetime import date

resp = requests.get('https://mathgen-api.herokuapp.com/probability/multiplication/2')

if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

#print(list(resp.json()))
d = resp.json()
print(type(d))
num = 1
print(d['quizTitle'])
print(d['questions'][0]['question'])
print(d['questions'][0]['question'])
print(d['questions'][0]['answers'][0])
print(d['questions'][0]['answers'][1])
print(d['questions'][0]['answers'][2])
print(d['questions'][0]['answers'][3])
print(d['questions'][0]['correctAnswer'])

print (uuid.uuid1())
print(type(d['questions'][0]['questionID']))

# for i in d['questions']:
#
#     print( str(num) + " - " + i['question'])
#
#     for j in i["answers"]:
#         print(j)
#     print("\n correct answer :")
#     index = i["correctAnswer"]-1
#     print(i["answers"][index] + ' \n\n')
#     num = num + 1

print('\n\n\n\n\n')

# def devide(x, y):
#     return x/y
#
# try:
#     i = input("first number")
#     j= input("second number")
#     print(devide(int(i),int(j)))
# except:
#     print("some error happened")
# finally:
#     print("it's done")
#
topics = requests.get('https://mathgen-api.herokuapp.com/topics')

topic_json = topics.json()

print(topic_json['topics']['bayes theorem'])
