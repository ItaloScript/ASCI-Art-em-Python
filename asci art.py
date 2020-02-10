import pyfiglet,colorama,termcolor
printado = input("o que você deseja printar ?")
colorama.init()
cor = input("em que cor?")
print(termcolor.colored(pyfiglet.figlet_format(printado),color=f"{cor}",on_color=f"on_white"))
