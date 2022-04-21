from simple_socket_package.mySimpleSocket import mySimpleSocketObj
from tree_expression_package.txpr_tree import txpr_tree
from project_constants import *


def main():
    # Create the socket
    socket_1 = mySimpleSocketObj(host_in= "project1.5700.network",port_in=27995,ssl_protocol=HW_1_SSL_PROTOCOL,timeout_sec=5)

    # initial hello
    socket_1.send_msg(DEFAULT_HELLO_MSG)
    decoded_msg =socket_1.rcv_msg(display_rcvd_msg=True,display_byte_received=True)

    while 'EVAL' in decoded_msg:
        # pre-process string before building tree, remove anything that is not the equation
        removed_frame = decoded_msg.lstrip("cs5700spring2022 EVAL ")
        removed_frame = removed_frame.rstrip("\n")

        # build the tree
        new_tree = txpr_tree(removed_frame)
        #solve the tree
        solution_lst = new_tree.solve_tree_xpr()

        if solution_lst[0] == "Passed":
            tree_solution = solution_lst[1]
            sltn_string = "cs5700spring2022 STATUS " + str(tree_solution) + "\n"
            # message needs to be sent as ascii encoded bytes
            socket_1.send_msg(msg_send=sltn_string,encoding_schema="ascii")
        else:
            socket_1.send_msg(msg_send=ZERO_ERROR_MSG_SEND,encoding_schema="ascii")


        decoded_msg = socket_1.rcv_msg(decoding_schema="ascii",display_byte_received=False,display_rcvd_msg=True)

    print("\nAll expressions solved\n\nDisplaying Secret Flag Message:")
    processed_final = decoded_msg.lstrip("cs5700spring2022 BYE ")
    processed_final = processed_final.rstrip("\n")
    print(processed_final)
    socket_1.close_connection()



main()