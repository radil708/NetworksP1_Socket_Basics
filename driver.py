#!/usr/bin/env python3

from socket_functions import *

def main():
    m_sock = create_ssl_socket(HOST, PORT, TIMEOUT_VAL_SEC)
    send_msg(m_sock, "cs5700spring2022 HELLO adil.r\n" )
    rec1 = receive_msg(m_sock)
    print("\nReceiving and Solving Expressions...\nPlease Wait...\n")

    while "EVAL" in rec1:
        removed_frame = rec1.lstrip("cs5700spring2022 EVAL ")
        new_tree = txpr_tree(removed_frame)
        sol_list = new_tree.solve_tree_xpr()

        if sol_list[0] == "Passed":
            tree_solution = sol_list[1]
            sltn_string ="cs5700spring2022 STATUS " + str(tree_solution) + "\n"
            encoded_sltn = sltn_string.encode("ascii")
            m_sock.send(encoded_sltn)

        else:
            error_msg = "cs5700spring2022 ERR #DIV/0\n"
            encoded_error = error_msg.encode("ascii")
            m_sock.send(encoded_error)

        rec1 = receive_msg(m_sock)

    print("All expressions solved\nDisplaying Secret Flag Message:")
    print(rec1)

    print("\nClosing Socket\n")
    m_sock.close()

    print("Socket Succesfully Closed")

main()