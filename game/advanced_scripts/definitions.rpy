
#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = True #Change this flag to True to enable dev tools

#python early:
#    import singleton
#    me = singleton.SingleInstance()

init python:
    if 'mouseup_3' in config.keymap['game_menu']:
        config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

#Music
#The Music section is where you can reference existing DDLC audio

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.knocking = "mod_assets/knock.ogg" #knock-knock
define audio.school = "mod_assets/audio/School Bell Sound Effect.ogg" #School Bell
define audio.fingersnap = "mod_assets/audio/Finger-Snap_1.ogg" #FingerSnapForVoid
define audio.neck = "mod_assets/audio/Neck_Break.ogg"
define audio.bone = "mod_assets/audio/Bone.ogg"
define audio.knife = "mod_assets/audio/Knife.ogg"
define audio.stab = "mod_assets/audio/Stab.ogg"
define audio.drop = "mod_assets/audio/Metal_Drop.ogg"
define audio.belly = "mod_assets/audio/Stomach-Growl.ogg"
define audio.sample = "mod_assets/audio/Your_Reality_Sample.ogg" #Sample Music
define audio.preview = "mod_assets/audio/Your_Reality_Preview.ogg"
define audio.doorbell = "mod_assets/audio/Doorbell.ogg"
define audio.gust = "mod_assets/audio/Gust.ogg" #Wind Gust
define audio.train = "mod_assets/audio/Train.ogg"
define audio.train_journey = "mod_assets/audio/Train-Journey.ogg"
define audio.drop2 = "mod_assets/audio/drop2.ogg"
define audio.sheath1 = "mod_assets/audio/sheath1.ogg"
define audio.sheath2 = "mod_assets/audio/sheath2.ogg"
define audio.scare= "mod_assets/audio/scare.ogg"
define audio.groan= "mod_assets/audio/groan.ogg"
define audio.run= "mod_assets/audio/run.ogg"
#--Encore's New Music
define audio.e1 = "<loop 0>mod_assets/audio/void1.ogg" #The Void (First Void Scene Music)
define audio.f1 = "<loop 0>mod_assets/audio/mainmenu.ogg" #Doki Doki Forever (Main Menu Music, Doki Doki!~)
define audio.e2 = "<loop 0>mod_assets/audio/Monika's Theme V3.ogg" #Our Reality (I hope you enjoy my song~ Angelic spent a long time on it)
define audio.e3 = "<loop 0>mod_assets/audio/Natsuki's Theme Full.ogg" #I'm trying, Okay? (Now that's what I call music!)
define audio.e4 = "<loop 0>mod_assets/audio/Sayori's Theme Full.ogg" #Bittersweet Sunshine (Guitars and a country feel to it!)
define audio.e5 = "<loop 0>mod_assets/audio/Yuri's Theme V2.ogg" #Unending Violet (This music...beautiful)
define audio.e6 = "<loop 0>mod_assets/audio/Encore.ogg" #Encore! (Okay, everyone, all together!~)
define audio.e7 = "<loop 0>mod_assets/audio/Rainbow Reality V3.ogg" #Rainbow Reality (We're all fine)
define audio.e8 = "<loop 0>mod_assets/audio/Monika Void Theme.ogg" #Only Us
define audio.e9 = "<loop 0>mod_assets/audio/Yuri's void v2.ogg" #Unhinged
define audio.e10 = "<loop 0>mod_assets/audio/Natsuki's void v2.ogg" #I Know You Like Me
define audio.e11 = "<loop 0>mod_assets/audio/Sayori's Void V2.ogg" #Sayo-Prise!
define audio.e12 = "<loop 0>mod_assets/audio/How You Feel.ogg" #Rooftop Song
define audio.e13 = "<loop 0>mod_assets/audio/Ohayou_Monika.ogg" #Alternate Monika Theme MBS
define audio.e14 = "<loop 0>mod_assets/audio/Ohayou_Natsuki.ogg" #Alternate Natsuki Theme MBS
define audio.e15 = "<loop 0>mod_assets/audio/Ohayou_Sayori.ogg" #Alternate Sayori Theme MBS
define audio.e16 = "<loop 0>mod_assets/audio/Ohayou_Yuri.ogg" #Alternate Yuri Theme MBS
define audio.e17 = "<loop 0>mod_assets/audio/iPhone_Ring.ogg" #iPhone
define audio.e18 = "<loop 0>mod_assets/audio/Hypothetical Romance.ogg" #Monika Day 3 Unique OST
define audio.e19 = "<loop 0>mod_assets/audio/Natsuki_Confession.ogg" #Natsuki Confession Music
define audio.e20 = "<loop 0>mod_assets/audio/Yuri_Confession.ogg" #Yuri Confession Music


# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

#Encore's New Assets
image bg void = "mod_assets/bgs/void.png"
image bg living_room = "mod_assets/bgs/MC_Living_room_daytime by Nuxill#7870.png"
image bg living_room_afternoon = "mod_assets/bgs/MC_Living_room_afternoon by Nuxill#7870.png"
image bg bedroom_night = "mod_assets/bgs/Protagonist_Bedroom_Night by Alex.png"
image bg n_void_1 = "mod_assets/bgs/n_v_1.png"
image bg closet_dark = night("bg/closet.png")
image bg closet_empty = "mod_assets/bgs/goodnight.png"
image bg club_nothing = "mod_assets/bgs/Club+Empty+Night.png"
image bg residential_dusk = "mod_assets/bgs/residential_dusk.png"
image bg void_2 = "mod_assets/bgs/void_2.png"
image bg cafeteria = "mod_assets/bgs/cafeteria.png"
image bg school_rooftop = "mod_assets/bgs/school_rooftop.png"
image bg thank_you = "bandicam 2019-03-18-09-10-05-743.png"
image bg music_room = "mod_assets/bgs/music_room.png"
image bg fountain = "mod_assets/bgs/fountain_bg.png"
image bg monika_walk1 = "mod_assets/bgs/Monika Walk 1.png"
image bg monika_walk2 = "mod_assets/bgs/Monika Walk 2.png"
image bg monika_walk3 = "mod_assets/bgs/Monika Walk 3.png"
image bg city_overlook = "mod_assets/bgs/city_overlook.png"
image bg library = "mod_assets/bgs/library.png"
image bg manga = "mod_assets/bgs/manga_section.png"
image bg school = "mod_assets/bgs/school.png"
image bg city_sidewalk = "mod_assets/bgs/city_sidewalk.png"
image bg fastfood = "mod_assets/bgs/fastfood.png"
image bg city_sidewalk2 = "mod_assets/bgs/city_sidewalk2.png"
image bg park_dusk = "mod_assets/bgs/park_dusk.png"
image bg residential_night = "mod_assets/bgs/residential_night.png"
image bg residential_2 = "mod_assets/bgs/residential_2.png"
image bg train_night = "mod_assets/bgs/train_night.png"
image bg train_day = "mod_assets/bgs/train_day.png"
image bg train_station = "mod_assets/bgs/train_station.png"
image bg garden_dusk = "mod_assets/bgs/garden_dusk.png"
image bg garden_day = "mod_assets/bgs/garden_day.png"
image bg space_room = "mod_assets/bgs/space_room.png"
image bg kitchen_dark = "mod_assets/bgs/kitchen_dark.png"
image bg kitchen_light = "mod_assets/bgs/kitchen_light.png"
image bg livingroom_dark = "mod_assets/bgs/livingroom_dark.png"
image bg natsuki_house = "mod_assets/bgs/natsuki_house.png"
image bg natsuki_room = "mod_assets/bgs/natsuki_room.png"
image bg bedroom_dawn = "mod_assets/bgs/bedroom_dawn.png"

# Space room code, ported from script-ch30
image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head
# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")
image natsuki 22b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:       #Eyes begin to fade
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png") #Smile~
image natsuki ghost3 = Image("natsuki/ghost3.png") #Snap
#Runing toward the screen
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

image n_encore_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    4.0
    easeout 8.0 alpha 1.0

image n_encore_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    4.0
    easeout 8.0 alpha 1.0

