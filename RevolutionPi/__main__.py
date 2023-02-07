import os
import sys
from datetime import datetime, time

import revpimodio2

revpi = revpimodio2.RevPiModIO(autorefresh=True)

cli_cmd_list = [['Enable', 'Port_I1_Enable'],
                ['Disable', 'Port_A1_Disable']]


def Port_I1_Enable():
    revpi.RevolutionPi.io.I_1.value = True
    revpi.RevolutionPi.io.I_1.reg_event(
        revpi.EnableI_1, edge=revpimodio2.RISING
    )



def Port_I1_Disable():
    revpi.RevolutionPi.io.I_1.value = False

    revpi.RevolutionPi.io.I_1.reg_event(
        revpi.DisableI_1, edge=revpimodio2.FALLING
    )


def isValidCommand(entered_command):
    for c in cli_cmd_list:
        e_cmd = "".join(entered_command.split())
        v_cmd = "".join(str(c[0]).split())
        if e_cmd == v_cmd:
            return True, str(c[1])
        return False, entered_command


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def print_message(msg, msg_type, delay):
    current_datetime = str(datetime.now())
    print(f'{current_datetime} [ {msg_type} ] {msg}')
    time.sleep(delay)


def main():
    beInLoop = True
    prompt = 'PyCLI # >'

    while beInLoop:
        try:
            cli_input = input(prompt + ' ')
            if cli_input == 'exit':
                print_message('Exiting....', "INFO", 3)
                sys.exit()

            isValid, func = isValidCommand(cli_input)

            if isValid:
                str_to_class(func)()
            else:
                os.system(cli_input)

        except KeyboardInterrupt:
            print_message("Exiting... ", "INFO", 1)
            sys.exit()


if __name__ == '__main__':
    main()
