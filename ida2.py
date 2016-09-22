def record(s, e, g, h):
    if h == 0:
        print('Usando PDB 2')
    elif h == 1:
        print('Usando manhattan')
    elif h == 2:
        print("Usando PDB 4")
    print("Largo de la solución: %5d" % s)
    print("Nodos expandidos:     %5d" % e)
    print("Nodos generados:      %5d" % g)
    print("")


def ida(state, h):
    # h = 0 maximo entre las Pdb
    # h = 1 manhattan
    state.parent = None
    expanded = 0
    generated = 0

    def search(state, g, f_bound, exp, gen):
        exp += 1
        f_state = g + state.heuristic(h)
        if f_state > f_bound:
            return None, f_state, exp, gen
        if state.check_goal():
            return state, f_state, exp, gen
        minim = 10000000
        for child in state.get_children():

            gen += 1
            goal, new_f_bound, exp, gen = search(child, g + 1, f_bound, exp, gen)
            if goal is not None:
                return goal, new_f_bound, exp, gen
            if new_f_bound < minim:
                minim = new_f_bound



        return None, minim, exp, gen


    f_bound = state.heuristic(h)
    if state.check_goal():
        return state
    while True:
        goal_found, new_f_bound, expanded, generated = search(state, 0, f_bound,
                                                            expanded, generated)
        if goal_found is not None:
            break
        if f_bound == 10000000:
            return False
        f_bound = new_f_bound

    size = goal_found.solution_length()
    record(size, expanded, generated, h)
    return goal_found
