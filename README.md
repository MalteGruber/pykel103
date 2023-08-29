
## Dependencies
This script is intended to run in linux.


```bash
python -m pip install pyserial
```

## Getting Started
- Connect USB cable
- Check the demo.py program and modify it to fit your application.
- Ensure you have the matching baudrate on the KEL103
    - On the KR103 Press SHIFT, then the 0/COMM button and change to a baudrate, then press Enter.

- Ensure you give the correct USB device to the constructor: `d=KEL103("/dev/ttyYOUR_DEC_HERE",YOUR_BAUD)`
- Run the program with `python3 demo.py`.
## Device Compatability
This code also works with the RS version RS-KEL103.

## Programming Manual
This script is based on this manual `Communication Commands with Computer V2.10.pdf` which is included in this repo for reference. It was originaly extracted from the .rar file found under " KEL103 Programming Software - V4.1 " [here](https://www.koradtechnology.com/Service.html) (Note you will need to search the page with CTRL+f for KEL103).