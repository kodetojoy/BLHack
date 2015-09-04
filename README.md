```
 ____                _           _                 _     _    _            _
|  _ \              | |         | |               | |   | |  | |          | |
| |_) | ___  _ __ __| | ___ _ __| | __ _ _ __   __| |___| |__| | __ _  ___| | __
|  _ < / _ \| '__/ _` |/ _ \ '__| |/ _` | '_ \ / _` / __|  __  |/ _` |/ __| |/ /
| |_) | (_) | | | (_| |  __/ |  | | (_| | | | | (_| \__ \ |  | | (_| | (__|   <
|____/ \___/|_|  \__,_|\___|_|  |_|\__,_|_| |_|\__,_|___/_|  |_|\__,_|\___|_|\_\
```

# WARNING
This script was made specifically for Mac OS 10.6.8 (this exact version).
**Do not** run this script if you are running any other version!
I AM NOT RESPONSIBLE FOR ANY DAMAGES OF LOSS OF DATA YOU MIGHT ENCOUNTER BY USE/MISUSE OF THIS SCRIPT!

However, if you want to play Borderlands 2 on Mac OS 10.6.8 (through Steam), this can help you out!

This script modifies a system file:

-------------------------------------------------
/System/Library/CoreServices/SystemVersion.plist
-------------------------------------------------

**PLEASE BACK THIS FILE UP BEFORE RUNNING THIS SCRIPT!**

If something goes wrong or things start acting strange, RESTORE this file from your backup! Easy!


## Why I made this
The non-steam version of Borderlands 2 works perfectly fine on Snow Leopard, but the steam version won't launch unless you have at least Mac OS 10.7.5! BLEH! I was stubborn about updating past 10.6.8 (Snow Leopard) but I still
wanted to play Borderlands 2 on Steam.  So I made this script to trick Steam into thinking I was running a newer version of OSX, which allowed Borderlands 2 to run in Steam just fine!

SUCCESS!

## How to use

Because this modifies a system file, you need to run it with administrator privliges.

```
sudo python hack.py
```

You will then see this:

```
Which Mac OS version would you like to be running?
1.) 10.6.8
2.) 10.7.5
3.) 10.8.5
4.) 10.9.5
4.) 10.10.5
```

If you want to play Borderlands 2, type:

```
2
```

and press return. 

```
Success! You are now running 10.7.5! (teehee)
```
If you go to the Apple Menu and look under "About This Mac" you can verify that your system version has changed.

Re-launch Steam if it was open while you changed your versions.

Now you can launch Borderlands 2 in Steam on Snow Leopard!


## Warning #2
REMEMBER TO RUN THIS SCRIPT AGAIN TO CHANGE YOUR VERSION BACK TO 10.6.8 WHEN YOU ARE DONE PLAYING BORDERLANDS!

That means: run this script again but instead of choosing option 2, choose option 1.  That's it!

Some programs will not launch while your system version has been hacked, you will get errors that give you the impression things have been corrupted/damage.  Do not worry, you just need to revert your system version back to the way it was. 

You might run into problems if you reboot the computer while your system version has been hacked, but I have never encountered an unbootable state by using this method/script.

### Good luck!