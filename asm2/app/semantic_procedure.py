class Procedure:
    def __init__(self, typ, value : str):
        self.type = typ
        self.value = value
        
    def __str__(self) -> str:
        return self.value
    
def create_semantic_procedure(tree):
    gap = '?' + str(tree.label()["GAP"])
    logical_form = tree.label()['SEM']
    
    # For example: [<ApplicationExpression TRAVEL1(SOURCE(NAME(h2,'HCMC'),h2),DEST(NAME(n2,'NT'),n2),t1)>, <ApplicationExpression WH(t1,HOW1)>]
    travel_exp, wh_exp = logical_form.args
    wh_type = [wh.name for wh in wh_exp.constants()][0] # Get question type
    
    procedure = Procedure(wh_type, "")
    t = '?'
    
    if wh_type == 'LIST1':
        # Get all tours
        procedure.value = "(PRINT-ALL {} (TOUR {}))".format(gap, gap)
    elif wh_type == 'HOW1': 
        # Create how-long procedure
        source_exp, dest_exp, _ = travel_exp.args
        source, dest = list(source_exp.constants())[0].name.replace("'",""), list(dest_exp.constants())[0].name.replace("'","")
        
        t += [variable.name for variable in dest_exp.variables()][0]
        tour = "(TOUR {} {})".format(dest, t)
        procedure.tour_code = dest
        procedure.source = source
        procedure.dest = dest
        
        source = "(DTIME {} {} {})".format(t, source, gap)
        dest = "(ATIME {} {} {})".format(t, dest, gap)
        run_time = "(RUN-TIME {})".format(t)
        procedure.value = "(PRINT-ALL {} {} {} {} {})".format(t, tour, run_time, source, dest)
    elif wh_type == 'HOW2':
        # How-many procedure
        dest_exp, _ = travel_exp.args
        dest = list(dest_exp.constants())[0].name.replace("'","")
        procedure.tour_code = dest
        
        tour = "(TOUR {} {})".format(dest, gap)
        procedure.value = "(PRINT-ALL {} {})".format(gap, tour)
    elif wh_type == 'WHICH1':
        # By transportation procedure
        dest_exp, _ = travel_exp.args
        dest = list(dest_exp.constants())[0].name.replace("'","")
        procedure.tour_code = dest
        
        t += [variable.name for variable in dest_exp.variables()][0]
        tour = "(TOUR {} {})".format(dest, t)
        by = "(BY {} {})".format(t, gap)
        procedure.value = "(PRINT-ALL {} {} {})".format(gap, tour, by)
    elif wh_type == 'WHAT1':
        # Schedule procedure
        dest_exp, _ = travel_exp.args
        dest = list(dest_exp.constants())[0].name.replace("'","")
        procedure.tour_code = dest
        t += [variable.name for variable in dest_exp.variables()][0]
        tour = "(TOUR {} {})".format(dest, t)
        dtime = "(DTIME {} HCMC {})".format(t, gap)
        procedure.value = "(PRINT-ALL {} {} {})".format(gap, tour, dtime)
        
    return procedure
        