class Connector:
    def connect(self, other):
        pass


class HDMIConnector(Connector):
    pass


class PowerSocketConnector(Connector):
    pass


class EthernetConnector(Connector):
    pass


class Television(EthernetConnector, PowerSocketConnector, HDMIConnector):
    def __init__(self):
        self.hdmi_connector = HDMIConnector()
        self.power_connector = PowerSocketConnector()
        self.ethernet_connector = EthernetConnector()


class GameConsole(EthernetConnector, PowerSocketConnector, HDMIConnector):
    def __init__(self):
        self.hdmi_connector = HDMIConnector()
        self.power_connector = PowerSocketConnector()
        self.ethernet_connector = EthernetConnector()


class Router(EthernetConnector, PowerSocketConnector, HDMIConnector):
    def __init__(self):
        self.ethernet_connector = EthernetConnector()


tv = Television()
game_console = GameConsole()

tv.hdmi_connector.connect(game_console.hdmi_connector)