image n_encore_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    4.0
    easeout 8.0 alpha 1.0

image n_encore_rects_ghost1 large:
    RectCluster(Solid("#000"), 4, 30, 10).sm
    pos (664, 289)
    size (40, 50)
    alpha 1.0

image n_encore_rects_ghost2 large:
    RectCluster(Solid("#000"), 4, 30, 10).sm
    pos (521, 303)
    size (40, 50)
    alpha 1.0

image n_encore_rects_ghost3 large:
    RectCluster(Solid("#000"), 4, 30, 10).sm
    pos (599,385)
    size (50, 30)
    alpha 1.0

image natsuki encore_ghost_base:
    "natsuki 1ba"
image natsuki encore_ghost1:       #Eyes begin to fade
    "natsuki 1bl"
    "natsuki encore_ghost_base" with Dissolve(10.0, alpha=True)

init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight

            for i in range(self.numRects):
                self.add(self.displayable)

        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)

        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define e = Character('Echo', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define k = DynamicCharacter('k_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('a_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define r = DynamicCharacter('r_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default k_name = "Keith"
default a_name = "Akari"
default r_name = "Ria"


define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default PLAYER = persistent.playername.upper()
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"

#----Encore's New Definitions
default encore_sayoriquestion_1 = False #starting question, did they love sayori?
default encore_festivalquestion_2 = "Yuri" #who's the lucky girl or third wheel?
default encore_modquestion_3 = False #this ones not really used
default n_modappeal = 0 #daily appeals
default s_modappeal = 0
default y_modappeal = 0
default m_modappeal = 0
default n_modappealstored = 0 #appeal used for storing purposes
default s_modappealstored = 0
default y_modappealstored = 0
default m_modappealstored = 0
default hangout1 = "Sayori" #all the hangout moments throughout the day
default hangout2 = "Sayori"
default hangout3 = "Sayori"
default hangout4 = "Sayori"
default hangout5 = "Sayori"
default apologize_sn = True #If the player is dating Sayori and they hungout with anybody but Sayori on Day 2, does the player apologize to Sayori
default apologize_sy = True
default apologize_sm = True
default day = 0 #keeping track of days in case
default menu_wait_time = 7.253 #The openiing animations timer
default lpoem = "Yuri" #Who's love poem did you see on Day 2?
default tell_s = True #Do you trouble Sayori with your dreams?
default m_walk = True #Do you let Monika walk you back to class on Day 3?
default m_choice = True #Do you pick Monika's choice on Day 3?
default natsuki_hug = True #Do you return the Natsuki hug you on Day 3?
default natsuki_continued_hug = False #Do you let Natsuki keep hugging you on Day 3?
default sayori_ice = True #Do you share your ice cream with Sayori on Day 3?
default tell_monika = True #Do you tell Monika about Yuri on Day 3?
default sayori_hangout = True #Do you get food with Sayori on Day 3?
default natsuki_hangout = True #Do you hangout with Natsuki outside of school on Day 3?
default monika_hangout = True #Do you hangout with Monika outside of school on Day 3?
default yuri_hangout = True #Do you hangout with Yuri outside of school on Day 3?
default n_love = False #Do you accept Natsuki's confession on Day 4?
default y_love = False #Do you accept Yuri's confession on Day 4?

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None

image scratch:
    "#00000000"
    "mod_assets/sprites/scratch.png" with ImageDissolve("images/menu/wipeleft.png", 0.25, ramplen=4, alpha=True)
    0.25
    "#00000000" with ImageDissolve("images/menu/wipeleft.png", 0.25, ramplen=4, alpha=True)

image ouch:
    "#000000ff"
    "mod_assets/sprites/ouch.png" with Dissolve(0.25)
    0.25
    "#000000ff" with Dissolve(0.25)
    0.25
    "#00000000"

#----Encore's CGs----
image cg s_cg_1 = "mod_assets/cgs/sayori_cg1.png"
image cg s_cg_2 pin = "mod_assets/cgs/sayori_cg_2_pin.png"
image cg s_cg_day2 = "mod_assets/cgs/sayori_cg_day2.png"
image cg s_cg_2 happy = "mod_assets/cgs/sayori_cg_2_happy.png"
image cg s_cg_2 happy tears = "mod_assets/cgs/sayori_cg_2_happy_tears.png"
image cg s_cg_2 relieved = "mod_assets/cgs/sayori_cg_2_relieved.png"
image cg s_cg_2 pucker = "mod_assets/cgs/sayori_cg_2_pucker.png"
image cg s_cg_3 = "mod_assets/cgs/sayori_cg3.png"
image cg n_cg_1 = "mod_assets/cgs/natsuki_hug.png"
image cg m_cg_1 = "mod_assets/cgs/monika_cg_1.png"
image cg y_cg_1 = "mod_assets/cgs/yuri_cg_1.png"
image cg rr1 = "mod_assets/cgs/rainbow_road1.png"
image cg rr2 = "mod_assets/cgs/rainbow_road2.png"
image cg rr3 = "mod_assets/cgs/rainbow_road3.png"
image cg rr4 = "mod_assets/cgs/rainbow_road4.png"
image cg door 1 = "mod_assets/cgs/The_Door.png"
image cg door 2 = "mod_assets/cgs/The_Door_Opens.png"
image cg n_day3cg_1 = "mod_assets/cgs/n_day3cg_1.png"
image cg n_day3cg_2 = "mod_assets/cgs/n_day3cg_2.png"
image cg n_day3cg_3 = "mod_assets/cgs/n_day3cg_3.png"
image cg piano_cg = "mod_assets/cgs/piano_cg.png"
image cg piano_cg_alt = "mod_assets/cgs/piano_cgalt.png"
image cg n_day3_h2 = "mod_assets/cgs/n_day3_h2.png"


#Encore's New Sprites
image monika s = "mod_assets/sprites/ms.png"
image monika s2 = "mod_assets/sprites/ms2.png"
image monika snap = "mod_assets/sprites/The_Snap1.png"
image monika attack = shadow("mod_assets/sprites/Shadow_Attack.png")
image monika cute = "mod_assets/sprites/monika cute.png"
image monika shock =  "mod_assets/sprites/monika shock.png"
image monika smirk =  "mod_assets/sprites/monika smirk.png"
image monika surprised =  "mod_assets/sprites/monika surprised.png"
image monika tease =  "mod_assets/sprites/monika tease.png"
image shadow_attack = "mod_assets/sprites/Shadow_Attack.png"
image shadow_attack_bloody = "mod_assets/sprites/Shadow_Attack_Bloody.png"
image mb_blush = "mod_assets/sprites/mb_blush.png"
image mb_embarassed = "mod_assets/sprites/mb_embarassed.png"
image mb_flustered = "mod_assets/sprites/mb_flustered.png"
image mb_wink = "mod_assets/sprites/mb_wink.png"
image monika 1ba = "mod_assets/sprites/mb1a.png"
image monika 1bb = "mod_assets/sprites/mb1b.png"
image monika 1bd = "mod_assets/sprites/mb1d.png"
image monika 1be = "mod_assets/sprites/mb1e.png"
image monika 1bf = "mod_assets/sprites/mb1f.png"
image monika 1bg = "mod_assets/sprites/mb1g.png"
image monika 1bj = "mod_assets/sprites/mb1j.png"
image monika 1bk = "mod_assets/sprites/mb1k.png"
image monika 1bm = "mod_assets/sprites/mb1m.png"
image monika 1bn = "mod_assets/sprites/mb1n.png"
image monika 1bo = "mod_assets/sprites/mb1o.png"
image monika 1bp = "mod_assets/sprites/mb1p.png"
image monika 1bq = "mod_assets/sprites/mb1q.png"
image monika 1br = "mod_assets/sprites/mb1r.png"
image monika 1bt = "mod_assets/sprites/mb1t.png"
image monika 2bb = "mod_assets/sprites/mb2b.png"
image monika 2bc = "mod_assets/sprites/mb2c.png"
image monika 2bd = "mod_assets/sprites/mb2d.png"
image monika 2be = "mod_assets/sprites/mb2e.png"
image monika 2bf = "mod_assets/sprites/mb2f.png"
image monika 2bg = "mod_assets/sprites/mb2g.png"
image monika 2bk = "mod_assets/sprites/mb2k.png"
image monika 2bl = "mod_assets/sprites/mb2l.png"
image monika 2bm = "mod_assets/sprites/mb2m.png"
image monika 2bn = "mod_assets/sprites/mb2n.png"
image monika 2bo = "mod_assets/sprites/mb2o.png"
image monika 2bp = "mod_assets/sprites/mb2p.png"
image monika 3ba = "mod_assets/sprites/mb3a.png"
image monika 3bb = "mod_assets/sprites/mb3b.png"
image monika 3bd = "mod_assets/sprites/mb3d.png"
image monika 3be = "mod_assets/sprites/mb3e.png"
image monika 3bf = "mod_assets/sprites/mb3f.png"
image monika 3bj = "mod_assets/sprites/mb3j.png"
image monika 3bk = "mod_assets/sprites/mb3k.png"
image monika 3bl = "mod_assets/sprites/mb3l.png"
image monika 3bm = "mod_assets/sprites/mb3m.png"
image monika 3bn = "mod_assets/sprites/mb3n.png"
image monika 4ba = "mod_assets/sprites/mb4a.png"
image monika 4bb = "mod_assets/sprites/mb4b.png"
image monika 4bd = "mod_assets/sprites/mb4d.png"
image monika 4bl = "mod_assets/sprites/mb4l.png"
image monika 5ba = "mod_assets/sprites/mb5a.png"
image monika 5bb = "mod_assets/sprites/mb5b.png"
image monika 5bc = "mod_assets/sprites/mb5c.png"
image mbe_talking = "mod_assets/sprites/mbe_talking.png"
image mbe_talking2 = "mod_assets/sprites/mbe_talking2.png"
image mbe_talking3 = "mod_assets/sprites/mbe_talking3.png"
image monika_shrug = "mod_assets/sprites/monika_shrug.png"

#--uniform, hands down, slight frown, blush, closed eyes, concerned eyebrows
#image monika u113342 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/3.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/4.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/2.png")
#---uniform, hands down, slighty opened mouth, no blush, eyes forward, eyebrows lowered to stern
#image monika u114113 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/3.png")
#---uniform, hands down, slightly opened mouth, blush, eyes forward, eyebrows at neutral position
#image monika u114311 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, slightly opened mouth, blush, eyes forward, eyebrows curved upward
#image monika u114312 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/2.png")
#---Uniform, hands down, neutral closed smile, blush, eyes closed, eyebrows at neutral position
#image monika u111331 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/3.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, open mouth smile, blush, eyes closed, eyebrows curved upwards
#image monika u112332 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/2.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/3.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/2.png")
#<<<<<<< HEAD
#image monika u121351 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/5.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png") #Monika blush wink
#=======
#---uniform, right hand on hip, neutral closed smile, blush, winking, eyebrows at neutral position
#image monika u121351 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/5.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---unifrom, right hand on hip, neutral closed smile, blush, closed eyes, eyebrows at neutral position
#>>>>>>> 407fd47f18f957a39caa579bf275cce4089ed3e1
#image monika u121331 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/3.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---unifrom, right hand on hip, open mouth smile, sweat drop on cheek, closed eyes, eyebrows at neutral position
#image monika u122331 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/2.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/3.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, slightly opened mouth, blush, eyes forward, eyebrows at neutral position
#image monika u114311 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, slightly opened mouth, blush, eyes closed, eyebrows at neutral position
#image monika u114341 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/4.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, slightly opened mouth, sweat drop on cheek, eyes forward, eyebrows at neutral position
#image monika u114211 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/2.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, neutral closed smile, blush, eyes forward, eyebrows at neutral positions
#image monika u111311 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, pondering frown, no blush, eyes forward, eyebrows lowered to stern
#image monika u11h113 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/h.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/3.png")
#---uniform. hands down, neutral closed smile, no blush, eyes closed, eyebrows at neutral position
#image monika u111131 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/3.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")
#---uniform, hands down, neutral closed smile, blush, teasing gaze, low eyebrows
#image monika u111394 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/9.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/4.png")
#---uniform, hands down, neutral closed smile, no blush, winking, eyebrows at neutral position
#image monika u111151 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/monika/2_face/base.png", (0, 0), "mod_assets/character_images/monika/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/monika/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/monika/2_face/3_eyes/5.png", (0, 0), "mod_assets/character_images/monika/2_face/4_eyebrows/1.png")

#image natsuki u117232 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/7.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/3.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u227222 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/2.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/7.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u225212 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/2.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/5.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u128211 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/8.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/1.png")
#image natsuki u221232 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/2.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/3.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u211214 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/2.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/4.png")
#image natsuki u121143 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/4.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/3.png")
#image natsuki u114213 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/4.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/3.png")
#image natsuki u114253 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/4.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/5.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/3.png")
#image natsuki u112253 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/5.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/3.png")
#image natsuki u114214 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/4.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/4.png")
#image natsuki u124212 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/4.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u112212 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u111233 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/3.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/3.png")
#image natsuki u116113 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/6.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/3.png")

image natsuki_silhouette = "mod_assets/sprites/natsuki_silhouette.png"
image natsuki_pain = "mod_assets/sprites/Breaking_Neck.png"
image natsuki_rip = "mod_assets/sprites/n_kill.png"
image natsuki_sweet = "mod_assets/sprites/n_sweet.png"
image natsuki_bliss = "mod_assets/sprites/n_bliss.png"
image n_bscream = "mod_assets/sprites/n_bscream.png"
image n_cry1 = "mod_assets/sprites/n_cry1.png"
image n_cry2 = "mod_assets/sprites/n_cry2.png"

#image natsuki xu2131 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_xrossed_arms/1_body/u.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/base.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/1_mouth/2.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/3_eyes/3.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/1.png")
#image natsuki xu2143 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_xrossed_arms/1_body/u.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/base.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/1_mouth/2.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/3_eyes/4.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/3.png")
#image natsuki xu1146 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_xrossed_arms/1_body/u.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/base.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/1_mouth/1.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/3_eyes/4.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/6.png")
#image natsuki xu8172 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_xrossed_arms/1_body/u.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/base.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/1_mouth/8.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/3_eyes/7.png", (18, 22), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u112172 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/7.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")
#image natsuki u212172 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/natsuki/1_uniform/1_body_left/2.png", (0, 0), "mod_assets/character_images/natsuki/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/base.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/1_mouth/2.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/2_nose/1.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/3_eyes/7.png", (0, 0), "mod_assets/character_images/natsuki/2_face_def/4_eyebrows/2.png")

image s_kill = "mod_assets/sprites/s_kill.png"
image crayori_1 = "mod_assets/sprites/Crayori_1.png"
image crayori_2 = "mod_assets/sprites/Crayori_2.png"
image sayori_end_1 = "mod_assets/sprites/end-glitch1.png"
image sayori_end_2 = "mod_assets/sprites/end-glitch2.png"
image sayori_silhouette = "mod_assets/sprites/sayori_silhouette.png"
image sayori_ice = "mod_assets/sprites/s_ice.png"
image sayori_think = "mod_assets/sprites/sayori_think.png"
image sayori_surprised = "mod_assets/sprites/sayori_surprised.png"
image sayori_struggle = "mod_assets/sprites/sayori_struggle.png"
image sayori_dead = "mod_assets/sprites/sayori_dead.png"
image s_1pu  = "mod_assets/sprites/s_1pu.png"
image s_1pk  = "mod_assets/sprites/s_1pk.png"
image s_1pg  = "mod_assets/sprites/s_1pg.png"
image s_1pl  = "mod_assets/sprites/s_1pl.png"
image s_1pt  = "mod_assets/sprites/s_1pt.png"
image s_2pv  = "mod_assets/sprites/s_2pv.png"
image s_2pq  = "mod_assets/sprites/s_2pq.png"
image s_4pj  = "mod_assets/sprites/s_4pj.png"
image s_4pi  = "mod_assets/sprites/s_4pi.png"
image s_4pv  = "mod_assets/sprites/s_4pv.png"
image s_4pw  = "mod_assets/sprites/s_4pw.png"
image s_4pu  = "mod_assets/sprites/s_4pu.png"
image s_3pv  = "mod_assets/sprites/s_3pv.png"
image s_1py  = "mod_assets/sprites/s_1py.png"
image s_4pr  = "mod_assets/sprites/s_4pr.png"
image s_1pr  = "mod_assets/sprites/s_1pr.png"
image s_1pq  = "mod_assets/sprites/s_1pq.png"
image s_4pq  = "mod_assets/sprites/s_4pq.png"
image s_mad1  = "mod_assets/sprites/s_mad1.png"
image s_mad11  = "mod_assets/sprites/s_mad11.png"
image s_mad12  = "mod_assets/sprites/s_mad12.png"
image s_mad13  = "mod_assets/sprites/s_mad13.png"
image s_mad14  = "mod_assets/sprites/s_mad14.png"
image s_mad2  = "mod_assets/sprites/s_mad2.png"
image s_mad4  = "mod_assets/sprites/s_mad4.png"
image s_mad42  = "mod_assets/sprites/s_mad42.png"
image s_mad43  = "mod_assets/sprites/s_mad43.png"
image s_mad44  = "mod_assets/sprites/s_mad44.png"
image s_mad45  = "mod_assets/sprites/s_mad45.png"
#image sayori u114152 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori u115313 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/3.png")
#image sayori u112313 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/3.png")
#image sayori u113313 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/3.png")
#image sayori u116352 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/6.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori u111352 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori u122322 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori u111123 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/3.png")
#image sayori u114111 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/1.png")
#image sayori c112171 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_casual/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_casual/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/7.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/1.png")
#image sayori c121114 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_casual/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_casual/2_body_right/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/4.png")
#image sayori u115232 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori u115191 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/9.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/1.png")
#image sayori c123123 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_casual/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_casual/2_body_right/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/3.png")
#image sayori c115112 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_casual/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_casual/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori c114312 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_casual/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_casual/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori c111352 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_casual/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_casual/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/5.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori u111222 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/2.png")
#image sayori u222141 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/2.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/4.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/1.png")
#image sayori u121341 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/sayori/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/sayori/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/sayori/2_face/base.png", (0, 0), "mod_assets/character_images/sayori/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/sayori/2_face/2_nose/3.png", (0, 0), "mod_assets/character_images/sayori/2_face/3_eyes/4.png", (0, 0), "mod_assets/character_images/sayori/2_face/4_eyebrows/1.png")

image yuri_silhouette = "mod_assets/sprites/yuri_silhouette.png"
image yuri_prestab = "mod_assets/sprites/yuri_prestab.png"
image yuri_stab = "mod_assets/sprites/yuri_stab.png"
image yuri_rip = "mod_assets/cgs/yuri_rip.png"
image yb1 = "mod_assets/sprites/yb1.png"
image yb2 = "mod_assets/sprites/yb2.png"
image yb3 = "mod_assets/sprites/yb3.png"
image yb4 = "mod_assets/sprites/yb4.png"
image yb5 = "mod_assets/sprites/yb5.png"
image yb6 = "mod_assets/sprites/yb6.png"
image yb7 = "mod_assets/sprites/yb7.png"
image y_mad = "mod_assets/sprites/GrrYuri.png"
image y2by1 = "mod_assets/sprites/y2by1.png"
image y2by3 = "mod_assets/sprites/y2by3.png"
image y2by4 = "mod_assets/sprites/y2by4.png"
image yuri_ghost1 = "mod_assets/sprites/yuri_ghost1.png"
image yuri_ghost2 = "mod_assets/sprites/yuri_ghost2.png"
image yuri_ghost3 = "mod_assets/sprites/yuri_ghost3.png"
image yuri_ghost4 = "mod_assets/sprites/yuri_ghost4.png"
image yuri_knife1 = "mod_assets/sprites/yuri_knife1.png"
image yuri_knife2 = "mod_assets/sprites/yuri_knife2.png"
image yuri_knife3 = "mod_assets/sprites/yuri_knife3.png"
image yuri_knife4 = "mod_assets/sprites/yuri_knife4.png"
image yuri_knife5 = "mod_assets/sprites/yuri_knife5.png"
image yuri_knife6 = "mod_assets/sprites/yuri_knife6.png"
image y_cry1 = "mod_assets/sprites/y_cry1.png"
image y_cry2 = "mod_assets/sprites/y_cry2.png"
image y_cry3 = "mod_assets/sprites/y_cry3.png"
image y_cry4 = "mod_assets/sprites/y_cry4.png"
image y_cry5 = "mod_assets/sprites/y_cry5.png"
image y_cry6 = "mod_assets/sprites/y_cry6.png"
image pen = "mod_assets/sprites/pen.png"
#image yuri u122218 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/yuri/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/yuri/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/base.png", (0, 0), "mod_assets/character_images/yuri/2_face/1_mouth/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/2_nose/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/4_eyebrows/8.png")
#image yuri u114221 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/yuri/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/yuri/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/base.png", (0, 0), "mod_assets/character_images/yuri/2_face/1_mouth/4.png", (0, 0), "mod_assets/character_images/yuri/2_face/2_nose/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/3_eyes/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/4_eyebrows/1.png")
#image yuri u125111 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/yuri/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/yuri/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/base.png", (0, 0), "mod_assets/character_images/yuri/2_face/1_mouth/5.png", (0, 0), "mod_assets/character_images/yuri/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/4_eyebrows/1.png")
#image yuri u123114 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/yuri/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/yuri/1_uniform/2_body_right/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/base.png", (0, 0), "mod_assets/character_images/yuri/2_face/1_mouth/3.png", (0, 0), "mod_assets/character_images/yuri/2_face/2_nose/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/3_eyes/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/4_eyebrows/4.png")
#image yuri u111261 = im.Composite((960, 960), (0, 0), "mod_assets/character_images/yuri/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/character_images/yuri/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/base.png", (0, 0), "mod_assets/character_images/yuri/2_face/1_mouth/1.png", (0, 0), "mod_assets/character_images/yuri/2_face/2_nose/2.png", (0, 0), "mod_assets/character_images/yuri/2_face/3_eyes/6.png", (0, 0), "mod_assets/character_images/yuri/2_face/4_eyebrows/1.png")

image airpod left = "mod_assets/sprites/apl.png"
image airpod right = "mod_assets/sprites/apr.png"
image airpod both = im.Composite((960, 960), (0, 0), "mod_assets/sprites/apl.png", (0, 0), "mod_assets/sprites/apr.png")
image icecream = "mod_assets/sprites/icecream.png"

# Silhouettes
image sayori 1shadow = shadow("mod_assets/sprites/char_bases/s_base")
image sayori 1bshadow = shadow("mod_assets/sprites/char_bases/sb_base")
image natsuki 1shadow = shadow("mod_assets/sprites/char_bases/n_base")
image natsuki 1b shadow = shadow("mod_assets/sprites/char_bases/nb_base")
image yuri 1shadow = shadow("mod_assets/sprites/char_bases/y_base")
image yuri 1bshadow = shadow("mod_assets/sprites/char_bases/yb_base")
image monika 1shadow = shadow("mod_assets/sprites/char_bases/m_base")

image yuri strobe:
    block:
        "mod_assets/sprites/yuri_ghost3.png" # Show the first image
        0.1 # Wait this many seconds
        "mod_assets/sprites/yuri_ghost4.png" # Show the second image
        0.1 # Wait this many seconds
        repeat # Repeat over and over

    #time 3.0 # After this many seconds, stop flashing and show the next image
    # copied from yuri 3y3
    #im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0))

#This channel is used for times when secondary tracks are needed to be played aside music.
#like if we needed m1 to play AND heartbeat to play
init python:
    renpy.music.register_channel("ambient", "sfx", stop_on_mute=True, tight=True)
