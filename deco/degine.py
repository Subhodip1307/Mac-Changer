import pyfiglet
from colorama import Fore ,Back,Style
name="..MAC_Changer.."
colord_lines=[]
colors=['\x1b[34m', '\x1b[94m']
asii_banner=pyfiglet.figlet_format(name)
lines=asii_banner.split("\n")
for i ,line in enumerate(lines):
    color=colors[i % len(colors)]
    colord_line="{}{}{}".format(color,line,Style.RESET_ALL)
    colord_lines.append(colord_line)
colord_banner="\n".join(colord_lines)
print(colord_banner)     
            