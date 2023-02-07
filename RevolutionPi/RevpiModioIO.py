import revpimodio2


class RevPiModIO:
    def __init__(self):
        # Instantiate RevPiModIO2 and handle "program exit" signal
        self.RevolutionPi = revpimodio2.RevPiModIO(autorefresh=True)

    @staticmethod
    def RevPiExit(self):
        """This function is executed just before exit the program."""
        self.RevolutionPi.core.A1 = revpimodio2.OFF

    @staticmethod
    def EnableI_1(self):
        self.RevolutionPi.io.I_1.value = True

        self.RevolutionPi.io.I_1.reg_event(
            self.EnableI_1, edge=revpimodio2.RISING
        )

    def DisableI_1(self):
        self.RevolutionPi.io.I_1.value = False

        self.RevolutionPi.io.I_1.reg_event(
            self.DisableI_1, edge=revpimodio2.FALLING
        )
