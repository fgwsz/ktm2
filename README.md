# KTM2 ( Windows | Linux )
`KTM2(Keyboard To Mouse)`'s purpose is to replace mouse operation with keyboard operation on Windows/Linux operating systems.
## Execute
Windows:Execute`ktm2/ktm.ps1`  
Linux:Execute`ktm2/ktm.sh`  
## Configure
Edit `ktm2/ktm/config.json`
```json
{
    "mouse_init_move_distance" :64,
    "mouse_init_wheel_distance":4,
    "leader"                   :"alt_l",
    "mouse_move_up"            :"k",
    "mouse_move_down"          :"j",
    "mouse_move_left"          :"h",
    "mouse_move_right"         :"l",
    "mouse_left_click"         :"o",
    "mouse_left_double_click"  :"8",
    "mouse_left_down"          :"g",
    "mouse_left_up"            :"u",
    "mouse_right_click"        :"x",
    "mouse_right_down"         :"i",
    "mouse_right_up"           :"y",
    "mouse_wheel_down"         :"n",
    "mouse_wheel_up"           :"b",
    "mouse_distance_double"    :"2",
    "mouse_distance_halve"     :"-",
    "app_pause"                :"!",
    "app_restart"              :"@",
    "app_close"                :"^"
}
```
## Help
`mouse_init_move_distance` is `integer(>0)`  
`mouse_init_wheel_distance` is `integer(>0)`  
`leader` in
```json
[
    "alt","alt_l","alt_r","alt_gr",
    "ctrl","ctrl_l","ctrl_r",
    "shift","shift_l","shift_r",
    "cmd","cmd_l","cmd_r",
    "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10",
    "f11","f12","f13","f14","f15","f16","f17","f18","f19","f20",
    "space","tab","enter","backspace","esc",
    "caps_lock","num_lock","scroll_lock",
    "insert","delete","home","end","menu","pause","print_screen"
    "up","left","right","down","page_down","page_up",
    "media_play_pause","media_volume_mute","media_volume_down",
    "media_volume_up","media_previous","media_next"
]
```
others in
```json
[
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
    "s","t","u","v","w","x","y","z",
    "1","2","3","4","5","6","7","8","9","0",
    "`","-","=","[","]","\\",";","\'",",",".","/",
    "~","!","@","#","$","%","^","&","*","(",")","_","+","{","}","|",":","\"",
    "<",">","?"
]
```
> Tips:  
> Don't set duplicate shortcut keys.  
> Don't set the shortcut key to `""`(empty string).  
