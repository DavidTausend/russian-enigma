from rich.console import Console

console = Console()


def print_enigma_logo():
    logo = """
    ███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗
    ██╔════╝████╗  ██║██║██╔═════╗████╗ ████║██╔══██╗
    █████╗  ██╔██╗ ██║██║██║ ████║██╔████╔██║███████║
    ██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║
    ███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
    ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
    """
    print(logo)
    print("\nWelcome to the Enigma game\n")