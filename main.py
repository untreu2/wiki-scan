import subprocess

times = input("How many times do you wanna run the code?")

t = int(times)

for x in range(t):
  subprocess.run(["python", "scan.py"])

print("Finished.")