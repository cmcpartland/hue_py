class LightState:
    """
    LightState is an internal class that allows you to reactively set the properties on a light.
    Don't use this class directly, instead use the methods on the `HueLight` or `HueGroups` classes.
    """
    def __init__(self, state, bind_to=None):
        self.light = bind_to
        self.__brightness = state.get('bri')
        self.__hue = state.get('hue')
        self.__saturation = state.get('sat')
        self.__is_on = state.get('on')
        self.__reachable = state.get('reachable')

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, bri):
        self.__brightness = bri
        if self.light:
            self.light.set_state({'bri': bri})

    @property
    def color(self):
        return self.__hue, self.__sat

    @color.setter
    def color(self, color):
        hue, sat = color
        self.__hue = hue
        self.__sat = sat
        if self.light:
            self.light.set_state({'hue': hue, 'sat': sat})

    @property
    def hue(self):
        return self.__hue

    @hue.setter
    def hue(self, hue):
        self.__hue = hue
        if self.light:
            self.light.set_state({'hue': hue})

    @property
    def saturation(self):
        return self.__saturation
        
    @property
    def reachable(self):
        return self.__reachable

    @saturation.setter
    def saturation(self, sat):
        self.__saturation = sat
        if self.light:
            self.light.set_state({'sat': sat})

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, on):
        self.__is_on = on
        if self.light:
            self.light.set_state({'on': on})

    def to_payload(self):
        payload = {
            'bri': self.brightness,
            'sat': self.saturation,
            'hue': self.hue,
            'on': self.is_on,
            'reachable': self.reachable
        }
        return payload
