import subprocess

# A process is an instance of a running program.

# subprocess.check_call()
# subprocess.call()
# subprocess.wait()
# subprocess.wait()
# subprocess.check_output()
# subprocess.Popen()

# subprocess.run(['python', '-m', 'http.server', '8000'], capture_output = True, text = True)
# subprocess.run(['python', 'other.py'], capture_output = True, text = True)

completed = subprocess.run(['ls', '-l'], capture_output = True, text = True)
# print(completed.stdout.decode())
# print(completed.stderr.decode())
print(completed.args)
print(completed.stdout)
print(completed.stderr)
print(completed.returncode)
print(completed.check_returncode())
