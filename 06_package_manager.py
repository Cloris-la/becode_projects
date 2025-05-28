PS D:\projects> winget install neofetch
Found an existing package already installed. Trying to upgrade the installed package...
No available upgrade found.
No newer package versions are available from the configured sources.
PS D:\projects> winget search neofetch 
Name         Id                      Version Match             Source
---------------------------------------------------------------------
neofetch-win nepnep.neofetch-win     1.2.1   Moniker: neofetch winget
fastfetch    Fastfetch-cli.Fastfetch 2.44.0  Tag: neofetch     winget
PS D:\projects> winget launch neofetch
Windows Package Manager v1.10.390
Copyright (c) Microsoft Corporation. All rights reserved.

Unrecognized command: 'launch'

The winget command line utility enables installing applications and other packages from the command line.

usage: winget  [<command>] [<options>]

The following commands are available:
  install    Installs the given package
  show       Shows information about a package
  source     Manage sources of packages
  search     Find and show basic info of packages
  list       Display installed packages
  upgrade    Shows and performs available upgrades
  uninstall  Uninstalls the given package
  hash       Helper to hash installer files
  validate   Validates a manifest file
  settings   Open settings or set administrator settings
  features   Shows the status of experimental features
  export     Exports a list of the installed packages
  import     Installs all the packages in a file
  pin        Manage package pins
  configure  Configures the system into a desired state
  download   Downloads the installer from a given package
  repair     Repairs the selected package

For more details on a specific command, pass it the help argument. [-?]

The following options are available:
  -v,--version                Display the version of the tool
  --info                      Display general info of the tool
  -?,--help                   Shows help about the selected command
  --wait                      Prompts the user to press any key before exiting   
  --logs,--open-logs          Open the default logs location
  --verbose,--verbose-logs    Enables verbose logging for winget
  --nowarn,--ignore-warnings  Suppresses warning outputs
  --disable-interactivity     Disable interactive prompts
  --proxy                     Set a proxy to use for this execution
  --no-proxy                  Disable the use of proxy for this execution        

More help can be found at: https://aka.ms/winget-command-help
PS D:\projects> neofetch
llllllllllllllll   llllllllllllllll            cloris@LAPTOP-38BPV5NK
llllllllllllllll   llllllllllllllll            --------------
llllllllllllllll   llllllllllllllll            OS: Windows 11
llllllllllllllll   llllllllllllllll            Build: 24H2 (26100)
llllllllllllllll   llllllllllllllll            Uptime: 0 days, 9 hours, 59 minutes
llllllllllllllll   llllllllllllllll            Resolution: 1920x1200 @60Hz       
llllllllllllllll   llllllllllllllll            Terminal: C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe
llllllllllllllll   llllllllllllllll            CPU: 12th Gen Intel(R) Core(TM) i5-12500H
llllllllllllllll   llllllllllllllll            GPU: Intel(R) Iris(R) Xe Graphics 
                                               Memory: 8887 MB / 16069 MB (55% in use)
llllllllllllllll   llllllllllllllll            Disk: C:\ 333.1 GB (260.99 GB free)
llllllllllllllll   llllllllllllllll
llllllllllllllll   llllllllllllllll            Mem%:  -=[ //////////////////// ]=-
llllllllllllllll   llllllllllllllll
llllllllllllllll   llllllllllllllll            Disk%: -=[ //////////////////// ]=-
llllllllllllllll   llllllllllllllll
llllllllllllllll   llllllllllllllll                                              
llllllllllllllll   llllllllllllllll                                              
llllllllllllllll   llllllllllllllll
PS D:\projects> winget uninstall neofetch
Found neofetch-win [nepnep.neofetch-win]
Starting package uninstall...
Successfully uninstalled
PS D:\projects> 