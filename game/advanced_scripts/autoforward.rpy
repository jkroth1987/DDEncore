init python:
    
    group_talk = False
    group_total = 0
    say_pos = 0
    yur_pos = 0
    nat_pos = 0
    mon_pos = 0
    
    def show_original(who, what, **kwargs):
        return renpy.show_display_say(who, what, **kwargs)

    def sayori_focus(event, interact=True, **kwargs):
        if group_talk:
            if event == "begin":
                if group_total == 2:
                    if say_pos == 1:
                        renpy.show("sayori", at_list=[f21], zorder=1)
                    else:
                        renpy.show("sayori", at_list=[f22], zorder=1)
                elif group_total == 3:
                    if say_pos == 1:
                        renpy.show("sayori", at_list=[f31], zorder=1)
                    elif say_pos == 2:
                        renpy.show("sayori", at_list=[f32], zorder=1)
                    else:
                        renpy.show("sayori", at_list=[f33], zorder=1)
                elif group_total == 4:
                    if say_pos == 1:
                        renpy.show("sayori", at_list=[f41], zorder=3)
                    elif say_pos == 2:
                        renpy.show("sayori", at_list=[f42], zorder=3)
                    elif say_pos == 3:
                        renpy.show("sayori", at_list=[f43], zorder=3)
                    else:
                        renpy.show("sayori", at_list=[f44], zorder=3)
            elif event == "end":
                if group_total == 2:
                    if say_pos == 1:
                        renpy.show("sayori", at_list=[t21], zorder=3)
                    else:
                        renpy.show("sayori", at_list=[t22], zorder=3)
                elif group_total == 3:
                    if say_pos == 1:
                        renpy.show("sayori", at_list=[t31], zorder=3)
                    elif say_pos == 2:
                        renpy.show("sayori", at_list=[t32], zorder=3)
                    else:
                        renpy.show("sayori", at_list=[t33], zorder=3)
                elif group_total == 4:
                    if say_pos == 1:
                        renpy.show("sayori", at_list=[t41], zorder=3)
                    elif say_pos == 2:
                        renpy.show("sayori", at_list=[t42], zorder=3)
                    elif say_pos == 3:
                        renpy.show("sayori", at_list=[t43], zorder=3)
                    else:
                        renpy.show("sayori", at_list=[t44], zorder=3)
            s.show_function = show_original
            
    def yuri_focus(event, interact=True, **kwargs):
        if group_talk:
            if event == "begin":
                if group_total == 2:
                    if yur_pos == 1:
                        renpy.show("yuri", at_list=[f21], zorder=1)
                    else:
                        renpy.show("yuri", at_list=[f22], zorder=1)
                elif group_total == 3:
                    if yur_pos == 1:
                        renpy.show("yuri", at_list=[f31], zorder=1)
                    elif yur_pos == 2:
                        renpy.show("yuri", at_list=[f32], zorder=1)
                    else:
                        renpy.show("yuri", at_list=[f33], zorder=1)
                elif group_total == 4:
                    if yur_pos == 1:
                        renpy.show("yuri", at_list=[f41], zorder=3)
                    elif yur_pos == 2:
                        renpy.show("yuri", at_list=[f42], zorder=3)
                    elif yur_pos == 3:
                        renpy.show("yuri", at_list=[f43], zorder=3)
                    else:
                        renpy.show("yuri", at_list=[f44], zorder=3)
            elif event == "end":
                if group_total == 2:
                    if yur_pos == 1:
                        renpy.show("yuri", at_list=[t21], zorder=3)
                    else:
                        renpy.show("yuri", at_list=[t22], zorder=3)
                elif group_total == 3:
                    if yur_pos == 1:
                        renpy.show("yuri", at_list=[t31], zorder=3)
                    elif yur_pos == 2:
                        renpy.show("yuri", at_list=[t32], zorder=3)
                    else:
                        renpy.show("yuri", at_list=[t33], zorder=3)
                elif group_total == 4:
                    if yur_pos == 1:
                        renpy.show("yuri", at_list=[t41], zorder=3)
                    elif yur_pos == 2:
                        renpy.show("yuri", at_list=[t42], zorder=3)
                    elif yur_pos == 3:
                        renpy.show("yuri", at_list=[t43], zorder=3)
                    else:
                        renpy.show("yuri", at_list=[t44], zorder=3)
            y.show_function = show_original
            
    def natsuki_focus(event, interact=True, **kwargs):
        if group_talk:
            if event == "begin":
                if group_total == 2:
                    if nat_pos == 1:
                        renpy.show("natsuki", at_list=[f21], zorder=1)
                    else:
                        renpy.show("natsuki", at_list=[f22], zorder=1)
                elif group_total == 3:
                    if nat_pos == 1:
                        renpy.show("natsuki", at_list=[f31], zorder=1)
                    elif nat_pos == 2:
                        renpy.show("natsuki", at_list=[f32], zorder=1)
                    else:
                        renpy.show("natsuki", at_list=[f33], zorder=1)
                elif group_total == 4:
                    if nat_pos == 1:
                        renpy.show("natsuki", at_list=[f41], zorder=3)
                    elif nat_pos == 2:
                        renpy.show("natsuki", at_list=[f42], zorder=3)
                    elif nat_pos == 3:
                        renpy.show("natsuki", at_list=[f43], zorder=3)
                    else:
                        renpy.show("natsuki", at_list=[f44], zorder=3)
            elif event == "end":
                if group_total == 2:
                    if nat_pos == 1:
                        renpy.show("natsuki", at_list=[t21], zorder=3)
                    else:
                        renpy.show("natsuki", at_list=[t22], zorder=3)
                elif group_total == 3:
                    if nat_pos == 1:
                        renpy.show("natsuki", at_list=[t31], zorder=3)
                    elif nat_pos == 2:
                        renpy.show("natsuki", at_list=[t32], zorder=3)
                    else:
                        renpy.show("natsuki", at_list=[t33], zorder=3)
                elif group_total == 4:
                    if nat_pos == 1:
                        renpy.show("natsuki", at_list=[t41], zorder=3)
                    elif nat_pos == 2:
                        renpy.show("natsuki", at_list=[t42], zorder=3)
                    elif nat_pos == 3:
                        renpy.show("natsuki", at_list=[t43], zorder=3)
                    else:
                        renpy.show("natsuki", at_list=[t44], zorder=3)
            n.show_function = show_original
            
    def monika_focus(event, interact=True, **kwargs):
        if group_talk:
            if event == "begin":
                if group_total == 2:
                    if mon_pos == 1:
                        renpy.show("monika", at_list=[f21])
                    else:
                        renpy.show("monika", at_list=[f22])
                elif group_total == 3:
                    if mon_pos == 1:
                        renpy.show("monika", at_list=[f31])
                    elif mon_pos == 2:
                        renpy.show("monika", at_list=[f32])
                    else:
                        renpy.show("monika", at_list=[f33])
                elif group_total == 4:
                    if mon_pos == 1:
                        renpy.show("monika", at_list=[f41], zorder=3)
                    elif mon_pos == 2:
                        renpy.show("monika", at_list=[f42], zorder=3)
                    elif mon_pos == 3:
                        renpy.show("monika", at_list=[f43], zorder=3)
                    else:
                        renpy.show("monika", at_list=[f44], zorder=3)
            elif event == "end":
                if group_total == 2:
                    if mon_pos == 1:
                        renpy.show("monika", at_list=[t21])
                    else:
                        renpy.show("monika", at_list=[t22])
                elif group_total == 3:
                    if mon_pos == 1:
                        renpy.show("monika", at_list=[t31])
                    elif mon_pos == 2:
                        renpy.show("monika", at_list=[t32])
                    else:
                        renpy.show("monika", at_list=[t33])
                elif group_total == 4:
                    if mon_pos == 1:
                        renpy.show("monika", at_list=[t41], zorder=3)
                    elif mon_pos == 2:
                        renpy.show("monika", at_list=[t42], zorder=3)
                    elif mon_pos == 3:
                        renpy.show("monika", at_list=[t43], zorder=3)
                    else:
                        renpy.show("monika", at_list=[t44], zorder=3)
            m.show_function = show_original
            
label groupAll(total, sayo, yur, natsu, moni):
    $ group_talk = True
    $ group_total = total
    $ say_pos = sayo
    $ yur_pos = yur
    $ nat_pos = natsu
    $ mon_pos = moni
    return
    
label groupClear():
    $ group_talk = False
    $ group_total = 0
    $ say_pos = 0
    $ yur_pos = 0
    $ nat_pos = 0
    $ mon_pos = 0
    return