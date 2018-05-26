from math import fsum

class_dict = {}
class_ids =  []
report_dict = {}
default = 50

def create_class_content_dict(class_content):
    lines_arr = class_content.splitlines()

    for line in lines_arr:
        line_split =  line.split("|")

        id = line_split[0]
        lname = line_split[2]
        fname = line_split[1]

        class_dict[id] = lname+","+fname
        class_ids.append(id)

    return [class_dict,class_ids]

def individual_component(component_content):
     lines_arr = component_content.splitlines()
     max_point_value = lines_arr[0]
     lines_arr.remove(max_point_value)

     component_dict = {}

     for line in lines_arr:
        line_split =  line.split("|")

        id = line_split[0]
        marks = line_split[1]

        component_dict[id] = marks

     return [component_dict, max_point_value]

def component_average(component_content, component_name):

     lines_arr = component_content.splitlines()
     max_point_value = lines_arr[0]
     lines_arr.remove(max_point_value)

     marks = []
     total_marks = 0

     for line in lines_arr:
        line_split =  line.split("|")

        id = line_split[0]
        mark = line_split[1]
        marks.append(int(mark))
        total_marks = total_marks + int(mark)

     avg = total_marks / len(marks)

     return component_name + " average: " + str(format(avg, '.2f')) + "/" + max_point_value

def normalize_marks(component_name, component_marks, component_max_point):

    component_breakdown = dict(
                a1=7.5,
                a2=7.5,
                pr=25,
                t1=30,
                t2=30
               )

    component_percentage =  format((float(component_marks) / float(component_max_point)) * 100, '.2f')

    normalized_component_marks = format((float(component_breakdown[component_name])/float(100)) * float(component_percentage), '.2f')

    return float(normalized_component_marks)

def set_pass_fail_point(new_pass_fail):
    global  default
    default = new_pass_fail

def calc_final_letter_grade(gr):

    gr = int(gr)

    if gr >= default + 42:
        return "A+"
    elif gr >= default + 35 :
        return "A"
    elif gr >= default + 28 :
        return "A-"
    elif gr >= default + 21 :
        return "B+"
    elif gr >= default + 14 :
        return "B"
    elif gr >= default + 7 :
        return "B-"
    elif gr >= default :
        return "C"
    elif gr < default:
        return "Fail"

    else:
        return "0"

def standard_report(contents_dict, bool_new_pass_fail):

    if not bool_new_pass_fail:
        global  default
        default = 50

    component_names = ['a1','a2','pr','t1','t2']
    components_dict = {}
    component_max_val = {}

    for component_name in component_names:
        indiv_list = individual_component(contents_dict[component_name+"_contents"])
        components_dict[component_name] = indiv_list[0]
        component_max_val[component_name] = indiv_list[1]

    for id in class_ids:

         ln = class_dict[id].split(",")[0]
         fn = class_dict[id].split(",")[1]
         a1 = components_dict['a1'].get(id) if components_dict['a1'].get(id) else " "
         a2 = components_dict['a2'].get(id) if components_dict['a2'].get(id) else " "
         pr = components_dict['pr'].get(id) if components_dict['pr'].get(id) else " "
         t1 = components_dict['t1'].get(id) if components_dict['t1'].get(id) else " "
         t2 = components_dict['t2'].get(id) if components_dict['t2'].get(id) else " "

         a1_norm = normalize_marks('a1', a1 if a1 else 0, component_max_val['a1'])
         a2_norm = normalize_marks('a2', a2 if a2 else 0, component_max_val['a2'])
         pr_norm = normalize_marks('pr', pr if pr else 0, component_max_val['pr'])
         t1_norm = normalize_marks('t1', t1 if t1 else 0, component_max_val['t1'])
         t2_norm = normalize_marks('t2', t2 if t2 else 0, component_max_val['t2'])

         gr = fsum([a1_norm,a2_norm,pr_norm,t1_norm,t2_norm])

         report_dict[id] =  \
             [
                  {'ln': ln },
                  {'fn': fn },
                  {'a1': a1 },
                  {'a2': a2 },
                  {'pr': pr },
                  {'t1': t1 },
                  {'t2': t2 },
                  {'gr': str(gr) },
                  {'fl': calc_final_letter_grade(gr) }
             ]

    return report_dict

def sort_by_alternate_column(sort_order):
    class_ids_order = []

    if sort_order == "LT":

     for key, value in sorted(class_dict.iteritems(), key=lambda (k,v): (v,k)):
         class_ids_order.append(key)

    if sort_order == "GR":

     gr_dict = {}

     for item in report_dict:
         gr_dict[item ] = report_dict[item][7]["gr"]

     for key, value in sorted(gr_dict.iteritems(), key=lambda (k,v): (v,k), reverse= True):
         class_ids_order.append(key)

    return [class_ids_order]


