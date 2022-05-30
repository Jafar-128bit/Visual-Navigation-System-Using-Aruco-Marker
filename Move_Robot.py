import Network_module


class motion:
    @staticmethod
    def forwardMotion(url):
        Network_module.moveRobot(order=1, address=url)

    @staticmethod
    def BackwardMotion(url):
        Network_module.moveRobot(order=2, address=url)

    @staticmethod
    def LeftMotion(url):
        Network_module.moveRobot(order=3, address=url)

    @staticmethod
    def RightMotion(url):
        Network_module.moveRobot(order=4, address=url)

    @staticmethod
    def Stop(url):
        Network_module.moveRobot(order=5, address=url)
