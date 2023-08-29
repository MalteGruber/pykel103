from kel103 import KEL103
import time
"""
Open device, ensure you have the matching baudrate on the KEL103
On the KR103 Press SHIFT, then the 0/COMM button and change to a baudrate, then press Enter.
"""
d=KEL103("/dev/ttyACM0",9600)

"""
Setting the current will set the function to CC,
setting the voltage will enable CV and so on..
"""
d.set_current(0.0)
input("Ensure you are safe to enable load? Press enter to continue")
d.enable()
for i in range(10):
    d.set_current(0.001)
    time.sleep(0.5)
    d.set_current(1.001)
    time.sleep(0.5)
    print(f"{d.get_voltage()}V {d.get_current()}A {d.get_power()}W")
d.disable()
d.close()