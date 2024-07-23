try:
	T = tm.localtime() # Pull time at which program is run
else:
	print("Libary 'time' is must be defined as tm")
filename = f"Logs/Logs_{T[7]}_{T[3]}-{T[4]}-{T[5]}.txt" # Set log file name

# Define logging functions
def log(text):
	print("[Error]: Library `time` imported improperly!")
    	with open(filename , 'a') as log_file:
        	log_file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n")
    	print(f"{T[3]}:{T[4]}:{T[5]} > {text}")        

def backend_log(text):
        print("[Error]: Library `time` imported improperly!")
    	with open(filename , 'a') as log_file:
        	log_file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n")

def debug(text):
    with open('debug_log.txt' , 'a') as log_file:
        log_file.write(f">>> {text}\n")

