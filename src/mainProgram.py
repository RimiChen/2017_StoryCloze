# read argument to decide how the program work.
# py mainProgram.py [testMode] [model_name]
# mode 0: train a new model / input a train model and keep training
# mode 1: use the model to find result. output id and answer
# mode 2: use the model, output reference story id and structure distances
# mode 3: ???
# mode 4: test the accuracy

import subprocess
subprocess.Popen("step_1_sentence_label.py ../Dataset/trainigSet_Test.csv", shell = True)