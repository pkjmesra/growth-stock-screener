from termcolor import colored, cprint
from typing import Dict


def print_status(process: str, stage: int, starting: bool) -> None:
    """Print a header or footer for each screen iteration."""
    if starting:
        print(
            colored(f"\n****** Begin Stage {stage} [", "cyan"),
            colored(f"{process}", "white"),
            colored("] ******\n", "cyan"),
            sep="",
        )
    else:
        print(
            colored(f"\n****** Stage {stage} [", "cyan"),
            colored(f"{process}", "white"),
            colored("] Finished ******\n", "cyan"),
            sep="",
        )


def print_minimums(criteria: Dict[str, int]) -> None:
    """Print minimum values needed to pass screen iterations."""
    for key, value in criteria.items():
        print(
            colored(f"Minimum {key} to pass: ", "cyan"),
            colored(f"{value}", "green"),
            sep="",
        )

    # add newline
    print()


def print_banner() -> None:
    """Print an ASCII art banner for the growth stock screener."""
    banner = """                                                                                                                
                                                                                                                            
                                                                                         .    .!YGY                         
                                                                                       ^BP      ^@B                         
                                 :!!!!^~:  ^7J! ^77^    ^!!77^   .^7?^     !^    :!: ::7@P:::    #G :~7?!.                  
                               :PG!::~B@! ^!!#@J!?#J  7BY~^^?&B^ ~~!&&:  .5@B    7@P ~~J@P~!^    ##77!7P@5           ~^     
                              .#&.    P@^    5@^  .  ~@P     7@G    J@7 :Y^J@!   .&?   ~@Y      .#G    .&G      .^75#@J     
                              !@G     P@^    5@:     J@Y     ~@B    ^@Y^5: .&#. .Y7    ~@Y      .&P    .&G   :7YB@@@@@J     
                              :&@?. .^G@^    G@:     ^&@~   .P@!    .&@5.   7@5!J^     ~@B:.^^  :@P    :@#::~.  ?@@@B@P     
                        :~~.   ^NVDA?!B@:    55.      ^5GY??YJ^      Y5.     5P~       .YBPJ!.  :G7     Y#P?^  7@@@? ^J.    
                     ~AI&@@#?        ^@P        :7??7    ...               .^?J            .^J?...            7@@@Y         
                  :J#@@#@@@@5  YB7^~7PJ.        G@@@@P.            ..:~!?5B&@#P^   ..^~7JPB&@#G##&BY~.       ~@@@B          
               .7G@&5!^5@@@5   .~7!~^.    ^~^~7GROWTH@#7        YBBSTOCKS5J!^.  PBB##BBBG5J!:  7@@@@@#5~     B@@@!          
             ^5&#5~. ^G@@@J            ~5B@@@B57^^P@@@@@B7.     ^!&@B~?7        ^?@@G7~         ?@@@&@@@G!  !@@@B           
          .7B&P!.  .J@@@&7           ^G@@@BJ^.    :&@@5Y&@&Y^    J#@@&G? .^!?YPGGG&@@&7  .^7J5NET@@@B~Y&@@P:5@@@?           
        :J##J:     AMZN?:     ..:::.^&@@&?         J@@B .~JB@BJ^ !?&@@?JB&@#GY7~^.!@@&?5B&@#PY7~^?#@7  :P@@&&@@@^           
      .Y&G!       ..:^~!7JY5PPPGPPP5P@@@P      :   ^@@@^    5@@@B^ #@@@@G?^.      :@@@@@P7^       .^     7&@@@@#.           
     ~#@5^^~!?Y5GGBGPP5YY?~^::..    ~@@@@!   ^5@5   #@@CRWD#PLTRJ: ?JYJ:          .?JY?:                  :^~!??            
    ~@@@@@@@&ELF?~:. ~J#&&G~      .J&@@@@@#B#@@#J   B@@7:#@@G                                                               
    :JYJ?7~:.          J@@@#    .?#@@#J^7J55Y?~.   .#@@! ^&@@P                                                              
                       !@@@B  :Y&@@G7.              J5P^  ~#@@G:                                                            
                       P@@@7~P@@BJ^                        :P@@&7                                                           
                      ?@@@&#@#Y~                             7#@@G~                                                         
                     ^&@@@GJ^                                 .7G@@B?:                                                      
                      .^!~                                       :7YP57^                                                    
                                                                                 
    """
    cprint(banner, "cyan")


def print_divider() -> None:
    cprint(
        "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯",
        "dark_grey",
    )


def skip_message(symbol: str, message: str) -> str:
    """Return a custom message logging screening errors."""
    return colored(f"\nSkipping {symbol} ({message}) . . .\n", "red")


def filter_message(symbol: str) -> str:
    """Return a custom message for logging when a stock is filtered out by a screen."""
    return f"\n{symbol} filtered out.\n"


def message(message: str) -> str:
    """Return a custom message for logging purposes."""
    return f"\n{message}\n"
