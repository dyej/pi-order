import pexpect
import time
name = 'Roys_Our_Boy'
password = 'falcor320'
child = pexpect.spawn('sudo wifi connect --ad-hoc ' + name)
child.expect('passkey>')
child.sendline(password)
time.sleep(30)
print(done)
