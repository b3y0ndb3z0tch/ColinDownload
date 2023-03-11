#Add SCROLL function on CREATEEVENTSCREEN for the quick_event_buttons
#Lines 2660 show the iteration through a dictionary into dictionary
#need to work on line 2807 to edit from reading from list to reading from dict
#
#NEED TO COMPLETE EVENT PAGE SHOWING AND DISPLAY
#When Searching player using multiple fields, need to only return that player once
#When Creating a player need to check the fields to make sure they have a correct input
#IE FOR CREATING PLAYER FIELDS
#Phone starts with 1 and has 10 digits
#Email has @---.com
#Need to check if position works with/without spacing FDG F D G
#Need to check if LINE works with/without spacing 12 1 2
#Need to check if OUT is true of False
import json

from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivymd.material_resources import dp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton, MDRoundFlatButton, MDRectangleFlatIconButton, \
    MDRectangleFlatButton
from kivymd.uix.card import MDCard, MDCardSwipe, MDSeparator
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanelThreeLine
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget, OneLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch, \
    ThreeLineAvatarIconListItem, TwoLineAvatarIconListItem, TwoLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
import TestingIndividualLogicCode.testingfunctions
import TestingIndividualLogicCode.automatingdays
import TestingIndividualLogicCode.alerts
import TestingIndividualLogicCode.makingtable
#import TestingIndividualLogicCode.quickevent
from kivy.properties import partial
from kivymd.uix.list import OneLineListItem

from kivymd.uix.list import MDList


#from KivyMD.kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

#if movies_dict.get('year') is not None:

Window.size = (300, 500)


