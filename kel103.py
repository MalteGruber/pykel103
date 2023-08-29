import serial
class UsbCommKel103:
    def __init__(self,usb_dev,baudrate=115200):
        self.usb_dev = usb_dev
        self.baudrate = baudrate
        self.ser = None
        self.open()
    
    def open(self):
        self.ser = serial.Serial(self.usb_dev,self.baudrate)
        self.ser.timeout=1
        self.ser.flushInput()
        self.ser.flushOutput()
    def close(self):
        self.ser.close()
    
    def send_str(self,cmd):
        cmd+="\n"
        self.ser.write(cmd.encode())
    def read(self):
        return self.ser.read()

        

    def readline(self):
        line=b''
        while True:
            a=self.read()
            #print(a)
            if a==b'':
                break
            if a==b'':
                break
            line+=a
        return line.decode().strip()

class KEL103(UsbCommKel103):
    FUNC_VOLTAGE="VOLT"


    def __init__(self,usb_dev,baudrate=115200):
        super().__init__(usb_dev,baudrate)
        
        if 0:
            identity=self.get_identity()
            
            if "KEL103" not in identity:
                print("WARNING: Could not establish device identity using *IDN? command.")
            else:
                print(f"Found load: {identity}")
    def get_identity(self):
        cmd="*IDN?"
        self.send_str(cmd)
        return self.readline()
    
    def set_resistance(self,resistance):
        cmd=":RES %fOHM" % resistance
        self.send_str(cmd)
    def set_current(self,current):
        cmd=":CURR %fA" % current
        self.send_str(cmd)
    def set_power(self,power):
        cmd=":POW %fW" % power
        self.send_str(cmd)
    def enable(self,on=True):
        cmd=":INP OFF"
        if on:
            cmd=":INP ON"
        self.send_str(cmd)
    def disable(self):
        cmd=":INP OFF"
        self.send_str(cmd)
    def set_voltage(self,voltage):
        cmd=":VOLT %fV" % voltage
        self.send_str(cmd)
    def set_beep_on(self,on=True):
        cmd=":BEEP OFF"
        if on:
            cmd=":BEEP ON"
        cmd=":SYST"+cmd
        self.send_str(cmd)


    def _get_unit_stripped_str(self,data):
        try:
            return float(data[:-1])
        except:
            return None
    def get_voltage(self):
        cmd=":MEAS:VOLT?"
        self.send_str(cmd)

        return self._get_unit_stripped_str(self.readline())

    def get_current(self):
        cmd=":MEAS:CURR?"
        self.send_str(cmd)
        return self._get_unit_stripped_str(self.readline())

    def get_power(self):
        cmd=":MEAS:POW?"
        self.send_str(cmd)
        return self._get_unit_stripped_str(self.readline())


    """Not working..
    #Steps [{"setpoint":0.5,"slope":0.1,"time":1.0,unit:"A"}]
    def step_output(self, steps):
        #:LIST 2, 3A,2,1A,0.1A/uS,5S,2A,0.1A/uS,5S,3
        #:LIST 2, 3A,2,1A,0.1A/uS,5S,1A,0.1A/uS,5S,3
        cmd=f":LIST 2,\n 3A,2,"

        for step in steps:
          
            cmd+=f"{step.get('setpoint')}{step.get('unit')},{step.get('slope')}{step.get('unit')}/uS,{step.get('time')}S,"
        cmd=cmd[:-1]
        cmd+=",3"
        print(cmd)
        self.send_str(cmd)
    def get_list(self):
        cmd=":RCL:LIST 2"
        self.send_str(cmd)
        return self.readline()
    """
