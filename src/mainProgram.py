# read argument to decide how the program work.
# py mainProgram.py [testMode] [model_name]
# mode 0: train a new model / input a train model and keep training
# mode 1: use the model to find result. output id and answer
# mode 2: use the model, output reference story id and structure distances
# mode 3: ???
# mode 4: test the accuracy

import sys
import subprocess
import step_4_checkAnswer_function
from random import randint
import operator


population = []

iter = 0
full = 5
def generateNew(full, target):
    for iter in range(1, full+1):
        if iter > len(target):
            temp = []
            temp.append(randint(int(sys.argv[1]),int(sys.argv[2])))
            temp.append(randint(int(sys.argv[1]),int(sys.argv[2])))
            temp.append(randint(int(sys.argv[1]),int(sys.argv[2])))
            #print(temp)
            target.append(temp)
        
        iter = iter +1;
    return target
        
result = {}
target = []
population = []
end = 0
current_number = -1
while (len(population)<3) and end == 0:
    population = generateNew(full, population)
    print(population)
    test_count = 0
    for e in population:
        tail_string = str(e[0])+"_"+str(e[1])+"_"+str(e[2])
        new_output = "../Dataset/result/result_"+tail_string+".json"
        if test_count > current_number: 
            subprocess.call([
            "py", "step_3_method4.py",
            "./trained_model/model_1000.doc2vec",
            "../Dataset/testSet/test0.json",
            new_output,
            str(e[0]),
            str(e[1]),
            str(e[2])],
            shell=True
            )
        test = step_4_checkAnswer_function.checkFunction('../Dataset/testSet/answer0.json', new_output)
        #print(tail_string, ": ", test)
        result[tail_string] = str(test)
        test_count = test_count +1
    sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse = True)
    print(sorted_x)
    
    
    i = 0
    check_value =520
    check_count =0
    population = []
    for check in sorted_x:
        # preserve first 3
        if i < 2:
            #print(check)
            temp_value = check[0].split("_")
            temp_value[0] = temp_value[0].replace("_","")
            temp_value[1] = temp_value[1].replace("_","")
            temp_value[2] = temp_value[2].replace("_","")
            
            temp = []
            temp.append(int(temp_value[0]))
            temp.append(int(temp_value[1]))
            temp.append(int(temp_value[2]))
            population.append(temp)
            #print("2:")
            #print(population)
            
        #if i == 0:
        #   check_value = check[1]
        #else:
        if int(check[1]) > check_value:
            check_count = check_count+1
            
        i = i+1
    if check_count >2:
        end = 1
        print("\n\n should end")
        
    result = {}
    current_number = 1