# 10 bilion count time test

In this test I attempt 

```bash
                  -`                     shawal@shawalarch
                 .o+`                    -----------------
                `ooo/                    OS: Arch Linux x86_64
               `+oooo:                   Host: OptiPlex 5050
              `+oooooo:                  Kernel: Linux 6.10.4-arch2-1
              -+oooooo+:                 Uptime: 1 day, 3 hours, 6 mins
            `/:-:++oooo+:                Packages: 1826 (pacman)
           `/++++/+++++++:               Shell: fish 3.7.1
          `/++++++++++++++:              Display (LA1905): 1440x900 @ 60 Hz in 19″ [External]
         `/+++ooooooooooooo/`            Display (LA1905): 1440x900 @ 60 Hz in 19″ [External]
        ./ooosssso++osssssso+`           WM: Hyprland (Wayland)
       .oossssso-````/ossssss+`          Theme: Breeze-Dark [GTK2], Breeze [GTK3]
      -osssssso.      :ssssssso.         Icons: Deepin Dark [GTK2/3/4]
     :osssssss/        osssso+++.        Font: Noto Sans (10pt) [GTK2/3/4]
    /ossssssss/        +ssssooo/-        Cursor: breeze (24px)
  `/ossssso+/:-        -:/+osssso+-      Terminal: code-insiders 1.92.0-insider
 `+sso+:-`                 `.-/+oso:     CPU: Intel(R) Core(TM) i5-7500 (4) @ 3.80 GHz
`++:.                           `-/+/    GPU: Intel HD Graphics 630 @ 1.10 GHz [Integrated]
.`                                 `/    Memory: 4.51 GiB / 7.64 GiB (59%)
                                         Swap: 400.25 MiB / 3.82 GiB (10%)
                                         Disk (/): 281.17 GiB / 465.26 GiB (60%) - btrfs
                                         Local IP (enp0s31f6): 192.168.0.101/24
                                         Locale: en_US.UTF-8
                                                              
                                                                 
```

```bash
time java Main.java

________________________________________________________
Executed in    3.76 secs    fish           external
   usr time    4.08 secs  350.00 micros    4.08 secs
   sys time    0.03 secs  246.00 micros    0.03 secs
```

```bash
time pypy3 count.py

________________________________________________________
Executed in   10.79 secs    fish           external
   usr time   10.77 secs  326.00 micros   10.77 secs
   sys time    0.02 secs  230.00 micros    0.02 secs
```

```bash
rustc count.rs && time ./count

________________________________________________________
Executed in   62.41 secs    fish           external
   usr time   62.33 secs  154.00 micros   62.33 secs
   sys time    0.01 secs  110.00 micros    0.01 secs
```

```bash
g++ count.cpp && time ./a.out

________________________________________________________
Executed in   14.36 secs    fish           external
   usr time   14.35 secs  145.00 micros   14.35 secs
   sys time    0.00 secs   96.00 micros    0.00 secs
```

```bash
g++ count.c && time ./a.out

________________________________________________________
Executed in   14.33 secs    fish           external
   usr time   14.32 secs  118.00 micros   14.32 secs
   sys time    0.00 secs  104.00 micros    0.00 secs
```

```bash
clang count.c && time ./a.out

________________________________________________________
Executed in   14.87 secs    fish           external
   usr time   14.85 secs    0.00 micros   14.85 secs
   sys time    0.00 secs  266.00 micros    0.00 secs
```

```bash
time python count.py
```
over 800 seconds