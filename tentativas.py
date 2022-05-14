from colorama import Fore
def tentativas_res(t):
        if t >= 15:
            return("\n Voce ainda tem " + Fore.LIGHTMAGENTA_EX + f"{t}" +Fore.RESET + " tentativas restantes \n")
        
        elif t >= 10:
            return("\n Voce ainda tem " + Fore.LIGHTYELLOW_EX + f"{t}" +Fore.RESET + " tentativas restantes \n")

        else:
            return("\n Voce ainda tem " + Fore.LIGHTRED_EX+ f"{t}" +Fore.RESET + " tentativas restantes \n")