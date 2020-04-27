#!/usr/bin/python

import sys
import os
import subprocess as sp

def cleanupTrace():

    print("Cleaning up th Entire Trace paramaeter......\n")
    cmd1 = "cat /dev/null > /sys/kernel/debug/tracing/trace"
    cmd2 = "echo 0 > /sys/kernel/debug/tracing/tracing_on"
    cmd3 = "echo > /sys/kernel/debug/tracing/set_graph_function"
    cmd4 = "echo 0 >  /sys/kernel/debug/tracing/max_graph_depth"
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    os.system(cmd4)
    print("Scuccessfully cleared Trace paramaeter......\n")
    return 0
                

def showAllTracer():
    while True:
            print("-----------------------------------------------------------------")
            print("\t\t\033[1;35;40mAvailable Tracer Menu:\033[0;35;40m\n")
            print("\t\t\t\033[1;36;40m1.Available Tracer Type\n")
            print("\t\t\t2.Available Filter Function\n")
            print("\t\t\t3.Return Back\n")
            print("\t\t\t4.Exit\033[0;36;40m\n")
            print("-----------------------------------------------------------------")

            option = int(input("\t\t\tEnter your Choice from 1 to 4: \033[1;32;40m"))
            print("\033[0m")

            if(option == 1):
                cmd1 = "cat /sys/kernel/debug/tracing/available_tracers"
                os.system(cmd1)
            elif(option == 2):
                cmd1 = "cat  /sys/kernel/debug/tracing/available_filter_functions"
                os.system(cmd1)
            elif(option == 3):
                return 0
            elif(option == 4):
                return 5


def setTraceParam():
    while True:
            print("-----------------------------------------------------------------")
            print("\t\t\033[1;35;40mSet Trace Parameter Menu:\033[0;35;40m\n")
            print("\t\t\t\033[1;36;40m1.Set Graph Function\n")
            print("\t\t\t2.Max Graph Depth\n")
            print("\t\t\t3.Return Back\n")
            print("\t\t\t4.Exit\033[0;36;40m\n")
            print("-----------------------------------------------------------------")


            option = int(input("\t\t\tEnter your Choice from 1 to 4: \033[1;32;40m"))
            print("\033[0m")
            
            if(option == 1):
                fun = input("\t\t\tEnter the Function name: ")
                cmd1 = "echo {} > /sys/kernel/debug/tracing/set_graph_function".format(fun)
                os.system(cmd1)
            elif(option == 2):
                depth = int(input("\t\t\tEnter the function graph depth: "))
                cmd1 = "echo {} >  /sys/kernel/debug/tracing/max_graph_depth".format(depth)
                os.system(cmd1)
            elif(option == 3):
                return 0
            elif(option == 4):
                return 5



def setTrace():

    while True:
            print("-----------------------------------------------------------------")
            print("\t\t\033[1;35;40mSet Trace Menu:\033[0;35;40m\n")
            print("\t\t\t\033[1;36;40m1.Enable Trace Log\n")
            print("\t\t\t2.Disable Trace Log\n")
            print("\t\t\t3.Trace Log Staus\n")
            print("\t\t\t4.Return back\n")
            print("\t\t\t5.Exit\033[0;36;40m\n")
            print("-----------------------------------------------------------------")

            option = int(input("\t\t\tEnter your Choice from 1 to 5: \033[1;32;40m"))
            print("\033[0m")

            if(option == 1):
                cmd1 = "cat /dev/null > /sys/kernel/debug/tracing/trace"
                cmd2 = "echo 1 > /sys/kernel/debug/tracing/tracing_on"
                os.system(cmd1)
                os.system(cmd2)
            elif(option == 2):
                cmd1 = "echo > /sys/kernel/debug/tracing/trace"
                cmd2 = "echo 0 > /sys/kernel/debug/tracing/tracing_on"
                os.system(cmd1)
                os.system(cmd2)
            elif(option == 3):
                cmd1 = "cat /sys/kernel/debug/tracing/tracing_on"
                print("\t\t\tStatus is " )
                os.system(cmd1)

                cmd2 = "cat /sys/kernel/debug/tracing/set_graph_function"
                print("\t\t\tCurrent Tracing Function is " )
                os.system(cmd2)

                cmd3 = "cat /sys/kernel/debug/tracing/max_graph_depth"
                print("\t\t\tMAx Graph Depth is " )
                os.system(cmd3)
            elif(option == 4):
                return 0
            else:
                return 5


def main():
    os.system("clear")
    while True:

        try:
            print("-----------------------------------------------------------------")
            print("\033[1;37;40m Main Menu:\033[0;37;40m\n")
            print("\t\033[1;34;40m1. Available Tracer\n")
            print("\t2. Set Tracing Parameter\n")
            print("\t3. Set Trace\n")
            print("\t4. Cleanup\n")
            print("\t5. Exit\033[0;34;40m\n")
            print("-----------------------------------------------------------------")

            option = int(input("Enter your Choice from 1 to 5: \033[1;32;40m"))
            print("\033[0m")

            
            if(option == 1):
                option = showAllTracer()
            elif(option == 2):
                option = setTraceParam()
            elif(option == 3):
                option = setTrace()
            elif(option == 4):
                print("Cleanup")
                option = cleanupTrace()


            if(option == 5):
                print("Good Bye......See you again very soon!")
                sys.exit(0)

        except :
            sys.exit(1)
        



"""
@brief main function of the Program/entry Point
"""
if __name__ == "__main__":
    main()