navigation_helper = """

<CompletedEvents>:
    line_color: 
    size_hint_y: None
    height: content.height*1.5
    on_swipe_complete: app.on_swipe_completeevents(root)
    # padding: '8dp'
    # spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.
        md_bg_color: 0,0,0,.2

    MDCardSwipeFrontBox:
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: .8,.3,.2,1
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.08)
            # MDBoxLayout:
            #     orientation: 'vertical'
            #     #md_bg_color: .2,.53,.733,1 #blue
            #     md_bg_color: .8,.3,.2,1 #orange
            # # Content of card.
            MDAnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                ThreeLineListItem:
                    id: content
                    pos_hint: {"center_x":.5, "center_y":.5}
                    text: root.text2
                    secondary_text: root.second_text2
                    tertiary_text: root.third_text2
                    event_id2: root.event_id2
                    _no_ripple_effect: True
                    on_release: 
                        print(root.third_text2)
                        print(root.event_id2)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.05)
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.1)
                
<SwipeToDeleteItem2>:
    line_color: 
    size_hint_y: None
    height: content.height*1.5
    on_swipe_complete: app.on_swipe_complete2(root)
    # padding: '8dp'
    # spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.
        md_bg_color: 0,0,0,.2

    MDCardSwipeFrontBox:
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: .8,.3,.2,1
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.08)
            # MDBoxLayout:
            #     orientation: 'vertical'
            #     #md_bg_color: .2,.53,.733,1 #blue
            #     md_bg_color: .8,.3,.2,1 #orange
            # # Content of card.
            MDAnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                ThreeLineListItem:
                    id: content
                    pos_hint: {"center_x":.5, "center_y":.5}
                    text: root.text2
                    secondary_text: root.second_text2
                    tertiary_text: root.third_text2
                    event_id2: root.event_id2
                    _no_ripple_effect: True
                    on_release: 
                        print(root.third_text2)
                        print(root.event_id2)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.05)
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.1)

            

<PlayerNotificationCard>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.remove_player_from_notification(root)
    # padding: '8dp'
    # spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        # Content of card.
        ThreeLineListItem:
            id: content
            text: root.text2
            secondary_text: root.second_text2
            tertiary_text: root.third_text2
            player_id: root.player_id
            _no_ripple_effect: True
            on_release: 
                print(root.third_text2)
                print(root.player_id)
    
<SwipeToDeletePlayerCard>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.on_swipe_complete3(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        bg_color: .8,.3,.2,1
        # Player Content of card.
        ThreeLineListItem:
            id: content
            text: root.text3
            secondary_text: root.second_text3
            tertiary_text: root.third_text3
            search_player_id: root.search_player_id
            _no_ripple_effect: True
            on_release: 
                print("Releasing")
                print(root.third_text3)
                print(root.search_player_id)
                
<SwipeToAddSearchToEvent>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.on_swipe_complete4(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        bg_color: .8,.3,.2,1
        # Player Content of card.
        ThreeLineListItem:
            id: content
            text: root.text3
            secondary_text: root.second_text3
            tertiary_text: root.third_text3
            search_player_id: root.search_player_id
            _no_ripple_effect: True
            on_release: 
                print("Releasing")
                print(root.third_text3)
                print(root.search_player_id)


<SwipeToAddPlayerToInList>:
    size_hint_y: None
    height: content.height * .9
    on_swipe_complete: app.add_player_to_in_list(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        #Player Content of card.
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: .8,.3,.2,1
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            MDAnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                size_hint: (1, .8)      
                ThreeLineListItem:
                    id: content
                    #pos_hint: {"center_x":.5, "center_y":.5}
                    text: root.text
                    secondary_text: root.second_text
                    _no_ripple_effect: True
                    on_release: 
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.1)
 
 
<SwipeToRemovePlayerFromAllEmail>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.remove_player_from_all_email_list(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        #Player Content of card.
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: .8,.3,.2,1
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            # MDAnchorLayout:
            #     anchor_x: 'center'
            #     anchor_y: 'center'
            #     size_hint: (1, .8)      
                
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: .2,.53,.733,1 #blue
                #md_bg_color: .8,.3,.2,1 #orange
                size_hint:(1,.1)
            MDSeparator:
                color: 1,1,1,1
                size_hint:(1,.1)
            ThreeLineListItem:
                id: content
                #pos_hint: {"center_x":.5, "center_y":.5}
                text: root.text
                secondary_text: root.second_text
                _no_ripple_effect: True
                on_release: 
 
# <SwipeToRemovePlayerFromAllEmail>:
#     size_hint_y: None
#     height: content.height * .5
#     on_swipe_complete: app.remove_player_from_all_email_list(root)
#     padding: '8dp'
#     spacing: '20dp'
#     MDCardSwipeLayerBox:
#         # Content under the card.
# 
#     MDCardSwipeFrontBox:
#         md_bg_color: .8,.3,.2,1
#         #Player Content of card.
#         MDBoxLayout:
#             orientation: 'vertical'
#             md_bg_color: .8,.3,.2,1
#             MDBoxLayout:
#                 orientation: 'vertical'
#                 md_bg_color: .2,.53,.733,1 #blue
#                 #md_bg_color: .8,.3,.2,1 #orange
#                 size_hint:(1,.1)
#             MDAnchorLayout:
#                 anchor_x: 'center'
#                 anchor_y: 'center'
#                 size_hint: (1, .8)      
#                 ThreeLineListItem:
#                     id: content
#                     #pos_hint: {"center_x":.5, "center_y":.5}
#                     text: root.text
#                     secondary_text: root.second_text
#                     _no_ripple_effect: True
#                     on_release: 
#             MDBoxLayout:
#                 orientation: 'vertical'
#                 md_bg_color: .2,.53,.733,1 #blue
#                 #md_bg_color: .8,.3,.2,1 #orange
#                 size_hint:(1,.1)
#             MDSeparator:
#                 color: 1,1,1,1
#                 size_hint:(1,.1)
 
 
 
<SwipeToPayPlayer>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.player_paid(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.
    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        #Player Content of card.
        ThreeLineListItem:
            id: content
            text: root.text
            secondary_text: root.second_text
            player_id: root.player_id
            _no_ripple_effect: True
            on_release: 

<SwipeToPayPlayer2>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.player_paid(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.
    MDCardSwipeFrontBox:
        md_bg_color: 0,1,0,1
        #Player Content of card.
        ThreeLineListItem:
            id: content
            text: root.text
            secondary_text: root.second_text
            player_id: root.player_id
            _no_ripple_effect: True
            on_release:
 
 
<SwipeToRemoveRegularFromEmailList>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.remove_regular_from_email_list(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            on_release:


<SwipeToRemoveAllFromEmailList>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.remove_all_from_email_list(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            on_release:


<SwipeToRemoveIndividualFromEmailList>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.remove_individual_from_email_list(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            on_release:
   
<SwipeToRemoveSubFromEmailList>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.remove_sub_from_email_list(root)
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            on_release:

<OrganizePlayerToTeam>:
    text: root.text
    secondary_text: root.second_text
    #tertiary_text: root.third_text
    player_id: root.player_id
    bg_color: .8,.3,.2,1
    on_size:
        # self.ids._left_container.width = left_container.width
        # self.ids._left_container.x = left_container.width
        # self.ids._right_container.width = right_container.width
        # self.ids._right_container.x = right_container.width
    on_press:
        print("You just clicked the main player card")
        app.add_under_player_card(root)
                
<OrganizeD1Line>:
    text: root.text
    secondary_text: root.second_text
    pos_hint: {"center_x": 0.5}
    player_id: root.player_id
    bg_color: .2,.53,.733,1
    IconLeftWidget:
        icon:"plus"
        on_press:
            print("plus was pressed")
            #app.organize_event_add_to_dark(root)
    IconRightWidget:
        icon:"minus"
        on_press:
            print("minus was pressed")
            #app.organize_event_add_to_light(root)

<OrganizeD2Line>:
    text: root.text
    secondary_text: root.second_text
    pos_hint: {"center_x": 0.5}
    player_id: root.player_id
    bg_color: .4,.63,.79,.5
    IconLeftWidget:
        icon:"plus"
        on_press:
            print("plus was pressed")
            #app.organize_event_add_to_dark(root)
    IconRightWidget:
        icon:"minus"
        on_press:
            print("minus was pressed")
            #app.organize_event_add_to_light(root)

<OrganizeL1Line>:
    text: root.text
    secondary_text: root.second_text
    player_id: root.player_id
    bg_color: .8,.3,.2,1
    IconLeftWidget:
        icon:"plus"
        on_press:
            print("plus was pressed")
            #app.organize_event_add_to_dark(root)
    IconRightWidget:
        icon:"minus"
        on_press:
            print("minus was pressed")
            #app.organize_event_add_to_light(root)
<OrganizeL2Line>:
    text: root.text
    text_color: 
    secondary_text: root.second_text
    player_id: root.player_id
    bg_color: .95,.54,.47,.5
    IconLeftWidget:
        icon:"plus"
        on_press:
            print("plus was pressed")
            #app.organize_event_add_to_dark(root)
    IconRightWidget:
        icon:"minus"
        on_press:
            print("minus was pressed")
            #app.organize_event_add_to_light(root)

<OrganizeDark1Team>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: print("Swiping")
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .2,.53,.733,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            player_id: root.player_id
            _no_ripple_effect: True
            on_release: 

<OrganizeDark2Team>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: print("Swiping")
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .4,.63,.79,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            player_id: root.player_id
            _no_ripple_effect: True
            on_release: 
    
<OrganizeLight1Team>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: print("Swiping")
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            player_id: root.player_id
            _no_ripple_effect: True
            on_release:    
<OrganizeLight2Team>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: print("Swiping")
    padding: '8dp'
    spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .95,.54,.47,1
        # Player Content of card.
        OneLineListItem:
            id: content
            text: root.text
            player_id: root.player_id
            _no_ripple_effect: True
            on_release:

<TryingButtonDark>:
    text: root.text
    player_id: root.player_id
    md_bg_color: .01,.5,1,1
    pos_hint: {"center_x": .5, "center_y": .5}

<RegularAllEmail>:
    text: root.text
    player_id: root.quick_event
    md_bg_color: .01,.5,1,1
    pos_hint: {"center_x": .5, "center_y": .5}

<SubstituteAllEmail>:
    text: root.text
    player_id: root.quick_event
    md_bg_color: 1,.5,.1,1
    pos_hint: {"center_x": .5, "center_y": .5}

<OpenAllEmail>:
    text: root.text
    player_id: root.quick_event
    md_bg_color: 0,0,0,.15
    pos_hint: {"center_x": .5, "center_y": .5}


<TryingButtonDark2>:
    text: root.text
    player_id: root.player_id
    md_bg_color: .01,.5,1,.5
    pos_hint: {"center_x": .5, "center_y": .5}
    
<TryingButtonLight>:
    text: root.text
    player_id: root.player_id
    md_bg_color: 1,.5,.1,1
    pos_hint: {"center_x": .5, "center_y": .5}
    
<TryingButtonLight2>:
    text: root.text
    player_id: root.player_id
    md_bg_color: 1,.5,.1,.5
    pos_hint: {"center_x": .5, "center_y": .5}

<QuickEventButtonLight>:
    text: root.text
    event_id: root.event_id
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: (.6, None)
    md_bg_color: 1,.5,.1,1

<QuickEventButtonDark>:
    text: root.text
    event_id: root.event_id
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: (.85, None)
    md_bg_color: .01,.5,1,1

#START OF APP
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            MDScreen:
                name: "HomeScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "BAH"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    BoxLayout:
                        orientation: 'vertical'
                        id: home_screen
            MDScreen:
                name: "NotificationScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "BAH"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    BoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            scroll_timeout: 100
                            do_x_scroll: True
                            MDList:
                                id: notifications
                                spacing:5
                        
#Create Event Button Flow START
            MDScreen:
                name: "CreateEventScreen"
                BoxLayout:
                    orientation: 'vertical'
                    #spacing: 15
                    MDTopAppBar:
                        title: "Create Event"
                        elevation: 2
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    MDSeparator:
                    MDBoxLayout:
                        id: quick_button_layout
                        orientation: 'vertical'
                        spacing: 5
                        #md_bg_color: 1,0,0,1 changes whole screen to red 
                        MDAnchorLayout:
                            size_hint: (1, .3)
                            #adaptive_height: True
                            anchor_x: 'center'
                            padding: [20, 5, 20, 5]
                            md_bg_color: 0,0,0,.5
                            
                            ScrollView:
                                scroll_timeout: 100
                                do_x_scroll: True
                                MDList:
                                    id: grid_for_quick_event_buttons
                                    spacing: 10                                    
                        MDSeparator:
                        AnchorLayout:
                            adaptive_height: True
                            anchor_x: 'center'
                            padding: [15, 0, 15, 5]
                            md_bg_color: .67,.67,.67,1
                            ScrollView:
                                scroll_timeout: 100
                                do_x_scroll: True
                                MDList:
                                    spacing: 5
                                    #md_bg_color: .67,.67,.67,.3
                                    MDTextField:
                                        id: date
                                        hint_text: "Date: MMDDYY - 010522"
                                        max_text_lenght: 6
                                        pos_hint: {"center_x": .5, "top": 1}
                                        size_hint: (.85, None)
                                    MDTextField:
                                        id: time
                                        hint_text: "Time: 0900pm"
                                        helper_text: "900PM"
                                        pos_hint: {"center_x": .5, 'center_y': .7}
                                        size_hint: (.85, None)
                                    MDTextField:
                                        id: day
                                        hint_text: "Day: Monday"
                                        pos_hint: {"center_x": .5, "top": 1}
                                        size_hint: (.85, None)
                                    MDTextField:
                                        id: location
                                        hint_text: "Location: Kroc"
                                        pos_hint: {"center_x": .5, 'center_y': .5}
                                        size_hint: (.85, None)
                                    MDTextField:
                                        id: cost
                                        hint_text: "Cost: 30"
                                        pos_hint: {"center_x": .5, 'center_y': .3}
                                        size_hint: (.85, None)
                                    MDTextField:
                                        id: totalplayers
                                        hint_text: "TOTAL PLAYERS"
                                        pos_hint: {"center_x": .5, 'center_y': .2}
                                        size_hint: (.85, None)
                                    MDRaisedButton:
                                        text: "Submit"
                                        pos_hint: {"center_x": .5, 'center_y': .1}
                                        size_hint: (.85, None)
                                        on_press:
                                            app.create_event(root)
                                            #root.ids.screen_manager.current = "CurrentEventsPage"
            MDScreen:
                name: "CurrentEventsPage"
                MDBoxLayout:
                    orientation: 'vertical'
                    #padding: [10,5,10,5]
                    MDTopAppBar:
                        title: "Current Events"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    ScrollView:
                        scroll_timeout: 100
                        padding: [12,5,12,15]
                        MDList:
                            id: currentevents_md_list
                            padding: [12,5,12,15]
                            spacing: '10dp'
#Create Event Button Flow START
#Players Button Flow START
            MDScreen:
                name: "SearchPlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Search Player"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                    MDSeparator:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 15
                        AnchorLayout:
                            #size_hint_x: 1
                            adaptive_height: True
                            anchor_x: 'center'
                            padding: [20, 5, 20, 5]
                            ScrollView:
                                scroll_timeout: 100
                                MDList:
                                    id: search_fields
                                    size_hint: (1, None)
                    MDRaisedButton:
                        text: "Search Players"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
                        on_press:
                            app.searchplayers()
#Search Player Found START
            MDScreen:
                name: "FoundPlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Found/Search"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: found_player_md_list
                            padding: '10dp'
                            spacing: '10dp'
                    MDRaisedButton:
                        text: "Found Player Screen Button"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
#Found Player From Search Screen Start
            MDScreen:
                name: "SpecificFoundPlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    id: testing
                    MDTopAppBar:
                        title: "Edit Player Info"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: specific_found_player_md_list
                            padding: '15dp'
                            spacing: '15dp'
                    MDRaisedButton:
                        text: "Save Edited Player"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
                        on_press:
                            print("time to stick back into the .json file")
                            app.saveeditfromsearchplayer()
#Create Event Button Flow END
#Players Button Flow END
#Search Player Found END
#Found Player From Search Screen END
#Players Create Player Button START
            MDScreen:
                name: "CreatePlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Create Player"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                    MDSeparator:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 15
                        AnchorLayout:
                            #size_hint_x: 1
                            adaptive_height: True
                            anchor_x: 'center'
                            padding: [20, 5, 20, 5]
                            ScrollView:
                                scroll_timeout: 100
                                MDList:
                                    id: create_player_fields
                    MDRaisedButton:
                        text: "Create Player"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
                        on_press:
                            app.save_create_player(root)
#Players Create Player Button END
#Manage Quick EVENTS Button START
#Add Quick Event Button START
            MDScreen:
                name: "CreateQuickEventScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Quick Event"
                        elevation: 2
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    MDSeparator:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 15
                        padding: [20,5,20,5]
                        MDTextField:
                            id: quick_time
                            hint_text: "Time: 0900pm"
                            helper_text: "900PM"
                            pos_hint: {"center_x": .5, 'center_y': .7}
                            size_hint: (1, None)
                        MDTextField:
                            id: quick_day
                            hint_text: "Day: Monday"
                            pos_hint: {"center_x": .5, "top": 1}
                            size_hint: (1, None)
                        MDTextField:
                            id: quick_location
                            hint_text: "Location: Kroc"
                            pos_hint: {"center_x": .5, 'center_y': .5}
                            size_hint: (1, None)
                        MDTextField:
                            id: quick_cost
                            hint_text: "Cost: 30"
                            pos_hint: {"center_x": .5, 'center_y': .3}
                            size_hint: (1, None)
                        MDTextField:
                            id: quick_totalplayers
                            hint_text: "TOTAL PLAYERS"
                            pos_hint: {"center_x": .5, 'center_y': .2}
                            size_hint: (1, None)
                        MDRaisedButton:
                            text: "Submit"
                            pos_hint: {"center_x": .5, 'center_y': .1}
                            size_hint: (1, None)
                            on_press:
                                app.create_quick_event(root)
                                root.ids.screen_manager.current = "CreateEventScreen"
#Add Quick Event Button END
#Back To Create Event Screen
#Edit Quick Event Button START
#Delete Quick Event Button START
            MDScreen:
                name: "EditQuickEventScreen"
                BoxLayout:
                    orientation: 'vertical'
                    #spacing: 15
                    MDTopAppBar:
                        title: "Edit Qck Event"
                        elevation: 2
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    MDBoxLayout:
                        orientation: 'vertical'
                        #md_bg_color: 0,0,0,.1
                        spacing: 10
                        MDAnchorLayout:
                            size_hint: (1,3)
                            #adaptive_height: True
                            anchor_x: 'center'
                            padding: [20, 5, 5, 35]
                            md_bg_color: 1,1,1,.3
                            MDScrollView:
                                scroll_timeout: 100
                                do_x_scroll: True
                                MDList:
                                    id: edit_quick_event_layout
                                    spacing: 15
                        MDAnchorLayout:
                            id: edit_quick_event_layout2
                            padding: [0,0,10,0]
                            #md_bg_color: 1,1,1,.3
                            size_hint: (1, .1)
                            #adaptive_height: True
                            anchor_x: 'center'
                            anchor_y: 'bottom'
                                
                            
                                
                                
#Edit Quick Event Button END  
#Delete Quick Event Button END
#Right Nav Events Current Events Button START
#Takes you to Current Events Screen      
#SLIDE EVENT START
            MDScreen:
                name: "SpecificEventPage"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Invited Guests"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                        right_action_items: 
                            [
                            ['account-alert', lambda x: app.display_assigned_dark()],
                            ['account-alert-outline', lambda x: app.change_light_assign()],
                            ['menu', lambda x: nav_drawer3.set_state('open')]
                            ]
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDBoxLayout:
                            id: specific_event_page_box_layout
                            orientation: 'vertical'
                            size_hint: (1,.2)
                            md_bg_color: (0,0,0,.15)
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: specific_event_label
                                spacing: '8dp'
                                padding: '8dp'
                                # MDLabel:
                                #     text: "Invited Players"
                                #     halign: 'center'
                                #     spacing: '8dp'
#Tool Bar Dark Team Button START
            MDScreen:
                name: "AssignDark"
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: [10, 3, 10, 5]
                    #spacing: '15dp'
                    MDTopAppBar:
                        title: "Dark Lines"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: 
                            [
                            #['home', lambda x: app.change_home_screen()],
                            ['home-export-outline',lambda x: app.back_to_current_event()]
                            ]
                        right_action_items: 
                            [
                            ['account-switch-outline', lambda x: app.display_teams()],
                            ['account-alert-outline', lambda x: app.change_light_assign()],
                            ['menu', lambda x: nav_drawer3.set_state('open')]
                            ]                           
                    MDBoxLayout:   
                        orientation: 'vertical'
                        padding: [15,5,15,5]                   
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_dark_line1
                                spacing: '10dp'
                        MDSeparator:
                            color: .8,.3,.2,1
                            size_hint: (1,.025)
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_dark_line2
                                spacing: '10dp'
#Tool Bar Dark Team Button END
#Tool Bar Light Team Button START    
            MDScreen:
                name: "AssignLight"
                BoxLayout:
                    orientation: 'vertical'
                    padding: [10, 3, 10, 5]
                    #spacing: '15dp'
                    MDTopAppBar:
                        title: "Light Lines"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: 
                            [
                            #['home', lambda x: app.change_home_screen()],
                            ['home-export-outline',lambda x: app.back_to_current_event()]
                            ]
                        right_action_items: 
                            [
                            ['account-switch-outline', lambda x: app.display_teams()],
                            ['account-alert', lambda x: app.display_assigned_dark()],
                            ['menu', lambda x: nav_drawer3.set_state('open')]
                            ]                           
                    MDBoxLayout:   
                        orientation: 'vertical' 
                        padding: [15,5,15,5]                  
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_light_line1
                                spacing: '10dp'
                        MDSeparator:
                            color: .2,.53,.733,1
                            size_hint: (1,.025)
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_light_line2
                                spacing: '10dp'  
#Tool Bar Light Team Button END  
#Tool Bar Both Team Button START                
            MDScreen:
                name: "DisplayTeams"
                BoxLayout:
                    orientation: 'vertical'
                    padding: [0, 0, 0, 0]
                    #spacing: '15dp'
                    MDTopAppBar:
                        title: "Full Teams"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: 
                            [
                            #['home', lambda x: app.change_home_screen()],
                            ['home-export-outline',lambda x: app.back_to_current_event()]
                            ]
                        right_action_items: 
                            [
                            ['email-edit-outline', lambda x: app.send_final_email()], #in the send_final_email function
                            ['menu', lambda x: nav_drawer3.set_state('open')] 
                            ]                           
                    MDBoxLayout:
                        padding: [5,5,5,5]
                        spacing: 15                    
                        MDScrollView:
                            scroll_timeout: 100
                            padding: [0,5,2,0]
                            MDList:
                                id: display_dark
                                spacing: '25dp'
                        MDScrollView:
                            scroll_timeout: 100
                            padding: [0,5,2,0]
                            MDList:
                                id: display_light
                                spacing: '25dp' 
#Tool Bar Both Team Button END
#Email Button calls send_final_email function START END
#Invite Players Button START
#Invite Regulars Button START           
            MDScreen:
                name: "InviteRegularsScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Invite Regulars"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home-export-outline', lambda x: app.change_to_event_home_screen()]]
                        right_action_items: [['menu', lambda x: nav_drawer3.set_state('open')]]
                    MDBoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            scroll_timeout: 100
                            size_hint: (1,.3)
                            MDList:
                                id: list_of_regulars_display
                        ScrollView:
                            scroll_timeout: 100
                            size_hint: (1,1)
                            MDTextField:
                                id: quick_event_text
                                multiline: True
                                pos_hint_x: {"center_x": .5}
                                size_hint: (.8, None)
                        MDRaisedButton:
                            text: "Send Regular Email"
                            size_hint: (1, None)
                            on_press:
                                app.inviteregularssendemail()   
#Invite Regulars Button END

#Invite ALL Players Button START           
            MDScreen:
                name: "InviteAllPLayersScreen"
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '15dp'
                    MDTopAppBar:
                        title: "Sd Reg Eml 2:"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home-export-outline', lambda x: app.change_to_event_home_screen()]]
                        right_action_items: [['menu', lambda x: nav_drawer3.set_state('open')]]
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDScrollView:
                            scroll_timeout: 100
                            padding: [10,5,10,15]
                            size_hint: (1,.35)
                            MDList:
                                id: email_all_players
                                padding: [15, 5, 15, 5]
                                spacing: '10dp'
                        MDSeparator:
                        
                        ScrollView:
                            scroll_timeout: 100
                            size_hint: (1,1)
                            MDTextField:
                                id: all_players_quick_event_text
                                multiline: True
                                pos_hint_x: {"center_x": .5}
                                size_hint: (.8, None)
                        MDScrollView:
                            scroll_timeout: 100
                            padding: [10,5,10,15]
                            size_hint: (1,.35)
                            MDList:
                                id: all_players_getting_email
                                spacing: '8dp'
                                padding: '8dp'
                        MDRaisedButton:
                            text: "Send This Event Email To:"
                            size_hint: (1, None)
                            on_press:
                                app.allplayersinviteemail()   
#Invite ALL Players Button END

#Send Regular Email Button calls inviteregularssendemail START END
#Invite Players Invite Subs Button START
            MDScreen:
                name: "InviteSubsScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Invite Subs"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home-export-outline', lambda x: app.change_to_event_home_screen()]]
                        right_action_items: [['menu', lambda x: nav_drawer3.set_state('open')]]
                    MDBoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            scroll_timeout: 100
                            size_hint: (1, .3)
                            MDList:
                                id: list_of_subs_display  
                        ScrollView:
                            scroll_timeout: 100
                            size_hint: (1, 1)
                            MDTextField:
                                id: quick_event2_text
                                multiline: True
                                pos_hint_x: {"center_x": .5}
                                size_hint: (.8, None)
                        MDRaisedButton:
                            text: "Send Sub Email"
                            size_hint: (1, None)
                            on_press:
                                app.invitesubssendemail()
#Invite Players Invite Subs Button END 
#Send Regular Email Button calls invitesubssendemail START END
#Invite Players Invite Individual Player Button START
            MDScreen:
                name: "SearchInviteIndividualPlayer"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Search Individual"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: 
                            [
                            ['home-export-outline',lambda x: app.back_to_current_event()]
                            ]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: search_fields2
                            MDTextField:
                                id: playerfirst2
                                hint_text: "First Name"
                                pos_hint: {"center_x": .5, "top": 1}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerlast2
                                hint_text: "Last Name"
                                pos_hint: {"center_x": .5, 'center_y': .7}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerphone2
                                hint_text: "Phone Number 12345678901"
                                pos_hint: {"center_x": .5, "top": 1}
                                size_hint: (1, None)
                            MDTextField:
                                id: playeremail2
                                hint_text: "Email"
                                pos_hint: {"center_x": .5, 'center_y': .5}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerposition2
                                hint_text: "Position F D G"
                                pos_hint: {"center_x": .5, 'center_y': .3}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerline2
                                hint_text: "Line #"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)
                    MDRaisedButton:
                        text: "Search Players"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
                        on_press:
                            app.invitesearchplayers()
#Search Players Button calls invitesearchplayers
#Brings Into Event Found Player Screen
            MDScreen:
                name: "FoundEventInvitePlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Event Found Player"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home-export-outline', lambda x: app.change_to_event_home_screen()]]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: found_event_player_md_list
                            padding: '10dp'
                            spacing: '10dp'
                    MDRaisedButton:
                        text: "GOTO SEND EMAIL"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
                        on_press:
                            app.gotoindividualemail()
                            print("Called: app.gotoindividualemail() from FoundEventInvitePlayerScreen")
#Invite Players Invite Individual Player Button END
#Slide Individual Player START
#Goto Send Email Button calls gotoindividualemail
            MDScreen:
                name: "InviteIndividualsScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Invite Individuals"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home-export-outline', lambda x: app.change_to_event_home_screen()]]
                        right_action_items: [['menu', lambda x: nav_drawer3.set_state('open')]]
                    MDBoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            scroll_timeout: 100
                            size_hint: (1,.3)
                            MDList:
                                id: list_of_individuals_display
                        ScrollView:
                            scroll_timeout: 100
                            size_hint: (1,1)
                            MDTextField:
                                id: quick3_event_text
                                multiline: True
                                pos_hint_x: {"center_x": .5}
                                size_hint: (.8, None)
                        MDRaisedButton:
                            text: "Send Individual Email"
                            on_press:
                                app.invitefoundplayerssendemail()      
#Slide Individual Player END
#Send Individual Email Button calls invitefoundplayerssendemail function
#Right Nav Drawer Button
#Organize Attendees Button START
            MDScreen:
                name: "OrganizeEventScreen"
                BoxLayout:
                    orientation: 'vertical'
                    #spacing: '15dp'
                    MDTopAppBar:
                        title: "Organize Event"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: 
                            [
                            #['home', lambda x: app.change_home_screen()],
                            ['home-export-outline',lambda x: app.back_to_current_event()]
                            ]
                        right_action_items: 
                            [
                            ['account-alert', lambda x: app.display_assigned_dark()],
                            ['account-alert-outline', lambda x: app.change_light_assign()],
                            ['menu', lambda x: nav_drawer3.set_state('open')]
                            ]
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDBoxLayout:
                            id: organize_event_page_box_layout
                            orientation: 'vertical'
                            size_hint: (1,.2)     
                            md_bg_color: 0,0,0,.2        
                        ScrollView:
                            scroll_timeout: 100
                            #size_hint: (1,.5)
                            #size: (Window.width, Window.height- dp(20))
                            MDList:
                                id: organize_event_label
                                spacing: '15dp'
                        # MDBottomAppBar:
                        #     MDTopAppBar:
                        #         type: "bottom"
                        #         md_bg_color: .8,.3,.2,1
                        #         left_action_items: [['account-alert', lambda x: app.display_assigned_dark()]]
                        #         right_action_items: [['account-alert-outline', lambda x: app.change_light_assign()]]
#Organize Attendees Button END
#Right Nav Drawer Button
#Payment Button START
            MDScreen:
                name: "PaymentPage"
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    MDTopAppBar:
                        title: "Make Payment"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home-export-outline', lambda x: app.change_to_event_home_screen()]]
                        right_action_items: 
                            [
                            ['account-alert', lambda x: app.display_assigned_dark()],
                            ['account-alert-outline', lambda x: app.change_light_assign()],
                            ['menu', lambda x: nav_drawer3.set_state('open')]
                            ]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: players_who_need_to_pay
                            spacing: '8dp'
                            padding: '8dp'
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint: (1, .1)
                        spacing: '8dp'
                        id: player_who_need_to_pay2
#Review Event Button START
            MDScreen:
                name: "ReviewPage"
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    MDTopAppBar:
                        title: "Review Event"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['home-export-outline', lambda x: app.change_to_event_home_screen()]]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: review_event
                            spacing: '8dp'
                            padding: '8dp'
                    MDRaisedButton:
                        text: "COMPLETE EVENT"
                        size_hint: (1, None)
                        on_press:
                            app.complete_event() 
                            
  
            MDScreen:
                name: "CompletedEventsPage"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Completed Events"
                        elevation: 2
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    Widget:
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: completed_md_list
                    MDRaisedButton:
                        text: "Raised Button"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)

                             
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'BAHimages/BAHlogo.jpeg'
                ScrollView:
                    MDList:
                        id: left_md_list
                        spacing: '8dp'
                        padding: '8dp'
                        MDRaisedButton:               
                            text: 'Create Event'
                            font_style: 'Subtitle1'
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            height: '75dp'
                            on_press:
                                print('Create Event Drawer Button was pressed')
                                app.add_quick_event_buttons(root)
                                root.ids.screen_manager.current = "CreateEventScreen"
                                nav_drawer.set_state('close')
                        MDFillRoundFlatButton:
                            text: 'Players'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('Create Player Drawer Button was pressed')
                                app.showLeftDrawerPlayersMenu = not app.showLeftDrawerPlayersMenu
                                app.showLeftDrawerPlayers(root)
                                
                        MDFillRoundFlatButton:
                            text: 'Manage Quick EVENTS'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                app.showManageQuickEvents = not app.showManageQuickEvents
                                print('Another Drawer Button was pressed')
                                #nav_drawer.set_state('close')
                                app.addManageQuickEvents(root)
                                #app.showLeftDrawerPlayersMenu = False
                                #root.ids.screen_manager.current = "CreateQuickEventScreen"
        MDNavigationDrawer:
            id: nav_drawer2
            anchor: 'right'
            ContentNavigationDrawer:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'BAHimages/BAHlogo.jpeg'
                ScrollView:
                    MDList:
                        id: right_md_list
                        spacing: '8dp'
                        padding: '8dp'
                        MDFillRoundFlatButton:
                            id: right_nav_event_button               
                            text: 'Events'
                            font_style: 'Subtitle1'
                            #rounded_button: 'True'
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            height: '75dp'
                            on_press:
                                print('Events RIGHT Drawer Button was pressed')
                                #root.ids.screen_manager.current = "CreateEventScreen"
                                #nav_drawer.set_state('close')
                                app.showRightDrawerEventsMenu = not app.showRightDrawerEventsMenu
                                app.showRightDrawerEvents(root)
                        MDRaisedButton:
                            text: 'Notifications'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('Notifications RIGHT Drawer Button was pressed')
                                app.change_to_notifications(root)
                                nav_drawer2.set_state('close')
                        # MDRaisedButton:
                        #     text: 'EVENT HOME'
                        #     font_style: 'Subtitle1'
                        #     size_hint_x: None
                        #     size_x: self.parent.width
                        #     pos_hint: {"center_x": .5}
                        #     size_hint: (1, None)
                        #     on_press:
                        #         print('Another RIGHT Drawer Button was pressed')      
                        #         nav_drawer2.set_state('close') 
                        #         app.back_to_current_event()
        MDNavigationDrawer:
            id: nav_drawer3
            anchor: 'right'
            ContentNavigationDrawer:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'BAHimages/BAHlogo.jpeg'
                ScrollView:
                    MDList:
                        id: nav_drawer3_md_list
                        spacing: '8dp'
                        padding: '8dp'
                        MDRaisedButton:
                            id: nav_drawer3_event_button               
                            text: 'Invite Players'
                            font_style: 'Subtitle1'
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            height: '75dp'
                            on_press:
                                print('Invite Players Drawer Button was pressed')
                                #nav_drawer3.set_state('close')
                                app.showSpecificEventDrawerPlayersMenu = not app.showSpecificEventDrawerPlayersMenu
                                app.showSpecificEventDrawerPlayersMenuModule(root)
                        MDRaisedButton:
                            text: 'Organize Attendees'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('Organize Attendees RIGHT Drawer Button was pressed')
                                root.ids.screen_manager.current = "OrganizeEventScreen"
                                nav_drawer3.set_state('close')
                                app.display_organize_event_screen()
                        MDRaisedButton:
                            text: 'EVENT HOME'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('Another RIGHT Drawer Button was pressed')      
                                nav_drawer3.set_state('close') 
                                root.ids.screen_manager.current = "SpecificEventPage"
                        MDRaisedButton:
                            text: 'PAYMENT'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('PAYMENT button was pressed from right nav_drawer3')      
                                nav_drawer3.set_state('close') 
                                app.load_paymentpage()
                                root.ids.screen_manager.current = "PaymentPage"
"""



