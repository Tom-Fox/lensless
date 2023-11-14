from serial import Serial
from pyubx2 import UBXReader

def getGPS():

    #更新获取GPS代码
    # gps = [35.710835661046396, 139.7603010534206]
    
    stream = Serial('/dev/ttyUSB0', 9600, timeout=3)
    ubr = UBXReader(stream)

    (raw_data, parsed_data) = ubr.read()
    while type(parsed_data) == str:
        (raw_data, parsed_data) = ubr.read()

    while parsed_data.identity != 'NAV-POSLLH':
        (raw_data, parsed_data) = ubr.read()
        while type(parsed_data) == str:
            (raw_data, parsed_data) = ubr.read()

    gps = [parsed_data.lat, parsed_data.lon]

    print('got GPS')
    return gps