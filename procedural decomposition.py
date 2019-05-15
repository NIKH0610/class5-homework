#This program draws faces and text boxes during functions.


def draw_wide_box():
    print("+------------------------+")
    print("|                        |")
    print("+------------------------+")


def draw_face():
    print("      ____________         ")
    print("     /            \\")
    print("     |O          O|")
    print("     |            |")
    print("     |      x     |")
    print("     |    \___/   |")
    print("     |            |")
    print("     \\___________/")

def main():
    draw_face()
    draw_wide_box()
    draw_wide_box()
    draw_face()
    draw_wide_box()

main()