class Tab(MDFloatLayout, MDTabsBase):
    # To implement content for a tab
    pass
    print("In the swipe to delete item card")

class SwipeToDeleteItem2(MDCardSwipe):
    text2 = StringProperty()
    second_text2 = StringProperty()
    third_text2 = StringProperty()
    event_id2 = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True

class CompletedEvents(MDCardSwipe):
    text2 = StringProperty()
    second_text2 = StringProperty()
    third_text2 = StringProperty()
    event_id2 = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True


class PlayerNotificationCard(MDCardSwipe):
    text2 = StringProperty()
    second_text2 = StringProperty()
    third_text2 = StringProperty()
    player_id = NumericProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True


class SwipeToDeletePlayerCard(MDCardSwipe):
    text3 = StringProperty()
    second_text3 = StringProperty()
    third_text3 = StringProperty()
    search_player_id = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True

class SwipeToAddSearchToEvent(MDCardSwipe):
    text3 = StringProperty()
    second_text3 = StringProperty()
    third_text3 = StringProperty()
    search_player_id = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True

class SwipeToAddPlayerToInList(MDCardSwipe):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    event_id = StringProperty()
    player_id = NumericProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True


class SwipeToRemovePlayerFromAllEmail(MDCardSwipe):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    event_id = StringProperty()
    player_id = NumericProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True



class SwipeToPayPlayer(MDCardSwipe):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    event_id = StringProperty()
    player_id = NumericProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True

class SwipeToPayPlayer2(MDCardSwipe):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    event_id = StringProperty()
    player_id = NumericProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True


class SwipeToRemoveRegularFromEmailList(MDCardSwipe):
    text = StringProperty()
    player_id = NumericProperty()
    player_email = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True

class SwipeToRemoveIndividualFromEmailList(MDCardSwipe):
    text = StringProperty()
    player_id = NumericProperty()
    player_email = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True

class SwipeToRemoveSubFromEmailList(MDCardSwipe):
    text = StringProperty()
    player_id = NumericProperty()
    player_email = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True

class TryingButtonDark(MDRaisedButton):
    text = StringProperty()
    player_id = NumericProperty()

class TryingButtonDark2(MDRaisedButton):
    text = StringProperty()
    player_id = NumericProperty()


class RegularAllEmail(MDRaisedButton):
    text = StringProperty()
    quick_event = StringProperty()
    size_hint = (1, None)

class SubstituteAllEmail(MDRaisedButton):
    text = StringProperty()
    quick_event = StringProperty()
    size_hint = (1, None)
class OpenAllEmail(MDRaisedButton):
    text = StringProperty()
    quick_event = StringProperty()
    size_hint = (1, None)

class QuickEventButtonLight(MDFillRoundFlatButton):
    text = StringProperty()
    event_id = StringProperty()

class QuickEventButtonDark(MDFillRoundFlatButton):
    text = StringProperty()
    event_id = StringProperty()

class QuickEventSubmitButton(MDFillRoundFlatButton):
    text = StringProperty()


class QuickEventTextField(MDTextField):
    id = StringProperty()

class TryingButtonLight(MDRaisedButton):
    text = StringProperty()
    player_id = NumericProperty()

class TryingButtonLight2(MDRaisedButton):
    text = StringProperty()
    player_id = NumericProperty()

class CreateEventScreen(MDScreen):
    pass

class CreateQuickEventScreen(MDScreen):
    pass

class LeftContainer(ILeftBodyTouch, MDBoxLayout):
    adaptive_width = True

class RightContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class OrganizePlayerToTeam(TwoLineListItem):
    text = StringProperty()
    second_text = StringProperty()
    #third_text = StringProperty()
    player_id = NumericProperty()
    adaptive_width = True

class OrganizeDark1Team(MDCardSwipe):
    text = StringProperty()
    player_id = NumericProperty()

class OrganizeDark2Team(MDCardSwipe):
    text = StringProperty()
    player_id = NumericProperty()

class OrganizeLight1Team(MDCardSwipe):
    text = StringProperty()
    player_id = NumericProperty()

class OrganizeLight2Team(MDCardSwipe):
    text = StringProperty()
    player_id = NumericProperty()

class OrganizeD1Line(OneLineAvatarIconListItem):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    player_id = NumericProperty()
class OrganizeD2Line(OneLineAvatarIconListItem):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    player_id = NumericProperty()

class OrganizeL1Line(OneLineAvatarIconListItem):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    player_id = NumericProperty()
class OrganizeL2Line(OneLineAvatarIconListItem):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    player_id = NumericProperty()

class CreatePlayerScreen(MDScreen):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    pass


class ScreenManager(ScreenManager):
    pass

class Tab(MDFloatLayout, MDTabsBase):
    content_text = StringProperty("")

sm = ScreenManager(transition=NoTransition())
sm.add_widget(CreateEventScreen(name="HomeScreen"))
sm.add_widget(CreateEventScreen(name="NotificationScreen"))
sm.add_widget(CreateEventScreen(name="CreateEventScreen"))
sm.add_widget(CreatePlayerScreen(name="CreatePlayerScreen"))
sm.add_widget(CreatePlayerScreen(name="CurrentEventsPage"))
sm.add_widget(CreatePlayerScreen(name="CompletedEventsPage"))
sm.add_widget(CreatePlayerScreen(name="SpecificEventPage"))
sm.add_widget(CreatePlayerScreen(name="SearchPlayerScreen"))
sm.add_widget(CreatePlayerScreen(name="SpecificFoundPlayerScreen"))
sm.add_widget(CreatePlayerScreen(name="InviteRegularsScreen"))
sm.add_widget(CreatePlayerScreen(name="OrganizeEventScreen"))
sm.add_widget(CreatePlayerScreen(name="AssignDark"))
sm.add_widget(CreatePlayerScreen(name="AssignLight"))
sm.add_widget(CreatePlayerScreen(name="SearchInviteIndividualPlayer"))
sm.add_widget(CreatePlayerScreen(name="FoundEventPlayerScreen"))
sm.add_widget(CreatePlayerScreen(name="FoundEventInvitePlayerScreen"))
sm.add_widget(CreatePlayerScreen(name="InviteIndividualsScreen"))
sm.add_widget(CreatePlayerScreen(name="CreatePlayerScreen"))
sm.add_widget(CreatePlayerScreen(name="DisplayTeams"))
sm.add_widget(CreatePlayerScreen(name="CreateQuickEventScreen"))
sm.add_widget(CreatePlayerScreen(name="EditQuickEventScreen"))
sm.add_widget(CreatePlayerScreen(name="PaymentPage"))
sm.add_widget(CreatePlayerScreen(name="ReviewPage"))
sm.add_widget(CreatePlayerScreen(name="InviteAllPLayersScreen"))



