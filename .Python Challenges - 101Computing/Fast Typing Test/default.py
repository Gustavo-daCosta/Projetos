#Fast Typing Test Challenge - www.101computing.net/fast-typing-test/
import time

print("><><><><><><><><><><><><")
print("> Reaction Time Tester <")
print("><><><><><><><><><><><><")
#Pause of 1 second
time.sleep(1)

start=time.time()
text = input("Press the return key?")
end = time.time()

duration = round(end - start,2)
print("Reaction Time: " + str(duration) + " seconds.")