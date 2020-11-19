while True:
    bus.write_byte(address, A0)
    value = bus.read_byte(address)
    if value >= THRESHOLD:
        print('Warning', value)
         TODO: broadcast to other pi
    time.sleep(0.1)