import subprocess, sys

def run_process(cmd):
	try:
		subprocess.check_call(cmd)
	except KeyboardInterrupt, e:
		sys.exit(1)
	except:
		pass

cmd = ['python', 'emrun.py'] + sys.argv[1:] + ['--safe_firefox_profile', 'index.html', 'autorun']
run_process(cmd)
