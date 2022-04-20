B1 = 'i'
B2 = 'o'

class TV:
    def __init__(self):
        self.state = 'power_off'
        self.poweron = 0

    def power(self):
        if self.poweron == 0:
            self.idle()
            self.poweron = 1
            print('TV on')
        elif self.poweron == 1:
            self.state = 'power_off'
            self.poweron = 0
            print('TV off')
    
    def volume(self, x):
        self.state = 'volume'
        B3 = 'io'

        y = input('Press "i" to increase volume or "o" to decrease volume, or "' + B3 + '" to stop changing volume\n')

        while 1:
            if y == B1:
                print('volume+')
            elif y == B2:
                print('volume-')
            elif y == B3:
                self.idle()
                return
            else:
                self.error()
                return

            y = input()

        self.idle()

    def channel(self, x):
        self.state = 'channel'
        B3 = 'oi'

        y = input('Press "i" to increase volume or "o" to decrease volume, or "' + B3 + '" to stop changing channel\n')

        while 1:
            if y == B1:
                print('channel+')
            elif y == B2:
                print('channel-')
            elif y == B3:
                self.idle()
                return
            else:
                self.error()
                return

            y = input()

        self.idle()

    def brightness(self, x):
        self.state = 'brightness'
        B3 = 'ii'

        y = input('Press "i" to increase volume or "o" to decrease volume, or "' + B3 + '" to stop changing brightness\n')

        while 1:
            if y == B1:
                print('brightness+')
            elif y == B2:
                print('brightness-')
            elif y == B3:
                self.idle()
                return
            else:
                self.error()
                return

            y = input()

        self.idle()

    def idle(self):
        self.state = 'idle'

    def error(self):
        if self.poweron == 0:
            print('TV not on')
            self.state == 'power_off'
        else:
            self.state = 'error'
            print('You have pressed an invalid button')
            self.idle()