import time as tm

def log(text):
	T = tm.localtime()
	with open(f"Logs_{T[7]}_{T[3]}-{T[4]}-{T[5]}.txt" , 'a') as log_file:
		log_file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}")
	print(f"{T[3]}:{T[4]}:{T[5]} > {text}")


def backend_log(text):
	T = tm.localtime()
	with open(f"Logs_{T[7]}_{T[3]}-{T[4]}-{T[5]}.txt" , 'a') as log_file:
		log_file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}")

