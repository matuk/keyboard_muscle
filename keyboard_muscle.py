import sys
import random
import timeit

number_trials = int(sys.argv[1])

hard_keys = "!@#$%ˆ&*()_+-=[]{};:',<.>/?~äöüÄÖÜzZyY"
hard_keys_list = list(hard_keys)
hard_keys_list.append('"')

number_correct = 0
average_time = 0

for i in range(number_trials):
    k = random.choice(hard_keys_list)
    start = timeit.default_timer()
    user_input = input(k+": ")
    end = timeit.default_timer()
    average_time += end - start
    if user_input == k:
        number_correct += 1

percentage_correct = 100 * number_correct / number_trials
print("Percentage of correct answers: {:6.1f} %".format(percentage_correct))
print("Average answering time: {:6.1f} s".format(average_time))

with open("results.txt", "a+") as file:
    file.write("{:6.1f}; {:6.1f}".format(percentage_correct, average_time))
