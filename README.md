# KTM2 ( Windows | Linux( [√]X11 [×]Wayland ) )
`KTM2(Keyboard To Mouse)`'s purpose is to replace mouse operation with 
keyboard operation on `Windows` and `Linux(X11)` operating systems.
## Install
`Windows`:Execute`ktm2/install.ps1`  
`Linux(X11)`:Execute`ktm2/install.sh`  
## Execute
`Windows`:Execute`ktm2/ktm.ps1`  
`Linux(X11)`:Execute`ktm2/ktm.sh`  
## Configure
Edit `ktm2/ktm/config.json`
```json
{
    "mouse_init_move_distance"  :0,
    "mouse_init_scroll_distance":0,
    "leader"                    :"",
    "mouse_move_up"             :"",
    "mouse_move_down"           :"",
    "mouse_move_left"           :"",
    "mouse_move_right"          :"",
    "mouse_left_click"          :"",
    "mouse_left_double_click"   :"",
    "mouse_left_down"           :"",
    "mouse_left_up"             :"",
    "mouse_right_click"         :"",
    "mouse_right_double_click"  :"",
    "mouse_right_down"          :"",
    "mouse_right_up"            :"",
    "mouse_middle_click"        :"",
    "mouse_middle_double_click" :"",
    "mouse_middle_down"         :"",
    "mouse_middle_up"           :"",
    "mouse_scroll_down"         :"",
    "mouse_scroll_up"           :"",
    "mouse_distance_double"     :"",
    "mouse_distance_halve"      :"",
    "app_pause"                 :"",
    "app_restart"               :"",
    "app_close"                 :""
}
```
## Help
`mouse_init_move_distance` is `integer(>0)`  
`mouse_init_scroll_distance` is `integer(>0)`  
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
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z",
    "1","2","3","4","5","6","7","8","9","0",
    "`","-","=","[","]","\\",";","'",",",".","/",
    "~","!","@","#","$","%","^","&","*","(",")","_","+","{","}","|",":","\"",
    "<",">","?"
]
```
> Tips:  
> Don't set duplicate shortcut keys.  
> Don't set the shortcut key to `0` or `""`(empty string).  
