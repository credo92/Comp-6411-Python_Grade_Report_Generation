import os
import compute

#getting current path and setting file paths
current_dir = os.getcwd()

class_file_dir = current_dir + "/class.txt"
a1_file_dir = current_dir + "/a1.txt"
a2_file_dir = current_dir + "/a2.txt"
project_file_dir = current_dir + "/project.txt"
t1_file_dir = current_dir + "/test1.txt"
t2_file_dir = current_dir + "/test2.txt"

def read_file(file_path):
    file_content = open(file_path,'r')
    return file_content.read()

def get_contents():
    return dict(
                class_contents=read_file(class_file_dir),
                a1_contents=read_file(a1_file_dir),
                a2_contents=read_file(a2_file_dir),
                pr_contents=read_file(project_file_dir),
                t1_contents=read_file(t1_file_dir),
                t2_contents=read_file(t2_file_dir)
               )
def init():

    class_dict = {}
    class_ids = []
    class_dict_ids_list = compute.create_class_content_dict(get_contents()["class_contents"])
    class_dict = class_dict_ids_list[0]
    class_ids = class_dict_ids_list[1]

    print(
        "1> Display individual component \n"
        "2> Display component average \n"
        "3> Display Standard Report\n"
        "4> Sort by alternate column\n"
        "5> Change Pass/Fail point\n"
        "6> Exit"
    )

    input = raw_input("\n Please enter choice : ")

    if input == "1":

        component = raw_input("\n \t select [A1, A2, PR, T1, or	T2 ] : ")
        component =  component.upper()

        if component == "A1" :
         indiv_comp_list =  compute.individual_component(get_contents()[component.lower()+"_contents"])
         indiv_component =  indiv_comp_list[0]
         max_point_value = indiv_comp_list[1]

         print "\n"
         print component + " grades (" + max_point_value + ")"
         print "\n"

         for id in sorted(list(set(class_ids))):
             print id + "\t \t " + class_dict[id] + "\t \t \t " + indiv_component[id]
             print "\n"

         print "\n"
         init()

        elif component == "A2" :
         indiv_comp_list =  compute.individual_component(get_contents()[component.lower()+"_contents"])
         indiv_component =  indiv_comp_list[0]
         max_point_value = indiv_comp_list[1]

         print "\n"
         print component + " grades (" + max_point_value + ")"
         print "\n"

         for id in sorted(list(set(class_ids))):
             print id + "\t \t " + class_dict[id] + "\t \t \t " + indiv_component[id]
             print "\n"

         print "\n"
         init()

        elif component == "PR" :

         indiv_comp_list =  compute.individual_component(get_contents()[component.lower()+"_contents"])
         indiv_component =  indiv_comp_list[0]
         max_point_value = indiv_comp_list[1]

         print "\n"
         print component + " grades (" + max_point_value + ")"
         print "\n"

         for id in sorted(list(set(class_ids))):
             print id + "\t \t " + class_dict[id] + "\t \t \t " + indiv_component[id]
             print "\n"

         print "\n"
         init()

        elif component == "T1" :

         indiv_comp_list =  compute.individual_component(get_contents()[component.lower()+"_contents"])
         indiv_component =  indiv_comp_list[0]
         max_point_value = indiv_comp_list[1]

         print "\n"
         print component + " grades (" + max_point_value + ")"
         print "\n"

         for id in sorted(list(set(class_ids))):
             print id + "\t \t " + class_dict[id] + "\t \t \t " + indiv_component[id]
             print "\n"

         print "\n"
         init()

        elif component == "T2" :

         indiv_comp_list =  compute.individual_component(get_contents()[component.lower()+"_contents"])
         indiv_component =  indiv_comp_list[0]
         max_point_value = indiv_comp_list[1]

         print "\n"
         print component + " grades (" + max_point_value + ")"
         print "\n"

         for id in sorted(list(set(class_ids))):
             print id + "\t \t " + class_dict[id] + "\t \t \t " + indiv_component[id]
             print "\n"

         print "\n "
         init()

        else:
            print "\n "
            init()

        init()
    elif input == "2":

        component = raw_input("select [A1,	A2,	PR,	T1,	or	T2 ] : ")
        component =  component.upper()

        if component == "A1" :
         average_component = compute.component_average(get_contents()[component.lower()+"_contents"],component)

         print "\n"
         print average_component
         print "\n "

         init()

        elif component == "A2" :
         average_component = compute.component_average(get_contents()[component.lower()+"_contents"],component)

         print "\n"
         print average_component
         print "\n "

         init()

        elif component == "PR" :
         average_component = compute.component_average(get_contents()[component.lower()+"_contents"],component)

         print "\n"
         print average_component
         print "\n "

         init()

        elif component == "T1" :
         average_component = compute.component_average(get_contents()[component.lower()+"_contents"],component)

         print "\n"
         print average_component
         print "\n "

         init()

        elif component == "T2" :
         average_component = compute.component_average(get_contents()[component.lower()+"_contents"],component)

         print "\n"
         print average_component
         print "\n "

         init()

        else:
            print "\n"
            init()

        init()

    elif input == "3":

        print("\n")
        report  =  compute.standard_report(get_contents(),False)
        print "ID\t\tLN\t\tFN\t\tA1\t\tA2\t\tPR\t\tT1\t\tT2\t\tGR\t\tFL"
        print "\n"

        for id in sorted(list(set(class_ids))):
            print id + "  " + report[id][0]["ln"] + "\t \t "+ report[id][1]["fn"] + "\t \t " + report[id][2]['a1'] + "\t \t " + report[id][3]['a2'] \
            + "\t \t " + report[id][4]['pr'] + "\t \t " + report[id][5]['t1'] + "\t \t " + report[id][6]['t2'] + "\t \t " + report[id][7]['gr'] \
                  + "\t \t " + report[id][8]['fl']

            print "\n"

        print "\n"
        init()

    elif input == "4":

        sort_order = raw_input("select sort order LT or GR : ")
        print "\n"
        sort_order = sort_order.upper()
        report  =  compute.standard_report(get_contents(),False)

        if sort_order == "LT":

            ids_sorted_lt = compute.sort_by_alternate_column(sort_order)[0]

            print "ID\t\tLN\t\tFN\t\tA1\t\tA2\t\tPR\t\tT1\t\tT2\t\tGR\t\tFL"
            print "\n"

            for id in ids_sorted_lt:
               print id + "  " + report[id][0]["ln"] + "\t \t "+ report[id][1]["fn"] + "\t \t " + report[id][2]['a1'] + "\t \t " + report[id][3]['a2'] \
            + "\t \t " + report[id][4]['pr'] + "\t \t " + report[id][5]['t1'] + "\t \t " + report[id][6]['t2'] + "\t \t " + report[id][7]['gr'] \
                  + "\t \t " + report[id][8]['fl']

            print "\n"
            init()

        elif sort_order == "GR":
            ids_sorted_gr = compute.sort_by_alternate_column(sort_order)[0]

            print "ID\t\tLN\t\tFN\t\tA1\t\tA2\t\tPR\t\tT1\t\tT2\t\tGR\t\tFL"
            print "\n"

            for id in ids_sorted_gr:
               print id + "  " + report[id][0]["ln"] + "\t \t "+ report[id][1]["fn"] + "\t \t " + report[id][2]['a1'] + "\t \t " + report[id][3]['a2'] \
            + "\t \t " + report[id][4]['pr'] + "\t \t " + report[id][5]['t1'] + "\t \t " + report[id][6]['t2'] + "\t \t " + report[id][7]['gr'] \
                  + "\t \t " + report[id][8]['fl']

            print "\n"
            init()

        else:
            init()

        init()

    elif input == "5":

        new_pass_fail_point = raw_input("change P/F Point : ")
        if int(new_pass_fail_point) > 100:
            print "wrong value for pass/fail \n"
            init()
        compute.set_pass_fail_point(int(new_pass_fail_point))

        report  =  compute.standard_report(get_contents(), True)
        print "ID\t\tLN\t\tFN\t\tA1\t\tA2\t\tPR\t\tT1\t\tT2\t\tGR\t\tFL"
        print "\n"

        for id in sorted(list(set(class_ids))):
            print id + "  " + report[id][0]["ln"] + "\t \t "+ report[id][1]["fn"] + "\t \t " + report[id][2]['a1'] + "\t \t " + report[id][3]['a2'] \
            + "\t \t " + report[id][4]['pr'] + "\t \t " + report[id][5]['t1'] + "\t \t " + report[id][6]['t2'] + "\t \t " + report[id][7]['gr'] \
                  + "\t \t " + report[id][8]['fl']

            print "\n"

        print "\n"
        init()

    elif input == "6":
        print("\n \t Good Bye")
        exit(1)
    else:
        print "\n choose correct choice 1-6 \n"
        init()

init()