class DemoApp(MDApp):
    def __int__(self, **kwargs):
        super(DemoApp, self).__init__(**kwargs)
    showRightDrawerEventsMenu = BooleanProperty(False)
    showLeftDrawerPlayersMenu = BooleanProperty(False)
    showNavDrawer3BLANKMenu = BooleanProperty(False)
    showSpecificEventDrawerPlayersMenu = BooleanProperty(False)
    showSpecificPlayerPosition = BooleanProperty(False)
    showManageQuickEvents = BooleanProperty(False)
    print("this will be run at startup")
    TestingIndividualLogicCode.automatingdays.check_current_day_for_new_event()

    def send_final_email(self):
        print("in the send_final_email function")
        print("coming from the Display Teams page")
        print("nav upper right send email icon pressed")
        print(self.current_event_identify)
        with open('standardmessages.json') as allstandardmessages:
            all_standard_messages = json.load(allstandardmessages)
            self.txt = TestingIndividualLogicCode.makingtable.email_message_body(all_standard_messages
                ,self.dict_of_event, self.current_event_day)
        with open("ContactInfo.json") as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            self.players_assigned_to_teams, self.table_to_insert = TestingIndividualLogicCode.makingtable.email_players_and_table(
                all_contact_info, self.dict_of_event)
            self.txt = self.txt.replace("insert_table", self.table_to_insert)
            # this is just test sending COMPLETED email context to certain emails
            TestingIndividualLogicCode.alerts.email_alert_table("adamwilliams86@yahoo.com", "Test Email With Table"
                , self.txt)
            # above
        # need to move this "send email" alert into the for loop to hit all emails of players
        self.emails_players_assigned_to_teams = []
        with open("ContactInfo.json") as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            for a in self.players_assigned_to_teams:
                print(a)
                self.emails_players_assigned_to_teams.append(all_contact_info[a-1].get("Email"))
            print(self.emails_players_assigned_to_teams)
        # above
        self.back_to_current_event()

    def back_to_current_event(self):
        print("*" * 250)
        print("back_to_current_event")
        print("*" * 250)
        self.root.ids.currentevents_md_list.clear_widgets()
        self.clear_specific_event()
        labeltext = TestingIndividualLogicCode.makingtable.current_event_title_bar(self.dict_of_event)
        specific_event_heading_label = MDLabel(text=labeltext, halign='center')
        self.root.ids.specific_event_page_box_layout.add_widget(specific_event_heading_label)
        with open('ContactInfo.json') as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            for a in self.dict_of_event.get("PlayersInvited"):
                namestring, positionstring, player_id = TestingIndividualLogicCode.makingtable.organize_player_invited_player_card(all_contact_info, self.dict_of_event, a)
                player_card = SwipeToAddPlayerToInList(text=namestring,
                                                       second_text=positionstring,
                                                       event_id=self.current_event_identify,
                                                       player_id=player_id
                                                       )
                self.root.ids.specific_event_label.add_widget(player_card)
        self.root.ids.screen_manager.current = 'SpecificEventPage'


    def display_teams(self):
        print("now time to display teams")
        self.root.ids.screen_manager.current = 'DisplayTeams'
        dark = True
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            if len(all_current_events[self.current_event_identify]["Dark"]["Goalie"]) != 0:
                self.root.ids.display_dark.add_widget(OneLineListItem(text=f"Dk G: {len(all_current_events[self.current_event_identify]['Dark']['Goalie'])} / 1", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Goalie"]:
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeDark1Team(text=namestring,
                                                                 player_id=all_contact_info[single_player - 1].get(
                                                                     "playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeDark2Team(text=namestring,
                                                                 player_id=all_contact_info[single_player - 1].get(
                                                                     "playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Dark"]["Line1"]["Forward"]) != 0:
                self.root.ids.display_dark.add_widget(OneLineListItem(text=f"Dk L1 F: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Forward'])} / 3 ", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line1"]["Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeDark1Team(text=namestring,
                                                                 player_id=all_contact_info[single_player - 1].get(
                                                                     "playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeDark2Team(text=namestring,
                                                                 player_id=all_contact_info[single_player - 1].get(
                                                                     "playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Dark"]["Line1"]["Defense"]) != 0:
                self.root.ids.display_dark.add_widget(OneLineListItem(text=f"Dk L1 D: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Defense'])} / 2", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line1"]["Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeDark1Team(text=namestring,
                                                                 player_id=all_contact_info[
                                                                     single_player - 1].get("playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeDark2Team(text=namestring,
                                                                 player_id=all_contact_info[
                                                                     single_player - 1].get("playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark

            if len(all_current_events[self.current_event_identify]["Dark"]["Line2"]["Forward"]) != 0:
                self.root.ids.display_dark.add_widget(
                    OneLineListItem(text=f"Dk L2 F: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Forward'])} / 3 ", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line2"][
                    "Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeDark1Team(text=namestring,
                                                                 player_id=all_contact_info[
                                                                     single_player - 1].get("playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeDark2Team(text=namestring,
                                                                 player_id=all_contact_info[
                                                                     single_player - 1].get("playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Dark"]["Line2"]["Defense"]) != 0:
                self.root.ids.display_dark.add_widget(
                    OneLineListItem(text=f"Dk L2 D: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Defense'])} / 2", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line2"][
                    "Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeDark1Team(text=namestring,
                                                                 player_id=all_contact_info[
                                                                     single_player - 1].get("playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeDark2Team(text=namestring,
                                                                 player_id=all_contact_info[
                                                                     single_player - 1].get("playerid"))
                            self.root.ids.display_dark.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Light"]["Goalie"]) != 0:
                self.root.ids.display_light.add_widget(OneLineListItem(text=f"Lt G: {len(all_current_events[self.current_event_identify]['Light']['Goalie'])} / 1", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Goalie"]:
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeLight1Team(text=namestring, player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeLight2Team(text=namestring, player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Light"]["Line1"]["Forward"]) != 0:
                self.root.ids.display_light.add_widget(OneLineListItem(text=f"Lt L1 F: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Forward'])} / 3", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line1"]["Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeLight1Team(text=namestring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeLight2Team(text=namestring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Light"]["Line1"]["Defense"]) != 0:
                self.root.ids.display_light.add_widget(OneLineListItem(text=f"Lt L1 D: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Defense'])} / 2", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line1"]["Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeLight1Team(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeLight2Team(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark

            if len(all_current_events[self.current_event_identify]["Light"]["Line2"]["Forward"]) != 0:
                self.root.ids.display_light.add_widget(
                    OneLineListItem(text=f"Lt L2 F: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Forward'])} / 3", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line2"]["Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeLight1Team(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeLight2Team(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Light"]["Line2"]["Defense"]) != 0:
                self.root.ids.display_light.add_widget(
                    OneLineListItem(text=f"Lt L2 D: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Defense'])} / 2", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line2"][
                    "Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        if dark:
                            self.player_card = OrganizeLight1Team(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeLight2Team(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.display_light.add_widget(self.player_card)
                            dark = not dark


    def display_assigned_dark(self):
        print("now display_assigned_dark")
        self.root.ids.screen_manager.current = 'AssignDark'
        #self.root.ids.organize_dark_goalie.clear_widgets()
        self.root.ids.organize_dark_line1.clear_widgets()
        self.root.ids.organize_dark_line2.clear_widgets()
        #self.root.ids.organize_dark_line1.add_widget(MDLabel(text="Dark:", halign='center'))
        #self.root.ids.organize_dark_line2.add_widget(MDLabel(text="Dark Line 2:", halign='center'))
        dark = True
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            if len(all_current_events[self.current_event_identify]["Dark"]["Goalie"]) != 0:
                self.root.ids.organize_dark_line1.add_widget(OneLineListItem(text=f"Dark Goalie: {len(all_current_events[self.current_event_identify]['Dark']['Goalie'])} / 1 ", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Goalie"]:
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        #namestring = "Name: "
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        # namestring += " P: "
                        # namestring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        # namestring += " ~ L: "
                        # namestring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeD1Line(text=namestring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line1.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeD2Line(text=namestring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line1.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Dark"]["Line1"]["Forward"]) != 0:
                self.root.ids.organize_dark_line1.add_widget(OneLineListItem(text=f"Dark Line 1 Forwards: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Forward'])} / 3 ", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line1"]["Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        # namestring += " P:"
                        # namestring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        # namestring += " ~ L: "
                        # namestring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeD1Line(text=namestring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line1.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeD2Line(text=namestring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line1.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Dark"]["Line1"]["Defense"]) != 0:
                self.root.ids.organize_dark_line1.add_widget(OneLineListItem(text=f"Dark Line 1 Defense: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Defense'])} / 2 ", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line1"]["Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        # namestring += " P:"
                        # namestring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        # namestring += " ~ L: "
                        # namestring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeD1Line(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line1.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeD2Line(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line1.add_widget(self.player_card)
                            dark = not dark

            if len(all_current_events[self.current_event_identify]["Dark"]["Line2"]["Forward"]) != 0:
                self.root.ids.organize_dark_line2.add_widget(
                    OneLineListItem(text=f"Dark Line 2 Forwards: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Forward'])} / 3 ", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line2"][
                    "Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        # namestring += " P:"
                        # namestring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        # namestring += " ~ L: "
                        # namestring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeD1Line(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line2.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeD2Line(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line2.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Dark"]["Line2"]["Defense"]) != 0:
                self.root.ids.organize_dark_line2.add_widget(OneLineListItem(text=f"Dark Line 2 Defense: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Defense'])} / 2", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Dark"]["Line2"][
                    "Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        # namestring += " P:"
                        # namestring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        # namestring += " ~ L: "
                        # namestring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeD1Line(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line2.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeD2Line(text=namestring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_dark_line2.add_widget(self.player_card)
                            dark = not dark


    def change_light_assign(self):
        print("*" * 150 )
        print("now change_light_assign")
        self.root.ids.organize_light_line1.clear_widgets()
        self.root.ids.organize_light_line2.clear_widgets()
        #self.root.ids.organize_light_line1.add_widget(MDLabel(text="Light Line 1:", halign='center'))
        #self.root.ids.organize_light_line2.add_widget(MDLabel(text="Light Line 2:", halign='center'))
        self.root.ids.screen_manager.current = 'AssignLight'
        dark = True
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            if len(all_current_events[self.current_event_identify]["Light"]["Goalie"]) != 0:
                self.root.ids.organize_light_line1.add_widget(OneLineListItem(text=f"Light Goalie: {len(all_current_events[self.current_event_identify]['Light']['Goalie'])} / 1", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Goalie"]:
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = ""
                        namestring += f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        positionstring = "Pos: "
                        positionstring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        positionstring += "  Line: "
                        positionstring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeL1Line(#font_style= 'Body2',
                                                                          text=namestring, second_text=positionstring, player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line1.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeL2Line(#font_style= 'Body2',
                                text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line1.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Light"]["Line1"]["Forward"]) != 0:
                self.root.ids.organize_light_line1.add_widget(OneLineListItem(text=f"Light Line 1 Forwards: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Forward'])} / 3", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line1"]["Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = ""
                        namestring += f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        positionstring = "Pos: "
                        positionstring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        positionstring += "  Line: "
                        positionstring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeL1Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line1.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeL2Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line1.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Light"]["Line1"]["Defense"]) != 0:
                self.root.ids.organize_light_line1.add_widget(OneLineListItem(text=f"Light Line 1 Defense: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Defense'])} / 2", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line1"]["Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = ""
                        namestring += f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        positionstring = "Pos: "
                        positionstring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        positionstring += "  Line: "
                        positionstring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeL1Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line1.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeL2Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line1.add_widget(self.player_card)
                            dark = not dark

            if len(all_current_events[self.current_event_identify]["Light"]["Line2"]["Forward"]) != 0:
                self.root.ids.organize_light_line2.add_widget(
                    OneLineListItem(text=f"Light Line 2 Forwards: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Forward'])} / 3", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line2"][
                    "Forward"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = ""
                        namestring += f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        positionstring = "Pos: "
                        positionstring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        positionstring += "  Line: "
                        positionstring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeL1Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line2.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeL2Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line2.add_widget(self.player_card)
                            dark = not dark
            if len(all_current_events[self.current_event_identify]["Light"]["Line2"]["Defense"]) != 0:
                self.root.ids.organize_light_line2.add_widget(
                    OneLineListItem(text=f"Light Line 2 Defense: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Defense'])} / 2 ", bg_color=(0,0,0,.15)))
                for single_player in all_current_events[self.current_event_identify]["Light"]["Line2"][
                    "Defense"]:
                    print(single_player)
                    with open('ContactInfo.json') as allcontactinfo:
                        all_contact_info = json.load(allcontactinfo)
                        namestring = ""
                        namestring += f"{all_contact_info[single_player - 1].get('Player First')}"
                        namestring += " " + f"{all_contact_info[single_player - 1].get('Player Last')}"
                        positionstring = "Pos: "
                        positionstring += f'{all_contact_info[single_player - 1].get("position F D G")}'
                        positionstring += "  Line: "
                        positionstring += f'{all_contact_info[single_player - 1].get("LINE")}'
                        if dark:
                            self.player_card = OrganizeL1Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line2.add_widget(self.player_card)
                            dark = not dark
                        else:
                            self.player_card = OrganizeL2Line(text=namestring, second_text=positionstring,
                                                              player_id=all_contact_info[
                                                                  single_player - 1].get("playerid"))
                            self.root.ids.organize_light_line2.add_widget(self.player_card)
                            dark = not dark


    def change_home_screen(self):
        print("change_home_screen module")
        self.root.ids.screen_manager.current = 'HomeScreen'
        self.root.ids.search_fields.clear_widgets()
        self.root.ids.create_player_fields.clear_widgets()

    def showSpecificEventDrawerPlayersMenuModule(self, root):
        print("*")
        print("showSpecificEventDrawerPlayersMenuModule")
        print("*" * 250)
        if self.showSpecificEventDrawerPlayersMenu:
            self.invite = MDRaisedButton(font_style = 'Subtitle2', text='Invite Regulars', on_press= self.inviteregularsbutton, size_hint = (1, None), padding = '10dp',   anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.nav_drawer3_md_list.add_widget(self.invite, 3)
            self.invite2 = MDRaisedButton(font_style = 'Subtitle2', text='Invite Subs', on_press= self.invitesubsbutton, size_hint = (1, None), padding = '10dp',  anchor_x = 'left', md_bg_color = (.2,.53,.733,1))
            root.ids.nav_drawer3_md_list.add_widget(self.invite2, 3)
            self.invite3 = MDRaisedButton(font_style = 'Subtitle2', text='Invite Individual Player', on_press= self.inviteindividualplayer, size_hint = (1, None), padding = '10dp',  anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.nav_drawer3_md_list.add_widget(self.invite3, 3)
            self.invite4 = MDRaisedButton(font_style='Subtitle2', text='Invite ALL Players',
                                          on_press=self.inviteallplayers, size_hint=(1, None), padding='10dp',
                                          anchor_x='left', md_bg_color=(.2,.53,.733,1))
            root.ids.nav_drawer3_md_list.add_widget(self.invite4, 3)

            self.secondchild = root.ids.nav_drawer3_md_list.children
        else:
            print(" we are in the showSpecificEventDrawerPlayersMenuModule(self, root): and removing the widgets")
            root.ids.nav_drawer3_md_list.remove_widget(self.invite)
            root.ids.nav_drawer3_md_list.remove_widget(self.invite2)
            root.ids.nav_drawer3_md_list.remove_widget(self.invite3)
            root.ids.nav_drawer3_md_list.remove_widget(self.invite4)



    def display_organize_event_screen(self):
        print("*" * 250)
        print("display_organize_event_screen")
        print("time to display the organize event information")
        self.root.ids.organize_event_page_box_layout.clear_widgets()
        self.root.ids.organize_event_label.clear_widgets()

        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            labeltext = TestingIndividualLogicCode.makingtable.organize_attendee_title_bar(self.dict_of_event)
            specific_event_heading_label = MDLabel(text=labeltext, halign='center')
            self.root.ids.organize_event_page_box_layout.add_widget(specific_event_heading_label)
            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                for a in all_current_events[self.current_event_identify].get("PlayersIn"):
                    name, positionstring, randomtext = TestingIndividualLogicCode.makingtable.organize_attendee_player_card(all_current_events,all_contact_info, self.current_event_identify,a)
                    self.player_card = OrganizePlayerToTeam(text=name, second_text=positionstring, player_id=a)
                    self.root.ids.organize_event_label.add_widget(self.player_card)

    def add_under_player_card(self, instance):
        print("*" * 250)
        print("in add_under_player_card module")
        print(self.root.ids.organize_event_label)
        print(self.root.ids.organize_event_label.children)
        print("CHILDREN")
        parent = self.root.ids.organize_event_label
        children = self.root.ids.organize_event_label.children
        print(self.showSpecificPlayerPosition)
        if self.showSpecificPlayerPosition:
            for item in children:
                print(item)
                print("JUST PRINTED ITEM")
                if isinstance(item, TryingButtonDark):
                    print("YES DARK Items")
                    self.display_organize_event_screen()
                if isinstance(item, TryingButtonLight):
                    print("YES LIGHT Items")
                    parent.remove_widget(item)
                    self.display_organize_event_screen()
        else:
            print(self.root.ids.organize_event_label.children.index(instance))
            print("CHILDREN INSTANCE")
            self.button_index = self.root.ids.organize_event_label.children.index(instance)
            print(instance.player_id)

            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                player_id = int(instance.player_id)
                print(player_id)
                print("PLAYER ID")
                if "G" in all_contact_info[instance.player_id - 1].get("position F D G"):
                    print("GOALIE")
                    self.dark_goalie = TryingButtonDark(font_style = "Subtitle2", text="Dark Goalie",
                                                    player_id=instance.player_id,
                                                    on_press= self.add_goalie_dark)#TRYING TO ADD instance.player_id
                    print(type(self.dark_goalie))
                    self.root.ids.organize_event_label.add_widget(self.dark_goalie, self.button_index)
                    self.light_goalie = TryingButtonLight(font_style="Subtitle2", text="Light Goalie",
                                                    player_id=instance.player_id,
                                                    on_press=self.add_goalie_light)  # TRYING TO ADD instance.player_id
                    print(type(self.light_goalie))
                    self.root.ids.organize_event_label.add_widget(self.light_goalie, self.button_index)
                if "1" in all_contact_info[instance.player_id - 1].get("LINE"):
                    print("ONLY LINE 1")
                    if "F" in all_contact_info[instance.player_id - 1].get("position F D G"):
                        print("Forward Line 1")
                        self.dark_forward_line_1 = TryingButtonDark(font_style="Subtitle2", text="Dark Line1 Forward",
                                                                player_id = instance.player_id,
                                                                on_press=self.add_dark_forward_line_1)#TRYING TO ADD instance.player_id
                        self.root.ids.organize_event_label.add_widget(self.dark_forward_line_1, self.button_index)
                        self.light_forward_line_1 = TryingButtonLight(font_style="Subtitle2", text="Light Line1 Forward",
                                                                player_id = instance.player_id,
                                                                on_press=self.add_light_forward_line_1)
                        self.root.ids.organize_event_label.add_widget(self.light_forward_line_1, self.button_index)
                    if "D" in all_contact_info[instance.player_id - 1].get("position F D G"):
                        print("Defense Line 1")
                        self.dark_defense_line_1 = TryingButtonDark(font_style="Subtitle2", text="Dark Line1 Defense",
                                                                player_id=instance.player_id,
                                                                on_press=self.add_dark_defense_line_1)  # TRYING TO ADD instance.player_id
                        self.root.ids.organize_event_label.add_widget(self.dark_defense_line_1, self.button_index)
                        self.light_defense_line_1 = TryingButtonLight(font_style="Subtitle2", text="Light Line1 Defense",
                                                                 player_id=instance.player_id,
                                                                 on_press=self.add_light_defense_line_1)
                        self.root.ids.organize_event_label.add_widget(self.light_defense_line_1, self.button_index)
                if "2" in all_contact_info[instance.player_id - 1].get("LINE"):
                    print("ONLY LINE 2")
                    if "F" in all_contact_info[instance.player_id - 1].get("position F D G"):
                        print("FORWARD LINE 2")
                        self.dark_forward_line_2 = TryingButtonDark2(font_style="Subtitle2", text="Dark Line2 Forward",
                                                                player_id = instance.player_id,
                                                                on_press=self.add_dark_forward_line_2)#TRYING TO ADD instance.player_id
                        self.root.ids.organize_event_label.add_widget(self.dark_forward_line_2, self.button_index)
                        self.light_forward_line_2 = TryingButtonLight2(font_style="Subtitle2", text="Light Line2 Forward",
                                                                player_id = instance.player_id,
                                                                on_press=self.add_light_forward_line_2)
                        self.root.ids.organize_event_label.add_widget(self.light_forward_line_2, self.button_index)
                    if "D" in all_contact_info[instance.player_id - 1].get("position F D G"):
                        print("Defense Line 2")
                        self.dark_defense_line_2 = TryingButtonDark2(font_style="Subtitle2", text="Dark Line2 Defense",
                                                                player_id=instance.player_id,
                                                                on_press=self.add_dark_defense_line_2)  # TRYING TO ADD instance.player_id
                        self.root.ids.organize_event_label.add_widget(self.dark_defense_line_2, self.button_index)
                        self.light_defense_line_2 = TryingButtonLight2(font_style="Subtitle2", text="Light Line2 Defense",
                                                                 player_id=instance.player_id,
                                                                 on_press=self.add_light_defense_line_2)
                        self.root.ids.organize_event_label.add_widget(self.light_defense_line_2, self.button_index)
        print(self.root.ids.organize_event_label.children)
        print("CHILDREN AGAIN")
        #print(self.root.ids.organize_event_label.children.index(instance))
        print("CHILDREN INSTANCE AGAIN")
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition

    def add_goalie_dark(self, instance):
        print("ADD GOALIE TO DARK")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Dark"]["Goalie"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_goalie_light(self, instance):
        print("ADD GOALIE TO LIGHT")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Light"]["Goalie"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_dark_forward_line_1(self, instance):
        print("add_dark_forward_line_1")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Dark"]["Line1"]["Forward"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_dark_forward_line_2(self, instance):
        print("add_dark_forward_line_2")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Dark"]["Line2"]["Forward"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_light_forward_line_1(self, instance):
        print("add_light_forward_line_1")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Light"]["Line1"]["Forward"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_light_forward_line_2(self, instance):
        print("add_light_forward_line_2")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Light"]["Line2"]["Forward"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_dark_defense_line_1(self, instance):
        print("add_dark_defense_line_1")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Dark"]["Line1"]["Defense"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_dark_defense_line_2(self, instance):
        print("add_dark_defense_line_2")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Dark"]["Line2"]["Defense"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_light_defense_line_1(self, instance):
        print("add_light_defense_line_1")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Light"]["Line1"]["Defense"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()
    def add_light_defense_line_2(self, instance):
        print("add_light_defense_line_2")
        print(instance.player_id)
        self.showSpecificPlayerPosition = not self.showSpecificPlayerPosition
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
            all_current_events[self.current_event_identify]["Light"]["Line2"]["Defense"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
            self.dict_of_event = all_current_events[self.current_event_identify]
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        self.display_organize_event_screen()


    def inviteindividualplayer(self, root):
        print("*" * 250)
        print(" in the inviteindividualplayer(self, root) functin")
        print("*" * 250)
        self.showSpecificEventDrawerPlayersMenu = not self.showSpecificEventDrawerPlayersMenu
        self.root.ids.nav_drawer3.set_state('close')
        TestingIndividualLogicCode.testingfunctions.remove_nav_drawer_3_widgets(self)
        self.root.ids.screen_manager.current = 'SearchInviteIndividualPlayer'
        for md_text_field in self.root.ids.search_fields2.children:
            md_text_field.text =""


    def invitesearchplayers(self):
        self.ids_of_new_individual_invites = []
        print("INVITE searchplayers MODULE")
        searchplayerlist = ["Player First", "Player Last", "Cell Number", "Email", "position F D G", "LINE"]
        print("start criteria seach and display player cards")
        textfields = [md_text_field.text for md_text_field in self.root.ids.search_fields2.children]
        print(textfields)
        searchdictionary = dict(zip(searchplayerlist, reversed(textfields)))
        print(searchdictionary)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ just printed searchdictionary")
        with open('ContactInfo.json') as contactinfo:
            allcontactinfo = json.load(contactinfo)
            print(allcontactinfo)
            for singlekey in searchdictionary:
                for singlecontact in allcontactinfo:
                    if singlekey != "position F D G" and singlecontact.get(singlekey) != "" and singlecontact.get(
                            singlekey) == searchdictionary.get(singlekey):
                        # singlecontact.get(singlekey).find(searchdictionary.get(singlekey)) != -1:
                        print("EVENT INVITE IM IN HERE")
                        playerfirst = singlecontact['Player First']
                        playerlast = singlecontact['Player Last']
                        playercell = singlecontact['Cell Number']
                        playeremail = singlecontact['Email']
                        searchhit = singlecontact[str(singlekey)]
                        player_card = SwipeToAddSearchToEvent(text3=f'SEARCH: {searchhit}',
                                                              second_text3=f'{playerfirst} {playerlast}',
                                                              third_text3=f'{playercell} {playeremail}',
                                                              search_player_id=str(singlecontact['playerid'])
                                                              )
                        self.root.ids.found_event_player_md_list.add_widget(player_card)
                    # print(singlecontact.get(singlekey))
                    # print("just printed the singlecontact.get(singlekey))")
                    if singlekey == "position F D G" and searchdictionary.get(singlekey) != "":
                        a = singlecontact.get(singlekey).find(searchdictionary.get(singlekey))
                        if a != -1:
                            print(a)
                            print("Made it into here")
                            playerfirst = singlecontact['Player First']
                            playerlast = singlecontact['Player Last']
                            playercell = singlecontact['Cell Number']
                            playeremail = singlecontact['Email']
                            searchhit = singlecontact[str(singlekey)]
                            player_card = SwipeToAddSearchToEvent(text3=f'SEARCH: {searchhit}',
                                                                  second_text3=f'{playerfirst} {playerlast}',
                                                                  third_text3=f'{playercell} {playeremail}',
                                                                  search_player_id=str(singlecontact['playerid']),
                                                                  )
                            self.root.ids.found_event_player_md_list.add_widget(player_card)

        self.root.ids.screen_manager.current = 'FoundEventInvitePlayerScreen'

    def inviteallplayers(self, root):
        print("---  in the inviteallplayers Module  ---")
        self.showSpecificEventDrawerPlayersMenu = not self.showSpecificEventDrawerPlayersMenu
        self.root.ids.nav_drawer3.set_state('close')
        self.root.ids.list_of_regulars_display.clear_widgets()
        self.root.ids.email_all_players.clear_widgets()
        self.root.ids.all_players_getting_email.clear_widgets()

        TestingIndividualLogicCode.testingfunctions.remove_nav_drawer_3_widgets(self)
        self.current_event_players_invited_list_ids = []
        self.ids_of_new_invites = []
        self.email_new_invites = []
        dark = True
        labeltext = TestingIndividualLogicCode.makingtable.current_event_title_bar(self.dict_of_event)
        self.root.ids.email_all_players.add_widget(
            OneLineListItem(text=labeltext,
                            bg_color=(0, 0, 0, .15)))
        email_types = ["Regulars", "Substitute", "Open"]
        with open('standardmessages.json') as allstandardmessages:
            all_standard_messages = json.load(allstandardmessages)
            print("*" * 300)
            print(self.current_event_day)
            specific_message = 'Reg'
            txt = str(all_standard_messages[specific_message])
            txt = TestingIndividualLogicCode.testingfunctions.replace_email_message(self, self.dict_of_event, txt)
            print(txt)
            print("*" * 300)
            # specific_message = all_standard_messages.get(specific_message)
            self.root.ids.all_players_quick_event_text.text = txt
        with open('quickevents.json') as f:
            quick_events = json.load(f)
            for key in quick_events.keys():
                print(key)
                for type in email_types:
                    title = str(type + " " + key)
                    if type == "Regulars":
                        self.root.ids.email_all_players.add_widget(RegularAllEmail(text=title, quick_event= title, on_press= self.findplayersinquickevent, size_hint=(1,None)))
                    if type == "Substitute":
                        self.root.ids.email_all_players.add_widget(SubstituteAllEmail(text=title, quick_event=title, on_press= self.findplayersinquickevent, size_hint=(1,None)))
                    if type == "Open":
                        self.root.ids.email_all_players.add_widget(
                            OpenAllEmail(text=title, quick_event=title, on_press=self.findplayersinquickevent, size_hint=(1,None)))
        self.root.ids.screen_manager.current = 'InviteAllPLayersScreen'

    def findplayersinquickevent(self, instance):
        print("---   findplayersinquickevent   function   ---")
        print(instance.quick_event)
        self.root.ids.all_players_getting_email.clear_widgets()
        self.root.ids.all_players_getting_email.clear_widgets()
        x = instance.quick_event.index(" ")
        key = instance.quick_event[x+1:]
        playercard = []
        print(playercard)
        self.current_event_players_invited_list_ids = TestingIndividualLogicCode.testingfunctions.show_all_players(self,
                                                                                                               self.dict_of_event)
        print(self.current_event_players_invited_list_ids)
        print(self.ids_of_new_invites)
        print("^"*250)
        with open("ContactInfo.json") as file:
            all_contacts = json.load(file)
            for single_contact in all_contacts:
                #print(single_contact)
                # text = instance.quick_event.rfind("Regulars")
                #print(text)
                if instance.quick_event.rfind("Regulars") == 0 and single_contact[key] == "R":
                    print("Made it into the regulars")
                    self.ids_of_new_invites.append(single_contact["playerid"])
                    #text = instance.quick_event.rfind("Regulars")
                if instance.quick_event.rfind("Substitute") == 0 and single_contact[key] == "S":
                    print("Made it into the Substitute")
                    self.ids_of_new_invites.append(single_contact["playerid"])
                    #text = instance.quick_event.rfind("Substitute")
                if instance.quick_event.rfind("Open") == 0 and single_contact[key] == "":
                    print("Made it into the Open")
                    self.ids_of_new_invites.append(single_contact["playerid"])
                    #text = instance.quick_event.rfind("Open")
            for new_invite in self.ids_of_new_invites:
                if new_invite not in self.current_event_players_invited_list_ids:
                    print("We need to invite this player")
                    print("+"*100)
                    #print(all_contacts[new_invite]["Email"])
                    self.email_new_invites.append(all_contacts[new_invite-1]["Email"])
                    print(self.email_new_invites)
                    playercard.append(new_invite)
                else:
                    print("Player is already invited")
                    print("-"*100)
            for a in playercard:
                namestring, positionstring, player_id = TestingIndividualLogicCode.makingtable.organize_player_invited_player_card(all_contacts, self.dict_of_event, int(a))
                player_card = SwipeToRemovePlayerFromAllEmail(text=namestring,
                                                       second_text=positionstring,
                                                       event_id=self.current_event_identify,
                                                       player_id=player_id
                                                       )
                self.root.ids.all_players_getting_email.add_widget(player_card)
        print(self.email_new_invites)


    def remove_player_from_all_email_list(self, instance):
        print("---   SwipeToRemovePlayerFromAllEmail just swiped")
        print("remove_player_from_all_email_list Function   ---")
        self.root.ids.all_players_getting_email.remove_widget(instance)
        #need to delete player id from this list
        #self.ids_of_new_invites
        print(self.ids_of_new_invites)
        self.ids_of_new_invites.remove(instance.player_id)
        print(self.ids_of_new_invites)


    def inviteregularsbutton(self, root):
#        self.root.ids.list_of_regulars_display.remove_widget(regular_player_card)
        self.showSpecificEventDrawerPlayersMenu = not self.showSpecificEventDrawerPlayersMenu
        self.root.ids.nav_drawer3.set_state('close')
        self.root.ids.list_of_regulars_display.clear_widgets()
        TestingIndividualLogicCode.testingfunctions.remove_nav_drawer_3_widgets(self)
        print("inviteregularsbutton MODULE")
        self.current_event_regular_list = []
        self.ids_of_new_invites = []
        with open('standardmessages.json') as allstandardmessages:
            all_standard_messages = json.load(allstandardmessages)
            print("*" * 300)
            print(self.current_event_day)
            specific_message = 'Reg'
            txt = str(all_standard_messages[specific_message])
            txt = TestingIndividualLogicCode.testingfunctions.replace_email_message(self, self.dict_of_event, txt)
            print(txt)
            print("*"*300)
            # specific_message = all_standard_messages.get(specific_message)
            self.root.ids.quick_event_text.text = txt
        with open('ContactInfo.json') as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            for a in all_contact_info:
                print("%"*250)
                if not(TestingIndividualLogicCode.testingfunctions.check_if_player_invited(self, self.dict_of_event, a["playerid"])) and a[self.current_event_title] == 'Z':
                    print("999"*100)
                    print("Need to add to email")
                    self.current_event_regular_list.append(a["Email"])
                    self.ids_of_new_invites.append(a["playerid"])
                    print("ALL TO LIST")
                    #namestring = a["Player First"] + " " + a["Player Last"]
                    regular_player_card = SwipeToRemoveRegularFromEmailList(text=a["Player First"] + " " +\
                                                                                     a["Player Last"],
                                                                                player_id = a["playerid"],
                                                                                player_email = a["Email"])
                    self.root.ids.list_of_regulars_display.add_widget(regular_player_card, 2)
        self.root.ids.screen_manager.current = 'InviteRegularsScreen'
        print("Need to send email and text notification and add to INVITED list")
    def invitesubsbutton(self, root):
        self.showSpecificEventDrawerPlayersMenu = not self.showSpecificEventDrawerPlayersMenu
        self.root.ids.nav_drawer3.set_state('close')
        self.root.ids.list_of_subs_display.clear_widgets()
        TestingIndividualLogicCode.testingfunctions.remove_nav_drawer_3_widgets(self)
        print("invitesubsbutton MODULE")
        self.current_event_sub_list = []
        self.ids_of_new_sub_invites = []
        with open('standardmessages.json') as allstandardmessages:
            all_standard_messages = json.load(allstandardmessages)
            specific_message = f'Sub'
            print(specific_message)
            txt = str(all_standard_messages[specific_message])
            txt = TestingIndividualLogicCode.testingfunctions.replace_email_message(self, self.dict_of_event, txt)
            print(txt)
            #print(all_standard_messages[0].get(specific_message))
            print("Printing Specific Message")
            # specific_message = all_standard_messages.get(specific_message)
            self.root.ids.quick_event2_text.text = txt
        with open('ContactInfo.json') as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            for a in all_contact_info:
                #print(a)
                if a["playerid"] in self.current_event_players_invited:
                    print("already invited")
                else:
                    if a[self.current_event_title] == 'Z':
                        self.current_event_sub_list.append(a["Email"])
                        self.ids_of_new_sub_invites.append(a["playerid"])
                        print("ALL TO LIST")
                        print(a)
                        #namestring = a["Player First"] + " " + a["Player Last"]
                        regular_player_card = SwipeToRemoveSubFromEmailList(text=a["Player First"] + " " +\
                                                                                     a["Player Last"],
                                                                                player_id = a["playerid"],
                                                                                player_email = a["Email"])
                        self.root.ids.list_of_subs_display.add_widget(regular_player_card, 2)
        self.root.ids.screen_manager.current = 'InviteSubsScreen'
        print("Need to send email and text notification and add to INVITED list")

    def allplayersinviteemail(self):
        print("---   in the allplayersinviteemail FUNCTION   ---")
        self.root.ids.email_all_players.clear_widgets()
        self.root.ids.all_players_getting_email.clear_widgets()
        print("NEED TO EMAIL THESE PLAYERS")
        print(self.email_new_invites)
        print("This Email Text")
        print(self.root.ids.all_players_quick_event_text.text)
        for singleplayer in self.email_new_invites:
            TestingIndividualLogicCode.alerts.email_alert(singleplayer, "BAH TUESDAY HOCKEY",
                                                      self.root.ids.all_players_quick_event_text.text)
        self.back_to_current_event()
        with open("myevents.json") as f:
            all_events = json.load(f)
            this_event = all_events[self.current_event_identify]
            print(this_event)
            for single_player_id in self.ids_of_new_invites:
                if single_player_id not in this_event["PlayersInvited"]:
                    this_event["PlayersInvited"].append(single_player_id)
            with open('myevents.json', 'w') as file:
                json.dump(all_events, file, indent=4, separators=(',', ':'))
        TestingIndividualLogicCode.testingfunctions.display_selected_event(self, self.current_event_identify, MDLabel,
                                                                           SwipeToAddPlayerToInList)

        #ALSO NEED TO ALLOW CHAD TO "MASS MAKE REGULARS / SUBS" AFTER COMPLETING AN EVENT IF WANTED
        #NEED TO ACTUALLY SEND THE EMAIL

    def remove_all_from_email_list(self, instance):
        # need to remove the regular from the email list
        print("just swiped remove_all_from_email_list")
        for a in self.ids_of_new_invites:
            print(a)
            if instance.player_id == a:
                self.ids_of_new_invites.remove(a)
        for a in self.current_event_regular_list:
            print(a)
            if instance.player_email == a:
                self.current_event_regular_list.remove(a)
        print(self.ids_of_new_invites)
        print(self.current_event_regular_list)


    def inviteregularssendemail(self):
        print("***   in the inviteregularssendemail MODULE   ***")
        self.root.ids.specific_event_label.clear_widgets()
        print("time to send the emails")
        print(self.current_event_regular_list)
        print("Just printed the self.current_event_regular_list WHICH IS EMAILS")
        with open("ContactInfo.json") as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            with open('myevents.json') as allcurrentevents:
                all_current_events = json.load(allcurrentevents)
                for a in self.ids_of_new_invites:
                    self.email_dict_of_player = all_contact_info[a-1]
                    print(self.email_dict_of_player)
                    if not (TestingIndividualLogicCode.testingfunctions.check_if_player_invited(self,
                                                                                                all_current_events[
                                                                                                    self.current_event_identify],
                                                                                                a)):
                        all_current_events[self.current_event_identify].get("PlayersInvited").append(a)
                        TestingIndividualLogicCode.alerts.email_alert(self.email_dict_of_player.get("Email"), "Test Email",
                                                                      self.root.ids.quick_event_text.text)
                        with open('myevents.json', 'w') as json_file:
                            json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                            print("Just dumped the info")
                            print(all_current_events[self.current_event_identify]["PlayersInvited"])
                    else:
                        print("Player Already Invited")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            # just added
            self.dict_of_event = all_current_events[self.current_event_identify]
            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                for a in all_current_events[self.current_event_identify]["PlayersInvited"]:
                    print('adding players to screen')
                    print(all_contact_info[a - 1])
                    namestring = "Name: "
                    namestring += f"{all_contact_info[a - 1].get('Player First')}"
                    namestring += " " + f"{all_contact_info[a - 1].get('Player Last')}"
                    positionstring = "Pos: "
                    positionstring += f'{all_contact_info[a - 1].get("position F D G")}'
                    positionstring += "  Line: "
                    positionstring += f'{all_contact_info[a - 1].get("LINE")}'
                    player_id = int(all_contact_info[a - 1].get("playerid"))
                    print(namestring)
                    player_card = SwipeToAddPlayerToInList(text=namestring,
                                                           second_text=positionstring,
                                                           event_id=self.current_event_identify,
                                                           player_id=player_id
                                                           )
                    self.root.ids.specific_event_label.add_widget(player_card)
        self.root.ids.screen_manager.current = 'SpecificEventPage'

    def invitesubssendemail(self):
        print("***   in the invitesubssendemail MODULE   ***")
        self.root.ids.specific_event_label.clear_widgets()
        print("time to send SUBS emails")
        print(self.current_event_sub_list)
        print("Just printed the self.current_event_SUB_list WHICH IS EMAILS")
        with open("ContactInfo.json") as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            with open('myevents.json') as allcurrentevents:
                all_current_events = json.load(allcurrentevents)
                for a in self.ids_of_new_sub_invites:
                    self.email_dict_of_player = all_contact_info[a-1]
                    print(self.email_dict_of_player)
                    if not (TestingIndividualLogicCode.testingfunctions.check_if_player_invited(self,
                                                                                                all_current_events[
                                                                                                    self.current_event_identify],
                                                                                                a)):
                        all_current_events[self.current_event_identify].get("PlayersInvited").append(a)
                        TestingIndividualLogicCode.alerts.email_alert(self.email_dict_of_player.get("Email"), "Test Email",
                                                                      self.root.ids.quick_event_text.text)
                        with open('myevents.json', 'w') as json_file:
                            json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                            print("Just dumped the info")
                            print(all_current_events[self.current_event_identify]["PlayersInvited"])
                    else:
                        print("Player Already Invited")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            # just added
            self.dict_of_event = all_current_events[self.current_event_identify]
            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                for a in all_current_events[self.current_event_identify]["PlayersInvited"]:
                    print('adding players to screen')
                    print(all_contact_info[a - 1])
                    namestring = "Name: "
                    namestring += f"{all_contact_info[a - 1].get('Player First')}"
                    namestring += " " + f"{all_contact_info[a - 1].get('Player Last')}"
                    positionstring = "Pos: "
                    positionstring += f'{all_contact_info[a - 1].get("position F D G")}'
                    positionstring += "  Line: "
                    positionstring += f'{all_contact_info[a - 1].get("LINE")}'
                    player_id = int(all_contact_info[a - 1].get("playerid"))
                    print(namestring)
                    player_card = SwipeToAddPlayerToInList(text=namestring,
                                                           second_text=positionstring,
                                                           event_id=self.current_event_identify,
                                                           player_id=player_id
                                                           )
                    self.root.ids.specific_event_label.add_widget(player_card)
        self.root.ids.screen_manager.current = 'SpecificEventPage'

    def invitefoundplayerssendemail(self):
        print("in the invite found players send email")
        self.root.ids.specific_event_label.clear_widgets()
        print("time to send the emails")
        with open("ContactInfo.json") as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            with open('myevents.json') as allcurrentevents:
                all_current_events = json.load(allcurrentevents)
                for a in self.ids_of_new_individual_invites:
                    self.email_dict_of_player = all_contact_info[a - 1]
                    print(self.email_dict_of_player)
                    if not(TestingIndividualLogicCode.testingfunctions.check_if_player_invited(self, all_current_events[self.current_event_identify], a)):
                        print("WE ARE UNDER THE IF NOT IN THE MAIN APP")
                        all_current_events[self.current_event_identify].get("PlayersInvited").append(a)
                        print(self.email_dict_of_player.get("Email"))
                        TestingIndividualLogicCode.alerts.email_alert(self.email_dict_of_player.get("Email"),
                                                                     "Test Email",
                                                                      self.root.ids.quick3_event_text.text)
                        with open('myevents.json', 'w') as json_file:
                            json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                            print("Just dumped the info")
                            print(all_current_events[self.current_event_identify]["PlayersInvited"])
                    else:
                        print("Player Already Invited")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            # just added
            self.dict_of_event = all_current_events[self.current_event_identify]
            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                for a in all_current_events[self.current_event_identify]["PlayersInvited"]:
                    print('adding players to screen')
                    print(all_contact_info[a - 1])
                    namestring = "Name: "
                    namestring += f"{all_contact_info[a - 1].get('Player First')}"
                    namestring += " " + f"{all_contact_info[a - 1].get('Player Last')}"
                    positionstring = "Pos: "
                    positionstring += f'{all_contact_info[a - 1].get("position F D G")}'
                    positionstring += "  Line: "
                    positionstring += f'{all_contact_info[a - 1].get("LINE")}'
                    player_id = int(all_contact_info[a - 1].get("playerid"))
                    print(namestring)
                    player_card = SwipeToAddPlayerToInList(text=namestring,
                                                           second_text=positionstring,
                                                           event_id=self.current_event_identify,
                                                           player_id=player_id
                                                           )
                    self.root.ids.specific_event_label.add_widget(player_card)
        self.root.ids.screen_manager.current = 'SpecificEventPage'


    def remove_regular_from_email_list(self, root):
        # need to remove the regular from the email list
        print("just swiped SwipeToRemoveRegularFromEmailList")
        for a in self.ids_of_new_invites:
            print(a)
            if root.player_id == a:
                self.ids_of_new_invites.remove(a)
        for a in self.current_event_regular_list:
            print(a)
            if root.player_email == a:
                self.current_event_regular_list.remove(a)
        print(self.ids_of_new_invites)
        print(self.current_event_regular_list)

    def remove_sub_from_email_list(self, root):
        # need to remove the regular from the email list
        print("just swiped SwipeToRemoveRegularFromEmailList")
        for a in self.ids_of_new_sub_invites:
            print(a)
            if root.player_id == a:
                self.ids_of_new_sub_invites.remove(a)
        for a in self.current_event_sub_list:
            print(a)
            if root.player_email == a:
                self.current_event_sub_list.remove(a)


    def remove_individual_from_email_list(self, instance):
        print(self.ids_of_new_individual_invites)
        self.ids_of_new_individual_invites.remove(instance.player_id)
        self.root.ids.list_of_individuals_display.remove_widget(instance)
        print(self.ids_of_new_individual_invites)

    def create_event(self, root):
        '''
        Comes from CREATEEVENTSCREEN
        Original nav drawers
        Changes page to "CurrentEventsPage"
        :param root:
        :return:
        '''
        print("Create_event button was pressed")
        print("Create_event MODULE")
        self.add_event_on_submit()
        self.clear_create_event_textfields()


    def create_quick_event(self, root):
        '''
        comes from the CreateQuickEventScreen
        Adds event into the quickevents.json file
        Used to create a button on the Create Event screen
        For commonly prepared information for events
        pulls textfields - saves to quickevents.json
        :param root:
        :return:
        '''
        self.add_quick_event_on_submit()
        self.clear_create_quick_event_textfields()
        self.add_quick_event_buttons(root)

    def add_quick_event_buttons(self, root):
        print("***IN THE add_quick_event_buttons to add the buttons for each quick event in the json file to the CreateEventScreen into the MDlist with ID:quick_event_buttons")
        self.root.ids.grid_for_quick_event_buttons.clear_widgets()
        dark = True
        with open('quickevents.json') as f:
            quick_events_buttons = json.load(f)
            print(quick_events_buttons.keys())
            for key, val in quick_events_buttons.items():
                print(key)
                print(val)
                print(type(val))
                if isinstance(val, dict):
                    event_id = str(key)
                    print(event_id)
                    print("WE MADE IT TO HERE TRYING TO ADD THE BUTTON")
                    if dark:
                        quick_event_button = QuickEventButtonLight(font_style = "Subtitle2",
                                                                   text=event_id,
                                                                   event_id=key,
                                                                   on_press=self.quickevent)
                        self.root.ids.grid_for_quick_event_buttons.add_widget(quick_event_button)
                        dark = not dark
                    else:
                        quick_event_button = QuickEventButtonDark(font_style="Subtitle2",
                                                                   text=event_id,
                                                                   event_id=key,
                                                                   on_press=self.quickevent)
                        self.root.ids.grid_for_quick_event_buttons.add_widget(quick_event_button)
                        dark = not dark
                    print("JUST ADDED A BUTTON")
                    print("*"*200)
                    print("yes its a dict")

                    for key, val in val.items():
                        print(key)
                        print(val)
                        if isinstance(val, dict):
                            print("yes its a dict2222")
    def add_quick_event_on_submit(self):
        print("*** in the add_quick_event_on_submit button press module")
        with open('quickevents.json') as f:
            quick_events =json.load(f)
            #quick_events["TotalQuickEvents"] += 1
            #self.quick_eventid = self.root.ids.quick_key.text
        self.time = self.root.ids.quick_time.text
        # print(self.time)
        self.location = self.root.ids.quick_location.text
        self.location = self.location.upper()
        # print(self.location)
        self.cost = self.root.ids.quick_cost.text
        # print(self.cost)
        self.totalplayers = self.root.ids.quick_totalplayers.text
        # print(self.totalplayers)
        self.day = self.root.ids.quick_day.text
        self.day = self.day.upper()
        # print("above is unformated")
        # Pulling Event Information
        # print(listobj)
        # print("above is the listobj")
        #self.fdate = self.date[0:2] + '/' + self.date[2:4] + '/' + self.date[4:6]
        self.ftime = TestingIndividualLogicCode.testingfunctions.format_time(self, self.time)
        # self.AMPM = self.time[4:6]
        # self.AMPM = self.AMPM.upper()
        #self.ftime = self.time[0:2] + ':' + self.time[2:4] + self.AMPM
        #self.cost = '$' + self.cost
        #self.flocation = self.location.upper()
        new_quick_event_dict = {
            "Time": self.ftime,
            "Day": self.day,
            "Location": self.location,
            "Cost": self.cost,
            "TotalPlayers": self.totalplayers
        }
        self.quick_eventid = self.day + " " + self.location + " " + self.ftime
        print(self.quick_eventid)
        quick_events[self.quick_eventid] = new_quick_event_dict
        with open('quickevents.json', 'w') as json_file:
            json.dump(quick_events, json_file, indent=4, separators=(',', ':'))
        with open('ContactInfo.json') as f:
            contactinfo =json.load(f)
            with open('quickevents.json') as g:
                dict_of_quick_events = json.load(g)
                contactinfo = TestingIndividualLogicCode.testingfunctions.add_quick_event_to_player_dict(self, contactinfo, dict_of_quick_events, self.quick_eventid)
                with open('ContactInfo.json', 'w') as json_file:
                    json.dump(contactinfo, json_file, indent=4, separators=(',', ':'))
        #NEED TO ADD THE QUICK EVENT TO EVERY PLAYER, AND MAKE SUBS AND REGULARS FOR ANY EVENT A REGULAR FOR THIS EVENT

    def add_event_on_submit(self):
        print("add_event_on_submit MODULE")
        self.clear_current_events()
        with open('myevents.json') as f:
            listobj = json.load(f)
            listobj['TotalEventCount'] += 1
            self.eventid = str(listobj['TotalEventCount'])
            # for piece in listobj:
            #     print(len(piece))
            #     print(piece.get('EventID', "None"))
            #     print('just printed piece')
            #     for i in piece:
            #         print(piece[i])
            #         print("Printing i in piece")
        self.date = self.root.ids.date.text
        #print(self.date)
        self.time = self.root.ids.time.text
        #print(self.time)
        self.location = self.root.ids.location.text
        #print(self.location)
        self.cost = self.root.ids.cost.text
        #print(self.cost)
        self.totalplayers = self.root.ids.totalplayers.text
        #print(self.totalplayers)
        self.day = self.root.ids.day.text
        #print("above is unformated")
        # Pulling Event Information
        #print(listobj)
        #print("above is the listobj")
        #self.fdate = self.date[0:2] + '/' + self.date[2:4] + '/' + self.date[4:6]
        self.fdate = TestingIndividualLogicCode.testingfunctions.format_date(self, self.date)
        self.AMPM = self.time[4:6]
        self.AMPM = self.AMPM.upper()
        #self.ftime = self.time[0:2] + ':' + self.time[2:4] + ' ' + self.AMPM
        self.ftime = TestingIndividualLogicCode.testingfunctions.format_time(self, self.time)
        self.cost = '$' + self.cost
        self.flocation = self.location.upper()
        # print(time)
        # print(cost)
        # print(location)
        new_event_dict = {
                "Date": self.fdate,
                "Day": self.day,
                "Time": self.ftime,
                "Location": self.flocation,
                "Cost": self.cost,
                "TotalPlayers": self.totalplayers,
                "PlayersIn": [],
                "PlayersInvited": [],
                "PlayersPaid": [],
                "Dark": {
                    "Goalie":[],
                    "Line1": {
                        "Forward": [],
                        "Defense": [],
                    },
                    "Line2": {
                        "Forward": [],
                        "Defense": [],
                    }
                },
                "Light": {
                    "Goalie": [],
                    "Line1": {
                        "Forward": [],
                        "Defense": [],
                    },
                    "Line2": {
                        "Forward": [],
                        "Defense": [],
                }
                },
                "Status": "Current",
            }
        already_created = TestingIndividualLogicCode.testingfunctions.check_event_already_created(self, listobj,
                                                                                                  new_event_dict)
        listobj[self.eventid] = new_event_dict

        if already_created:
            print("IN THE ALREADY CREATED")
            self.root.ids.home_screen.add_widget(MDLabel(text="THIS EVENT IS ALREADY CREATED"))
            self.root.ids.screen_manager.current = "HomeScreen"
        else:
            print("IN THE ELSE OF ALREADY CREATED")
            with open('myevents.json', 'w') as json_file:
                json.dump(listobj, json_file, indent=4, separators=(',', ':'))
            self.current_events_displayed()

    def quickevent(self, instance):
        print("quickevent MODULE")
        print(instance.event_id)
        with open('quickevents.json') as f:
            listobj = json.load(f)
            for key, val in listobj.items():
                # print(quickbutton)
                print(key)
                print(val)
                print("*"*250)
                if key == instance.event_id:
                    TestingIndividualLogicCode.testingfunctions.find_current_date_quick_event_date(self, str(listobj[instance.event_id]["Day"]))
                    self.root.ids.time.text = str(listobj[instance.event_id]["Time"])
                    self.root.ids.location.text = str(listobj[instance.event_id]["Location"])
                    self.root.ids.cost.text = str(listobj[instance.event_id]["Cost"])
                    self.root.ids.totalplayers.text = str(listobj[instance.event_id]["TotalPlayers"])
                    self.root.ids.day.text = str(listobj[instance.event_id]["Day"])



    def current_events_displayed(self):
        print("In the current_events_displayed Module")
        with open('myevents.json') as myevents:
            alleventslist = json.load(myevents)
            for allevent in alleventslist:
                if allevent != "TotalEventCount":
                    self.eventid = allevent
                    print(alleventslist[allevent]["Date"])
                    date = alleventslist[allevent]["Date"]
                    day = alleventslist[allevent]['Day']
                    time = alleventslist[allevent]['Time']
                    location = alleventslist[allevent]['Location']
                    cost = alleventslist[allevent]['Cost']
                    totalplayers = alleventslist[allevent]['TotalPlayers']
                    playersin = len(alleventslist[allevent]['PlayersIn']) \
                                + len(alleventslist[allevent]['Dark']['Goalie']) \
                                + len(alleventslist[allevent]['Dark']['Line1']['Forward']) + len(alleventslist[allevent]['Dark']['Line1']['Defense']) \
                                + len(alleventslist[allevent]['Dark']['Line2']['Forward']) + len(alleventslist[allevent]['Dark']['Line2']['Defense']) \
                                + len(alleventslist[allevent]['Light']['Goalie']) \
                                + len(alleventslist[allevent]['Light']['Line1']['Forward']) + len(alleventslist[allevent]['Light']['Line1']['Defense']) \
                                + len(alleventslist[allevent]['Light']['Line2']['Forward']) + len(alleventslist[allevent]['Light']['Line2']['Defense'])
                    event_card = SwipeToDeleteItem2(text2=f'{date} {day} {location} ',
                                                       second_text2=f'{time} ~~ {cost} ~~ {playersin}/{totalplayers}',
                                                       third_text2= f" INV: {len(alleventslist[allevent]['PlayersInvited'])} ~ ASN: {len(alleventslist[allevent]['PlayersIn'])}",
                                                        event_id2 = str(self.eventid))

                    self.root.ids.currentevents_md_list.add_widget(event_card)
            self.root.ids.screen_manager.current = 'CurrentEventsPage'

    def clear_create_event_textfields(self):
        print("clear_create_event_textfields MODULE")
        print("clear_create_event_textfields")
        self.root.ids.date.text = ""
        self.root.ids.time.text = ""
        self.root.ids.location.text = ""
        self.root.ids.cost.text = ""
        self.root.ids.totalplayers.text = ""
#end of the functions for creating event

    def clear_create_quick_event_textfields(self):
        print("clear_quick_create_event_textfields MODULE")
        print("clear_quick_create_event_textfields")
        self.root.ids.date.text = ""
        self.root.ids.time.text = ""
        self.root.ids.location.text = ""
        self.root.ids.cost.text = ""
        self.root.ids.totalplayers.text = ""
    def on_swipe_complete(self, instance):
        print("on_swipe_complete MODULE")
        print(dir(instance))
        print(instance)
        self.root.ids.md_list.remove_widget(instance)
        self.root.ids.screen_manager.current = 'CurrentEventsPage'

    def clear_specific_event(self):
        print("clear_specific_event MODULE")
        print("called from the back_to_current_event function")
        self.root.ids.specific_event_page_box_layout.clear_widgets()
        self.root.ids.specific_event_label.clear_widgets()

    def on_swipe_complete2(self, instance):
        print("on_swipe_complete2 MODULE")
        print("In on swipe 2 complete: " + str(instance.event_id2))
        self.root.ids.currentevents_md_list.clear_widgets()
        self.clear_specific_event()
        self.current_event_identify = instance.event_id2
        TestingIndividualLogicCode.testingfunctions.display_selected_event(self,self.current_event_identify, MDLabel, SwipeToAddPlayerToInList)
        # with open('myevents.json') as myevents:
        #     alleventslist = json.load(myevents)
        #     self.dict_of_event = alleventslist[self.current_event_identify]
        #     self.current_event_players_invited = self.dict_of_event.get("PlayersInvited")
        #     print("TRYING TO PRINT THE LIST OF CURRENT PLAYERS INVITED")
        #     print(self.current_event_players_invited)
        #     #print(self.dict_of_event)
        #     self.current_event_title = str(self.dict_of_event.get("Location") + " " + self.dict_of_event.get("Time"))
        #     self.current_event_day = self.dict_of_event.get('Day')
        #     labeltext = f" {self.dict_of_event.get('Date')}"
        #     labeltext += f" {self.dict_of_event.get('Day')}"
        #     labeltext += f" {self.dict_of_event.get('Location')}"
        #     labeltext += f" {self.dict_of_event.get('Time')}"
        #     labeltext += f"\nInvited: {len(self.dict_of_event.get('PlayersInvited'))}"
        #     labeltext += f" ~ To Assign: {len(self.dict_of_event.get('PlayersIn'))}"
        #     labeltext += f" ~ Goalies: {len(self.dict_of_event['Dark'].get('Goalie')) + len(self.dict_of_event['Light'].get('Goalie'))} \n" \
        #                  f"Dark: {len(self.dict_of_event['Dark']['Line1'].get('Forward')) + len(self.dict_of_event['Dark']['Line1'].get('Defense')) + len(self.dict_of_event['Dark']['Line2'].get('Forward')) + len(self.dict_of_event['Dark']['Line2'].get('Defense')) }" \
        #                  f" ~ Light: {len(self.dict_of_event['Light']['Line1'].get('Forward')) + len(self.dict_of_event['Light']['Line1'].get('Defense')) + len(self.dict_of_event['Light']['Line2'].get('Forward')) + len(self.dict_of_event['Light']['Line2'].get('Defense')) }"
        #     specific_event_heading_label = MDLabel(text=labeltext, halign='center')
        #     self.root.ids.specific_event_page_box_layout.add_widget(specific_event_heading_label)
        # with open('ContactInfo.json') as allcontactinfo:
        #     all_contact_info = json.load(allcontactinfo)
        #     for a in self.dict_of_event.get("PlayersInvited"):
        #         print(all_contact_info[a-1])
        #         namestring = "Name: "
        #         namestring += f"{all_contact_info[a-1].get('Player First')}"
        #         namestring += " " + f"{all_contact_info[a-1].get('Player Last')}"
        #         positionstring = "Pos: "
        #         positionstring += f'{all_contact_info[a-1].get("position F D G")}'
        #         positionstring += "  Line: "
        #         positionstring += f'{all_contact_info[a-1].get("LINE")}'
        #         player_id = int(all_contact_info[a-1].get("playerid"))
        #         print(namestring)
        #         player_card = SwipeToAddPlayerToInList(text=namestring,
        #                                                second_text=positionstring,
        #                                                event_id=self.current_event_identify,
        #                                                player_id=player_id
        #                                                )
        #         self.root.ids.specific_event_label.add_widget(player_card)
        #     # for a in str(singleevent.get(["PlayersIn"])):
        #     #     print(int(a))
        # self.root.ids.screen_manager.current = 'SpecificEventPage'
    def on_swipe_completeevents(self, instance):
        print("Need to pull up the events details")

    def on_swipe_complete3(self, instance):
        print("on_swipe_complete3 MODULE")
        print("In on swipe 3 complete: " +str(instance.search_player_id))
        self.search_player_id = instance.search_player_id
        self.root.ids.found_player_md_list.clear_widgets()
        self.root.ids.screen_manager.current = 'SpecificFoundPlayerScreen'
        with open('ContactInfo.json') as contactinfo:
            allcontactinfo = json.load(contactinfo)
            print(allcontactinfo)
            for singlecontact in allcontactinfo:
                if str(singlecontact.get('playerid')) == instance.search_player_id:
                    a = instance.search_player_id
                    print("Now We In Here")
                    self.index_of_player = int(a)-1
                    print(allcontactinfo[self.index_of_player])
                    dict_of_player = allcontactinfo[self.index_of_player]
                    print(dict_of_player)
                    # print(dict_of_player['Player First'])
                    allkeys = dict_of_player.keys()
                    allvalues = dict_of_player.values()
                    for i in allkeys:
                        print(dict_of_player[i])
                        here = str(i)
                        #print(allvalues[i])
                        textstring = str(dict_of_player[i])
                        if textstring != str(a):
                            button = MDTextField(hint_text= i, text=textstring)
                            self.root.ids.specific_found_player_md_list.add_widget(button)
                        else:
                            label = MDLabel(text=textstring, halign='center')
                            self.root.ids.specific_found_player_md_list.add_widget(label)
                         #self.root.ids.right_md_list.add_widget(self.button, 2)
# id for scroll view: root.ids.specific_found_player_md_list.add_widget(self.mdtextfield)
    def on_swipe_complete4(self, instance):
        print("on_swipe_complete4 MODULE")
        print("In on swipe 4 complete: " +str(instance.search_player_id))
        self.root.ids.found_event_player_md_list.remove_widget(instance)
        self.ids_of_new_individual_invites.append(int(instance.search_player_id))
        print(self.ids_of_new_individual_invites)
        #self.root.ids.screen_manager.current = 'InviteIndividualsScreen'
    def gotoindividualemail(self):
        print("gotoindividualemail: Now change the screen and populate the top email people and quick3_event_text")
        self.root.ids.found_event_player_md_list.clear_widgets()
        self.root.ids.list_of_individuals_display.clear_widgets()
        TestingIndividualLogicCode.testingfunctions.remove_nav_drawer_3_widgets(self)
        with open('standardmessages.json') as allstandardmessages:
            all_standard_messages = json.load(allstandardmessages)
            #print(all_standard_messages)
            specific_message = f'Sub'
            #print(specific_message)
            txt = str(all_standard_messages[specific_message])
            txt = TestingIndividualLogicCode.testingfunctions.replace_email_message(self, self.dict_of_event, txt)
            self.root.ids.quick3_event_text.text = txt
        with open('ContactInfo.json') as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            for a in self.ids_of_new_individual_invites:
                a = int(a)
                print(all_contact_info[a-1].get("Player First"))
                print("Need to add to screen")
                individual_player_card = SwipeToRemoveIndividualFromEmailList(
                    text=all_contact_info[a-1].get("Player First") + " " +
                    all_contact_info[a-1].get("Player Last"),
                    player_id=all_contact_info[a-1].get("playerid"),
                    player_email=all_contact_info[a-1].get("Email"))
                self.root.ids.list_of_individuals_display.add_widget(individual_player_card, 2)
        self.root.ids.screen_manager.current = 'InviteIndividualsScreen'


    def showLeftDrawerPlayers(self, root):
        print("in the showleftdrawerplayers module")
        if self.showManageQuickEvents:
            root.ids.left_md_list.remove_widget(self.addquickeventbutton)
            root.ids.left_md_list.remove_widget(self.addquickeventbutton2)
            root.ids.left_md_list.remove_widget(self.addquickeventbutton3)
            self.showManageQuickEvents = False
        if self.showLeftDrawerPlayersMenu:
            self.playerbutton = MDRaisedButton(font_style='Subtitle2', text='Search Players',
                                               on_press=self.gotosearchplayers,
                                               size_hint=(1, None), padding='10dp', anchor_x='left',
                                               md_bg_color=(.87, .36, .24, 1))
            root.ids.left_md_list.add_widget(self.playerbutton, 1)
            self.playerbutton2 = MDRaisedButton(font_style='Subtitle2', text='Create Player',
                                                on_press=self.createplayer,
                                                size_hint=(1, None), padding='10dp', anchor_x='left',
                                                md_bg_color=(.17, .36, .24, 1))
            root.ids.left_md_list.add_widget(self.playerbutton2, 1)
            self.secondchild = root.ids.left_md_list.children
        else:
            root.ids.left_md_list.remove_widget(self.playerbutton)
            root.ids.left_md_list.remove_widget(self.playerbutton2)

    def addManageQuickEvents(self, root):
        print("***  We are in the showMANAGEQUICKEVENTS module   ***")
        if self.showLeftDrawerPlayersMenu:
            root.ids.left_md_list.remove_widget(self.playerbutton)
            root.ids.left_md_list.remove_widget(self.playerbutton2)
            self.showLeftDrawerPlayersMenu = False
        if self.showManageQuickEvents:
            self.addquickeventbutton = MDRaisedButton(font_style='Subtitle2', text='Add Quick Event',
                                               on_press= self.gotoCreateQuickEventScreen,
                                               size_hint=(1, None), padding='10dp', anchor_x='left',
                                               md_bg_color=(.87, .36, .24, 1))
            root.ids.left_md_list.add_widget(self.addquickeventbutton, 0)
            self.addquickeventbutton2 = MDRaisedButton(font_style='Subtitle2', text='Edit Quick Event',
                                                on_press=self.gotoEditQuickEventScreen,
                                                size_hint=(1, None), padding='10dp', anchor_x='left',
                                                md_bg_color=(.17, .36, .24, 1))
            root.ids.left_md_list.add_widget(self.addquickeventbutton2, 0)
            self.addquickeventbutton3 = MDRaisedButton(font_style='Subtitle2', text='Delete Quick Event',
                                                      on_press=self.gotoDeleteQuickEventScreen,
                                                      size_hint=(1, None), padding='10dp', anchor_x='left',
                                                      md_bg_color=(.87, .36, .24, 1))
            root.ids.left_md_list.add_widget(self.addquickeventbutton3, 0)
        else:
            root.ids.left_md_list.remove_widget(self.addquickeventbutton)
            root.ids.left_md_list.remove_widget(self.addquickeventbutton2)
            root.ids.left_md_list.remove_widget(self.addquickeventbutton3)


    def load_paymentpage(self):
        print("IN THE load_paymentpage MODULE")
        self.root.ids.players_who_need_to_pay.clear_widgets()
        self.root.ids.player_who_need_to_pay2.clear_widgets()
        print(self.dict_of_event)
        print(self.current_event_identify)
        players_to_pay = TestingIndividualLogicCode.testingfunctions.add_player_to_payment_screen(self,self.dict_of_event)
        print(players_to_pay)
        print()
        print("+"*200)
        need_to_pay_label = MDLabel(text="NEED TO PAY",
                                    halign="center",font_style="H6")
        self.root.ids.players_who_need_to_pay.add_widget(need_to_pay_label)
        for number in players_to_pay:
            with open("ContactInfo.json") as f:
                all_contacts = json.load(f)
                print(all_contacts[number - 1])
                if all_contacts[number-1].get("Monies") < 30:
                    player_payment_card = SwipeToPayPlayer(
                        text=all_contacts[number - 1].get("Player First") + " " + all_contacts[number - 1].get(
                            "Player Last"),
                        player_id=number)
                    self.root.ids.players_who_need_to_pay.add_widget(player_payment_card)
                    #players_to_pay.remove(number)
        for number in players_to_pay:
            with open("ContactInfo.json") as f:
                all_contacts = json.load(f)
                print(all_contacts[number - 1])
                if all_contacts[number-1].get("Monies") > 30:
                    player_payment_card = SwipeToPayPlayer2(
                        text=all_contacts[number - 1].get("Player First") + " " + all_contacts[number - 1].get(
                            "Player Last"),
                        second_text = "$" + str(all_contacts[number-1].get("Monies")) + " Money in Account",
                        player_id=number)
                    self.root.ids.players_who_need_to_pay.add_widget(player_payment_card)
                    #players_to_pay.remove(number)
        self.root.ids.player_who_need_to_pay2.add_widget(MDRaisedButton(text="Review Event",
                                                                        size_hint=(1,None),
                                                                        on_press=self.review_Event))

    def review_Event(self, root):
        print("+++   in the review_Event Function   +++")
        self.root.ids.review_event.clear_widgets()
        self.root.ids.screen_manager.current = 'ReviewPage'
        #ID for PLAYER LIST
        #self.root.ids.review_event
        #ID for the button
        #self.root.ids.review_event2
        with open("myevents.json") as f:
            all_events = json.load(f)
            print(all_events[self.current_event_identify])
            dict_of_this_event = all_events[self.current_event_identify]
            paid_players = TestingIndividualLogicCode.testingfunctions.show_paid_players(self, all_events[self.current_event_identify])
            self.attended_players = TestingIndividualLogicCode.testingfunctions.show_all_players(self, all_events[self.current_event_identify])
            print(paid_players)
            print(self.attended_players)
            for player in paid_players:
                if player in self.attended_players:
                    index = self.attended_players.index(player)
                    self.attended_players.pop(index)
            all_players = paid_players + self.attended_players
            print(self.attended_players)
            print("*"*250)
            print(all_players)
            self.root.ids.review_event.add_widget(MDRectangleFlatButton
                                                  (text= "Total Players " + str(len(all_players)) + " / " + dict_of_this_event["TotalPlayers"],
                                                   size_hint=(1, None),
                                                   line_color=(0,0,0,1)))
            self.root.ids.review_event.add_widget(MDRectangleFlatButton
                                                  (text="Paid Players " + str(len(paid_players)) + " / " +
                                                        dict_of_this_event["TotalPlayers"],
                                                   size_hint=(1, None),
                                                   line_color=(0, 0, 1, 1)))

            with open("ContactInfo.json") as file:
                all_contacts = json.load(file)
                for player in paid_players:
                    print(player)
                    for contact_player in all_contacts:
                        if contact_player["playerid"] == player:
                            self.root.ids.review_event.add_widget(MDRectangleFlatButton
                                                          (text= str(contact_player["Player First"] + " " + contact_player["Player Last"]),
                                                           line_color=(0,1,0,1),
                                                           size_hint=(1,None)))
                self.root.ids.review_event.add_widget(MDRectangleFlatButton
                                                      (text="Attended Players " + str(len(self.attended_players)) + " / " +
                                                            dict_of_this_event["TotalPlayers"],
                                                       size_hint=(1, None),
                                                       line_color=(0, 0, 1, 1)))
                for player in self.attended_players:
                        for contact_player in all_contacts:
                            if contact_player["playerid"] == player:
                                self.root.ids.review_event.add_widget(MDRectangleFlatButton
                                                                  (text=str(contact_player["Player First"] + " " +
                                                                            contact_player["Player Last"]),
                                                                   line_color=(1,0,0,1),
                                                                   size_hint=(1,None)))
            print(paid_players)
            print(self.attended_players)
            print(all_players)
            print("%"*250)

    def complete_event(self):
        print("!!!   in the complete_event function   !!!")
        with open("myevents.json") as f:
            all_events = json.load(f)
            this_event = all_events[self.current_event_identify]
            print(this_event)
            completed_event_key = str(this_event["Date"] + " " + this_event["Location"] + " " + this_event["Time"])
            if (self.attended_players):
                with open('notifications.json') as f:
                    all_notifications = json.load(f)
                    this_notification = {completed_event_key:self.attended_players}
                    all_notifications.append(this_notification)
                    with open('notifications.json', 'w') as file:
                        json.dump(all_notifications, file, indent=4, separators=(',', ':'))
            completed_event_value = this_event["PlayersPaid"] + self.attended_players
            print(completed_event_key)
            print(completed_event_value)
            completed_event = {str(completed_event_key):completed_event_value}
            print("%"*250)
            print(completed_event)
            with open('completedevents.json') as f:
                completed_events = json.load(f)
                completed_events.append(completed_event)
                with open('completedevents.json', 'w') as file:
                    json.dump(completed_events, file, indent=4, separators=(',', ':'))
            print("%"*250)
            del all_events[self.current_event_identify]
            with open('myevents.json', 'w') as file:
                json.dump(all_events, file, indent=4, separators=(',', ':'))
        #Need to go into the NOTIFICATIONS.JSON file and pull the keys as "Heading" Cards and the values as "Swipe" Cards
        #To delete the notification
        #
        # event_card = PlayerNotificationCard(text2=f'{date} {day} {location} {time}',
        #                                 second_text2=f'Cost: {cost} ~ Players: {playersin}/{totalplayers}',
        #                                 third_text2=f"INV: {len(alleventslist[allevent]['PlayersInvited'])} ~ TO ASSIGN: {len(alleventslist[allevent]['PlayersIn'])}",
        #                                 event_id2=str(self.eventid))

        self.root.ids.screen_manager.current = 'NotificationScreen'

    def change_to_notifications(self, root):
        print("~~~ change_to_notifications function   ~~~")
        self.root.ids.notifications.clear_widgets()
        with open('notifications.json') as f:
            all_notifications = json.load(f)
            with open('ContactInfo.json') as file:
                all_contacts = json.load(file)
                for this_notification in all_notifications:
                    for key, val in this_notification.items():
                        #self.root.ids.notifications.add_widget(PlayerNotificationCard(text2=str(key)))
                        for single_player in val:
                            this_contact = all_contacts[single_player - 1]
                            self.root.ids.notifications.add_widget(
                                PlayerNotificationCard(text2=str(this_contact["Player First"] + " " + this_contact["Player Last"]),
                                                       second_text2=str(key),
                                                       third_text2="$" + str(this_contact["Monies"]),
                                                       player_id=single_player))
        self.root.ids.screen_manager.current = 'NotificationScreen'

    def remove_player_from_notification(self, instance):
        print("~~~   remove_player_from_notification function   ~~~")
        self.root.ids.notifications.remove_widget(instance)
        index=0
        with open("notifications.json") as f:
            all_notifications = json.load(f)
            for this_notification in all_notifications:
                print(this_notification)
                index += 1
                for key, val in this_notification.items():
                    if key == instance.second_text2:
                        for player in val:
                            print(player)
                            print(type(player))
                            if player == instance.player_id:
                                val.remove(player)
                                if len(val) == 0:
                                    all_notifications.pop(index-1)
                                with open('notifications.json', 'w') as file:
                                    json.dump(all_notifications, file, indent=4, separators=(',', ':'))

    def player_paid(self, instance):
        #add the players number to the "Payment" section of the event dictionary
        print("The player has paid for this event")
        self.root.ids.players_who_need_to_pay.remove_widget(instance)
        with open("myevents.json") as f:
            all_events = json.load(f)
            print(self.dict_of_event)
            all_events[self.current_event_identify]["PlayersPaid"].append(instance.player_id)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_events, json_file, indent=4, separators=(',', ':'))
        print("JUST SAVED THE PLAYER TO PAID")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[self.current_event_identify]
        with open("ContactInfo.json") as f:
            all_contacts = json.load(f)
            print(all_contacts[instance.player_id - 1])
            if all_contacts[instance.player_id - 1].get("Monies") > 30:
                all_contacts[instance.player_id - 1]["Monies"] = all_contacts[instance.player_id - 1].get("Monies") - 30
            print(all_contacts[instance.player_id-1])
            with open('ContactInfo.json', 'w') as json_file:
                json.dump(all_contacts, json_file, indent=4, separators=(',', ':'))



    def gotoDeleteQuickEventScreen(self, root):
        print("*** gotoDeleteQuickEventScreen  ***")
        self.root.ids.edit_quick_event_layout.clear_widgets()
        TestingIndividualLogicCode.testingfunctions.remove_edit_submit(self, root)
        TestingIndividualLogicCode.testingfunctions.closeLeftDrawerQuickButtons(self)
        self.showManageQuickEvents = False
        #self.root.ids.nav_drawer.set_state('close')
        self.root.ids.screen_manager.current = 'EditQuickEventScreen'
        dark = True
        with open("quickevents.json") as f:
            all_dict_quick_events = json.load(f)
            for key, val in all_dict_quick_events.items():
                if isinstance(val, dict):
                    if dark:
                        self.quick_event_panel = QuickEventButtonLight(text=key,event_id=str(key), on_press=self.deleteQuickEvent)
                        self.root.ids.edit_quick_event_layout.add_widget(self.quick_event_panel)
                        dark = not dark
                    else:
                        self.quick_event_panel = QuickEventButtonDark(text=key, event_id=str(key),
                                                                       on_press=self.deleteQuickEvent)
                        self.root.ids.edit_quick_event_layout.add_widget(self.quick_event_panel)
                        dark = not dark


    def change_to_event_home_screen(self):
        self.root.ids.screen_manager.current = "SpecificEventPage"

    def deleteQuickEvent(self, instance):
        print("%%% in the deleteQuickEvent Module")
        print(instance.event_id)
        with open("quickevents.json") as f:
            all_dict_quick_events = json.load(f)
            #all_dict_quick_events["TotalQuickEvents"] -= 1
            all_dict_quick_events.pop(instance.event_id)
            with open("quickevents.json", 'w') as json_file:
                json.dump(all_dict_quick_events, json_file, indent=4, separators=(',', ':'))
        self.root.ids.screen_manager.current = 'HomeScreen'
        self.root.ids.edit_quick_event_layout.clear_widgets()
    def gotoEditQuickEventScreen(self, root):
        print("***  gotoEditQuickEventScreen")
        self.root.ids.edit_quick_event_layout.clear_widgets()
        TestingIndividualLogicCode.testingfunctions.remove_edit_submit(self, root)
        TestingIndividualLogicCode.testingfunctions.closeLeftDrawerQuickButtons(self)
        self.showManageQuickEvents = False
        self.root.ids.screen_manager.current = 'EditQuickEventScreen'
        dark = True
        with open("quickevents.json") as f:
            all_dict_quick_events = json.load(f)
            for key, val in all_dict_quick_events.items():
                if isinstance(val, dict):
                    if dark:
                        self.quick_event_panel = QuickEventButtonLight(text=key,event_id=str(key), on_press=self.editQuickEvent)
                        self.root.ids.edit_quick_event_layout.add_widget(self.quick_event_panel)
                        dark = not dark
                    else:
                        self.quick_event_panel = QuickEventButtonDark(text=key, event_id=str(key),
                                                                       on_press=self.editQuickEvent)
                        self.root.ids.edit_quick_event_layout.add_widget(self.quick_event_panel)
                        dark = not dark
        self.root.ids.edit_quick_event_layout.add_widget(MDSeparator(color=(0,0,0,1), size_hint=(.8,None)))
        self.root.ids.edit_quick_event_layout2.add_widget(MDFillRoundFlatButton(text="Submit",on_press=self.saveTheQuickEvents))
        #self.root.ids.edit_quick_event_layout.add_widget()

#START WORKING HERE
#TRYING TO GET THE MDTEXTFIELDS TO UPDATE THEIR TEXT ATTRIBUTE
    def editQuickEvent(self, instance):
        print("%%%  in the editQuickEvent Module  %%%")
        self.showManageQuickEvents = False
        self.root.ids.nav_drawer.set_state('close')
        delete_range = 0
        for child in self.root.ids.edit_quick_event_layout.children[:]:
            if isinstance(child, QuickEventTextField):
                print("***")
                print(child)
                delete_range += 1
        for child in self.root.ids.edit_quick_event_layout.children[:delete_range]:
            self.root.ids.edit_quick_event_layout.remove_widget(child)
        self.event_id = instance.event_id
        self.quick_event_text_field_id = []
        #need to open the dictionary and add the MDTextfields with info and ids etc.
        with open("quickevents.json") as f:
            all_dict_quick_events = json.load(f)
            for key, val in all_dict_quick_events.items():
                if isinstance(val, dict):
                    print("PRINTING KEY2 VAL2")
                    for key2, val2 in val.items():
                        if key == instance.event_id:
                            print(key2, val2)
                            if str(key2) == "Enabled":
                                quick_event_text_field = QuickEventTextField(hint_text=str(key2)+" EMPTY = False", text=str(val2),
                                                                             id=str(key2))
                                self.root.ids.edit_quick_event_layout.add_widget(quick_event_text_field)
                                self.quick_event_text_field_id.append(str(key2))
                            else:
                                quick_event_text_field = QuickEventTextField(hint_text= str(key2), text=str(val2), id=str(key2))
                                self.root.ids.edit_quick_event_layout.add_widget(quick_event_text_field)
                                self.quick_event_text_field_id.append(str(key2))
        #self.root.ids.edit_quick_event_layout2.add_widget(QuickEventButton(text="Submit", event_id=instance.event_id, on_press=self.saveTheQuickEvents))

    def saveTheQuickEvents(self, root):
        print("%%%  in the saveTheQuickEvents  %%%")
        self.dict_of_edit_quick_event = {}
        for child in self.root.ids.edit_quick_event_layout.children:
            if isinstance(child, QuickEventTextField):
                #print(child)
                print(child.id)
                print(child.text)
                if child.id == "Enabled" and child.text and child.text != "False":
                    print("in if #1")
                    self.dict_of_edit_quick_event[child.id] = True
                if child.id == "Enabled" and child.text == "False" or not child.text:
                    print("in if #2")
                    self.dict_of_edit_quick_event[child.id] = False
                if child.id != "Enabled":
                    print("in if #3")
                    self.dict_of_edit_quick_event[child.id] = child.text
        with open("quickevents.json") as f:
            all_dict_quick_events = json.load(f)
            for key, val in all_dict_quick_events.items():
                if key == self.event_id:
                    all_dict_quick_events[key] = self.dict_of_edit_quick_event
        with open('quickevents.json', 'w') as json_file:
            json.dump(all_dict_quick_events, json_file, indent=4, separators=(',', ':'))
        self.root.ids.edit_quick_event_layout.clear_widgets()
        TestingIndividualLogicCode.testingfunctions.remove_edit_submit(self, root)
        self.root.ids.screen_manager.current = 'HomeScreen'


        #self.root.ids.left_md_list.clear_widgets(self.root.ids.left_md_list[:4])
        # for child in self.root.ids.left_md_list.children:
        #     print(child)
        #     if isinstance(child,QuickEventButton):
        #         print("Made it into here")

    def gotoCreateQuickEventScreen(self, root):
        print("***  gotoCreateQuickEventScreen")
        TestingIndividualLogicCode.testingfunctions.clear_quick_event_text_fields(self,root)
        self.root.ids.screen_manager.current = 'CreateQuickEventScreen'
        TestingIndividualLogicCode.testingfunctions.closeLeftDrawerQuickButtons(self)
        self.showManageQuickEvents = False
        #self.root.ids.nav_drawer.set_state('close')


    def showRightDrawerEvents(self, root):
        print("showRightDrawerEvents MODULE")
        if self.showRightDrawerEventsMenu:
            self.button = MDRaisedButton(font_style = 'Subtitle2', text='Current Events', on_press= self.showcurrentevent, size_hint = (1, None), padding = '10dp',   anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.right_md_list.add_widget(self.button, 1)
            self.button2 = MDRaisedButton(font_style = 'Subtitle2', text='Completed Events', on_press= self.showcompletedevent, size_hint = (1, None), padding = '10dp',  anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.right_md_list.add_widget(self.button2, 1)
            self.secondchild = root.ids.right_md_list.children
            print(self.secondchild)
        else:
            root.ids.right_md_list.remove_widget(self.button)
            root.ids.right_md_list.remove_widget(self.button2)

    def showcurrentevent(self, root):
        print("showcurrentevent MODULE")
        self.root.ids.right_md_list.remove_widget(self.button)
        self.root.ids.right_md_list.remove_widget(self.button2)
        self.showRightDrawerEventsMenu = not self.showRightDrawerEventsMenu
        self.clear_current_events()
        self.current_events_displayed()
        self.root.ids.nav_drawer2.set_state('close')
        print("Just printed ids")


    def showcompletedevent(self, root):
        print("showcompletedevent MODULE")
        self.root.ids.right_md_list.remove_widget(self.button)
        self.root.ids.right_md_list.remove_widget(self.button2)
        self.showRightDrawerEventsMenu = not self.showRightDrawerEventsMenu
        print("showcompletedevent pressed also")
        print("NEED TO CHANGE SCREEN TO COMPLETED EVENTS")
        self.root.ids.screen_manager.current = "CompletedEventsPage"
        with open("completedevents.json") as completedevents:
            allcompletedevents = json.load(completedevents)
            for singleevent in allcompletedevents:
                print(singleevent)
                for key, val in singleevent.items():
                    print(key)
                    print(val)
                    event_card = CompletedEvents(
                        text2 = str(key),
                        second_text2 = str(val)
                    )
                    self.root.ids.completed_md_list.add_widget(event_card)
    def clear_current_events(self):
        print("clear_current_events MODULE")
        self.root.ids.currentevents_md_list.clear_widgets()

    def remove_player_invited_add_player_in(self, file, event_id, player_id):
        print("in the specific event heading label")
        with open(file) as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[event_id].get("PlayersInvited").remove(player_id)
            all_current_events[event_id].get("PlayersIn").append(player_id)
            self.dict_of_event = all_current_events[event_id]
            labeltext = f" {self.dict_of_event.get('Date')}"
            labeltext += f" {self.dict_of_event.get('Day')}"
            labeltext += f" {self.dict_of_event.get('Location')}"
            labeltext += f" {self.dict_of_event.get('Time')}"
            labeltext += f"\nInvited: {len(self.dict_of_event.get('PlayersInvited'))}"
            labeltext += f" ~ Assign: {len(self.dict_of_event.get('PlayersIn'))}"
            labeltext += f" ~ Goalies: {len(self.dict_of_event['Dark'].get('Goalie')) + len(self.dict_of_event['Light'].get('Goalie'))} \n" \
                         f"Dark: {len(self.dict_of_event['Dark']['Line1'].get('Forward')) + len(self.dict_of_event['Dark']['Line1'].get('Defense')) + len(self.dict_of_event['Dark']['Line2'].get('Forward')) + len(self.dict_of_event['Dark']['Line2'].get('Defense'))}" \
                         f" ~ Light: {len(self.dict_of_event['Light']['Line1'].get('Forward')) + len(self.dict_of_event['Light']['Line1'].get('Defense')) + len(self.dict_of_event['Light']['Line2'].get('Forward')) + len(self.dict_of_event['Light']['Line2'].get('Defense'))}"
            specific_event_heading_label = MDLabel(text=labeltext, halign='center')
            self.root.ids.specific_event_page_box_layout.add_widget(specific_event_heading_label)
            with open('myevents.json', 'w') as json_file:
                json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            self.dict_of_event = all_current_events[event_id]
    def add_player_to_in_list(self, instance):
        print("In the add_player_to_in_list")
        print(instance.event_id)
        print(instance.player_id)
        self.root.ids.specific_event_label.remove_widget(instance)
        self.root.ids.specific_event_page_box_layout.clear_widgets()
        self.remove_player_invited_add_player_in("myevents.json", instance.event_id, instance.player_id)


    def gotosearchplayers(self, root):
        print("gotosearchplayers MODULE")
        self.root.ids.left_md_list.remove_widget(self.playerbutton)
        self.root.ids.left_md_list.remove_widget(self.playerbutton2)
        self.root.ids.found_event_player_md_list.clear_widgets()
        self.showLeftDrawerPlayersMenu = not self.showLeftDrawerPlayersMenu
        print("in the search players module")
        with open('ContactInfo.json') as f:
            all_contacts = json.load(f)
            for key, val in all_contacts[0].items():
                print(key, val)
                if str(key) != "playerid":
                    create_player_textfields = QuickEventTextField(id=str(key), hint_text=str(key))
                    self.root.ids.search_fields.add_widget(create_player_textfields)

        self.root.ids.screen_manager.current = 'SearchPlayerScreen'
        self.root.ids.nav_drawer.set_state('close')

    def searchplayers(self):
        print("searchplayers MODULE")
        self.root.ids.found_player_md_list.clear_widgets()
        #searchplayerlist = ["Player First", "Player Last", "Cell Number", "Email", "position F D G", "LINE"]
        print("start criteria seach and display player cards")
        #textfields = [md_text_field.text for md_text_field in self.root.ids.search_fields.children]
        searchdictionary = {}
        for child in self.root.ids.search_fields.children[:]:
            print(child.id)
            print(child.text)
            searchdictionary[child.id] = str(child.text.upper())
        # print(textfields)
        # searchdictionary = dict(zip(searchplayerlist,reversed(textfields)))
        print(searchdictionary)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ just printed searchdictionary")
        with open('ContactInfo.json') as contactinfo:
            allcontactinfo = json.load(contactinfo)
            print(allcontactinfo)
            for key, val in searchdictionary.items():
                print(key, val)
                print(type(key))
                print(type(val))
                for singlecontact in allcontactinfo:
                    print(":"*250)
                    print(singlecontact[key])
                    if key != "position F D G" and key != "Monies" and singlecontact[key] != "" and singlecontact[key].upper() == val:
                            #singlecontact.get(singlekey).find(searchdictionary.get(singlekey)) != -1:
                        print("IM IN HERE")
                        playerfirst = singlecontact['Player First']
                        playerlast = singlecontact['Player Last']
                        playercell = singlecontact['Cell Number']
                        playeremail = singlecontact['Email']
                        searchhit = singlecontact[str(key)]
                        player_card = SwipeToDeletePlayerCard(text3=f'SEARCH: {searchhit}',
                                                              second_text3=f'{playerfirst} {playerlast}',
                                                              third_text3=f'{playercell} {playeremail}',
                                                              search_player_id = str(singlecontact['playerid']),
                                                              )
                        self.root.ids.found_player_md_list.add_widget(player_card)
                    # print(singlecontact.get(singlekey))
                    # print("just printed the singlecontact.get(singlekey))")
                    if key == "position F D G" and val != "":
                        a = singlecontact.get(str(key)).find(val)
                        if a != -1:
                            print(a)
                            print("Made it into here")
                            playerfirst = singlecontact['Player First']
                            playerlast = singlecontact['Player Last']
                            playercell = singlecontact['Cell Number']
                            playeremail = singlecontact['Email']
                            searchhit = singlecontact[str(key)]
                            player_card = SwipeToDeletePlayerCard(text3=f'SEARCH: {searchhit}',
                                                                  second_text3=f'{playerfirst} {playerlast}',
                                                                  third_text3=f'{playercell} {playeremail}',
                                                                  search_player_id=str(singlecontact['playerid']),
                                                                  )
                            self.root.ids.found_player_md_list.add_widget(player_card)
                    if key == "Monies" and singlecontact["Monies"] != 0 and val != "":
                        print("Made it into here")
                        playerfirst = singlecontact['Player First']
                        playerlast = singlecontact['Player Last']
                        playercell = singlecontact['Cell Number']
                        playeremail = singlecontact['Email']
                        searchhit = singlecontact[str(key)]
                        player_card = SwipeToDeletePlayerCard(text3=f'SEARCH: {searchhit}',
                                                              second_text3=f'{playerfirst} {playerlast}',
                                                              third_text3=f'{playercell} {playeremail}',
                                                              search_player_id=str(singlecontact['playerid']),
                                                              )
                        self.root.ids.found_player_md_list.add_widget(player_card)
        self.root.ids.search_fields.clear_widgets()
        self.root.ids.screen_manager.current = 'FoundPlayerScreen'

    def saveeditfromsearchplayer(self):
        print("saveeditfromsearchplayer MODULE")
        print("here is where the .json save needs to go")
        foundplayerlist = ["playerid", "Player First", "Player Last", "Cell Number", "Email",
                            "position F D G", "LINE", "Tuesday", "Friday", "Sunday", "Monies", "Out", "Suspended"]
        md_text_fields2 = [md_text_field.text for md_text_field in self.root.ids.specific_found_player_md_list.children]
        for md_text_field in self.root.ids.specific_found_player_md_list.children:
            if isinstance(md_text_field, MDTextField):
                print(md_text_field.hint_text)
        insertdictionary = dict(zip(foundplayerlist,reversed(md_text_fields2)))
        try:
            insertdictionary["Monies"] = int(insertdictionary["Monies"])
        except:
            insertdictionary['Monies'] = 0
        insertdictionary['playerid'] = int(self.search_player_id)
        print(insertdictionary)
        print("just printed the dictionary to insert")
        with open('ContactInfo.json') as contactinfo:
            self.allcontactinfo = json.load(contactinfo)
            #fileplayersave = self.allcontactinfo[self.index_of_player]
            self.allcontactinfo[self.index_of_player] = insertdictionary
            with open('ContactInfo.json', 'w') as json_file:
                json.dump(self.allcontactinfo, json_file, indent=4, separators=(',', ':'))
        # for empty_search_field in self.root.ids.search_fields.children:
        #     empty_search_field.text = ""
        self.change_home_screen()

    def clear_search_text_fields(self):
        pass

    def createplayer(self, root):
        print("in the create player module")
        print("coming from clicking the player - create player button on left nav menu")
        self.root.ids.left_md_list.remove_widget(self.playerbutton)
        self.root.ids.left_md_list.remove_widget(self.playerbutton2)
        self.showLeftDrawerPlayersMenu = not self.showLeftDrawerPlayersMenu
        with open('ContactInfo.json') as f:
            all_contacts = json.load(f)
            for key, val in all_contacts[0].items():
                print(key, val)
                if str(key) != "playerid":
                    #TestingIndividualLogicCode.testingfunctions.add_with_path_and_class(self, self.root.ids.create_player_fields, QuickEventTextField(id=str(key), hint_text=str(key)))
                    create_player_textfields = QuickEventTextField(id=str(key), hint_text=str(key))
                    self.root.ids.create_player_fields.add_widget(create_player_textfields)
        # for md_text_field in self.root.ids.create_player_fields.children:
        #     md_text_field.text = ""
        self.root.ids.screen_manager.current = 'CreatePlayerScreen'
        self.root.ids.nav_drawer.set_state('close')

#COMEHERE
    def save_create_player(self, root):
        print("we just came from the CreatePlayerScreen")
        print("just clicked the CREATE PLAYER button")
        print("in the save_create_player module")
        insertdictionary = {}
        saveplayer = False
        # for child in self.root.ids.create_player_fields.children[:]:
        #     print(child.id)
        #     print(child.text)
        #     insertdictionary[str(child.id)] = str(child.text.upper())
        insertdictionary, saveplayer = TestingIndividualLogicCode.testingfunctions.check_create_player_text_fields(self, insertdictionary, saveplayer)
        print(insertdictionary)
        print(saveplayer)
        try:
            insertdictionary["Monies"] = int(insertdictionary["Monies"])
        except:
            insertdictionary['Monies'] = 0
        with open("ContactInfo.json") as allcontactinfo:
            self.all_contact_info = json.load(allcontactinfo)
            player_id = int(len(self.all_contact_info)) + 1
            print(player_id)
            insertdictionary['playerid'] = player_id
            self.all_contact_info.append(insertdictionary)
            print(self.all_contact_info)

            with open('ContactInfo.json', 'w') as json_file:
                json.dump(self.all_contact_info, json_file, indent=4, separators=(',', ':'))
        self.root.ids.create_player_fields.clear_widgets()
        # for md_text_field in self.root.ids.create_player_fields.children:
        #     md_text_field.text = ""

        self.root.ids.screen_manager.current = "HomeScreen"
    def just_testing(self):
        TestingIndividualLogicCode.makingtable.testing_key_word_args("testing", "self", "printing")

    def clear_search_players(self):
        print("clear_search_players MODULE")
        self.root.ids.player_md_list.clear_widgets()


    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen



DemoApp().run()
