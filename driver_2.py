#!/usr/bin/env python3
import sys
from socket_functions import *

DEFAULT_PORT = 27995
TIMEOUT = 20
FIRST_MSG_PREFIX = "cs5700spring2022 HELLO "

def display_arg_error(list_args : list):
    print("ERROR: Number of arguments incorrect:\n"
          "EXPECTED FORMATS are either:\n"
          "1.) <-p port> <-s> [hostname] [NEU email prefix]\n"
          "2.) <-s> [hostname] [NEU email prefix]\n"
          "ACTUAL was: {}".format(" ".join(list_args)))

def handle_address_arg(host_arg : str) -> str:
    if "network" in host_arg:
        return socket.gethostbyname("project1.5700.network")
    else:
        return host_arg


def handle_args():
    all_args = sys.argv[1:]
    dict_arguments = {}
    dict_arguments["Status"] = False

    if "-s" not in all_args:
        print("ERROR: encryption flag not detected!\n"
              "Please retry call with required '-s' argument")
        return dict_arguments

    if all_args[0] == "-p":
        dict_arguments["port"] = int(all_args[1])

        if len(all_args) < 5 or len(all_args) > 5:
            display_arg_error(all_args)
            return dict_arguments

        dict_arguments["host"] = all_args[3]
        dict_arguments["NEU"] = all_args[4]
        dict_arguments["Status"] = True
        return dict_arguments
    else:
        dict_arguments["port"] = DEFAULT_PORT

        if len(all_args) < 3 or len(all_args) > 3:
            display_arg_error(all_args)
            return dict_arguments

        dict_arguments["host"] = all_args[1]
        dict_arguments["NEU"] = all_args[2]
        dict_arguments["Status"] = True
        return dict_arguments


def arg_checkstep():
    my_dict = handle_args()
    if my_dict["Status"] == False:
        print("Program FAILED; Exiting Process")
        return
    else:
        print("-------------------------")
        m_sock = create_ssl_socket(socket.gethostbyname(my_dict["host"]), my_dict["port"], TIMEOUT)
        first_sendout_str = FIRST_MSG_PREFIX + my_dict["NEU"] + "\n"

        send_msg(m_sock, first_sendout_str)
        rec1 = receive_msg(m_sock)
        print("\nReceiving Expressions\nPlease Wait...")

        while "EVAL" in rec1:
            removed_frame = rec1.lstrip("cs5700spring2022 EVAL ")
            new_tree = txpr_tree(removed_frame)
            sol_list = new_tree.solve_tree_xpr()

            if sol_list[0] == "Passed":
                tree_solution = sol_list[1]
                sltn_string = "cs5700spring2022 STATUS " + str(tree_solution) + "\n"
                encoded_sltn = sltn_string.encode("ascii")
                m_sock.send(encoded_sltn)

            else:
                error_msg = "cs5700spring2022 ERR #DIV/0\n"
                encoded_error = error_msg.encode("ascii")
                m_sock.send(encoded_error)

            rec1 = receive_msg(m_sock)

        if "Unknown_Husky_Id" in rec1:
            print("NEU argument: [{}] is an UNKNOWN NEU user".format(my_dict["NEU"]))
            print("Program Exiting")
            print("\nClosing Socket...")
            m_sock.close()
            print("Socket Succesfully Closed")
            return

        else:
            print("\nAll expressions solved\n\nDisplaying Secret Flag Message:")
            print(rec1)

        print("\nClosing Socket...")
        m_sock.close()

        print("Socket Succesfully Closed")





    #port_selected =


arg_checkstep()