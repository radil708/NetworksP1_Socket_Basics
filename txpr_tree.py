from txpr_node import t_node
class txpr_tree:

    def __init__(self, string_expr : str):
        self.root = t_node()
        (self.root).build_helper(string_expr)

    def solve_tree_xpr(self) -> list:
        status = "Failed"
        try:
            solved = (self.root).node_solve_txpr()
            status = "Passed"
            return [status, solved]
        except ZeroDivisionError:
            solved = 0
            return [status, solved]





