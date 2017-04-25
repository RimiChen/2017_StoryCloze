# check answer
import sys
import json
import io
import re


result = {}
correct_answer = {}

correct_count = 0

answer_file =  sys.argv[1]
result_file =  sys.argv[2]

with open(answer_file) as answer_file:

    answerSet = json.load(answer_file)
    for e in answerSet:
        for k, v in e.items():
            correct_answer[k] = v

with open(result_file) as result_file:
    resultSet = json.load(result_file)
    for e in resultSet:
        for k, v in e.items():
            result[k] = v
            
            
for item in result:
    if correct_answer[item] == result[item]:
        correct_count = correct_count + 1
        
print("correct: ", correct_count)