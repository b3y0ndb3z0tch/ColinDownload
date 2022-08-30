#Working in:
# def send_final_email(self):
# need to structure email to send
# identify "table" of players and their positions
# personalize email for individual player

#need to refresh the individual player search findings swipe cards

#have the scroll views displaying the players - might need to put LINE 2 in the bottom or LIGHT players in the bottom
#need to have TOTAL LENGTHS of forwards defense somewhere???
#change_light_assign needs to be reworked and renamed

import json

from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivy.utils import get_color_from_hex
from kivymd.material_resources import dp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDCardSwipe
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget, OneLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch, \
    ThreeLineAvatarIconListItem, TwoLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
import TestingIndividualLogicCode.testingfunctions
import TestingIndividualLogicCode.alerts
import TestingIndividualLogicCode.makingtable
from kivy.properties import partial
from kivymd.uix.list import OneLineListItem
#when in invite - need to refresh the search for players
#when in invite - need to give option to go back to event home screen

#ADD INFORMATION TO EMAIL BY insert_date string replace
#Add players when email is sent to the playersinvited on the json file


Window.size = (300, 500)


navigation_helper = """
<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.on_swipe_complete(root)
    # padding: '8dp'
    # spacing: '20dp'
    MDCardSwipeLayerBox:
        # Content under the card.

    MDCardSwipeFrontBox:
        md_bg_color: .8,.3,.2,1
        # Content of card.
        ThreeLineListItem:
            id: content
            text: root.text
            secondary_text: root.second_text
            tertiary_text: root.third_text
            _no_ripple_effect: True

<SwipeToDeleteItem2>:
    size_hint_y: None
    height: content.height
    on_swipe_complete: app.on_swipe_complete2(root)
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
            event_id2: root.event_id2
            _no_ripple_effect: True
            on_release: 
                print(root.third_text2)
                print(root.event_id2)
                
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
    height: content.height
    on_swipe_complete: app.add_player_to_in_list(root)
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
    tertiary_text: root.third_text
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
    # LeftContainer:
    #     id: left_container
    #     MDIconButton:
    #         icon: "alpha-a-circle"
    #         on_press:
    #             print("LEFT PLUS")
    #             app.organize_event_add_to_d1(root)
    #     MDIconButton:
    #         icon: "alpha-b-circle"
    #         on_press:
    #             print("LEFT MINUS")
    #             app.organize_event_add_to_d2(root)
    #     MDIconButton:
    #         icon: "alpha-a-circle"
    #         on_press:
    #             print("LEFT PLUS")
    #             app.organize_event_add_to_d1(root)
    #     MDIconButton:
    #         icon: "alpha-b-circle"
    #         on_press:
    #             print("LEFT MINUS")
    #             app.organize_event_add_to_d2(root)
    # RightContainer:
    #     id: right_container
    #     MDIconButton:
    #         icon: "alpha-a-circle-outline"
    #         on_press:
    #             print("RIGHT PLUS")
    #             app.organize_event_add_to_l1(root)
    #     MDIconButton:
    #         icon: "alpha-b-circle-outline"
    #         on_press:
    #             print("RIGHT MINUS")
    #             app.organize_event_add_to_l2(root)
                
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
    bg_color: .4,.63,.79,1
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
    bg_color: .95,.54,.47,1
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
<TryingButtonLight>:
    text: root.text
    player_id: root.player_id
    md_bg_color: 1,.5,.1,1
    pos_hint: {"center_x": .5, "center_y": .5}

MDScreen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            MDScreen:
                name: "HomeScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "BAH"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['face-profile', lambda x: nav_drawer2.set_state('open')]]
                    Widget:
            MDScreen:
                name: "CreateEventScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Create Event"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['face-profile', lambda x: nav_drawer2.set_state('open')]]
                    BoxLayout:
                        id: quick_button_layout
                        orientation: 'vertical'
                        BoxLayout:
                            padding: '10dp'
                            spacing: '10dp'
                            MDRaisedButton:
                                #pos_hint:{'center_x': 0, 'y':None}
                                id: quickevent1
                                text: "1"
                                on_press:
                                    app.quickevent(self.text)
                            MDRaisedButton:
                                #pos_hint: {'center_x': .5, 'y':None}
                                id: quickevent2 
                                text: "2"
                                on_press:
                                    app.quickevent(self.text)
                            MDRaisedButton:
                                #pos_hint: {'center_x': 1, 'y':None}
                                id: quickevent3
                                text: "3"
                                on_press:
                                    app.quickevent(self.text)
                        MDTextField:
                            id: date
                            hint_text: "Date: MMDDYY - 010522"
                            max_text_lenght: 6
                            pos_hint: {"center_x": .5, "top": 1}
                            size_hint: (1, None)
                        MDTextField:
                            id: time
                            hint_text: "Time: 0900pm"
                            helper_text: "900PM"
                            pos_hint: {"center_x": .5, 'center_y': .7}
                            size_hint: (1, None)
                        MDTextField:
                            id: day
                            hint_text: "Day: Monday"
                            pos_hint: {"center_x": .5, "top": 1}
                            size_hint: (1, None)
                        MDTextField:
                            id: location
                            hint_text: "Location: Kroc"
                            pos_hint: {"center_x": .5, 'center_y': .5}
                            size_hint: (1, None)
                        MDTextField:
                            id: cost
                            hint_text: "Cost: $30"
                            pos_hint: {"center_x": .5, 'center_y': .3}
                            size_hint: (1, None)
                        MDTextField:
                            id: totalplayers
                            hint_text: "TOTAL PLAYERS"
                            pos_hint: {"center_x": .5, 'center_y': .2}
                            size_hint: (1, None)
                        MDRaisedButton:
                            text: "Submit"
                            pos_hint: {"center_x": .5, 'center_y': .1}
                            size_hint: (1, None)
                            on_press:
                                app.create_event(root)
                                root.ids.screen_manager.current = "CurrentEventsPage"
            MDScreen:
                name: "SearchPlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Search Player"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: search_fields
                            MDTextField:
                                id: playerfirst
                                hint_text: "First Name"
                                pos_hint: {"center_x": .5, "top": 1}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerlast
                                hint_text: "Last Name"
                                pos_hint: {"center_x": .5, 'center_y': .7}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerphone
                                hint_text: "Phone Number 12345678901"
                                pos_hint: {"center_x": .5, "top": 1}
                                size_hint: (1, None)
                            MDTextField:
                                id: playeremail
                                hint_text: "Email"
                                pos_hint: {"center_x": .5, 'center_y': .5}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerposition
                                hint_text: "Position F D G"
                                pos_hint: {"center_x": .5, 'center_y': .3}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerline
                                hint_text: "Line #"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)
                    MDRaisedButton:
                        text: "Search Players"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
                        on_press:
                            app.searchplayers()
            MDScreen:
                name: "CreatePlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Create Player"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: create_player_fields
                            MDTextField:
                                id: playerfirst
                                hint_text: "First Name"
                                pos_hint: {"center_x": .5, "top": 1}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerlast
                                hint_text: "Last Name"
                                pos_hint: {"center_x": .5, 'center_y': .7}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerphone
                                hint_text: "Phone Number 12345678901"
                                pos_hint: {"center_x": .5, "top": 1}
                                size_hint: (1, None)
                            MDTextField:
                                id: playeremail
                                hint_text: "Email"
                                pos_hint: {"center_x": .5, 'center_y': .5}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerposition
                                hint_text: "Position 'F' 'D' 'G'"
                                pos_hint: {"center_x": .5, 'center_y': .3}
                                size_hint: (1, None)
                            MDTextField:
                                id: playerline
                                hint_text: "Line # - '1' '2'"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)                            
                            MDTextField:
                                id: play_tuesday
                                hint_text: "Tuesday 'R' - Regular 'S' - Sub"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)                            
                            MDTextField:
                                id: play_friday
                                hint_text: "Friday 'R' - Regular 'S' - Sub"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)                            
                            MDTextField:
                                id: play_sunday
                                hint_text: "Sunday 'R' - Regular 'S' - Sub"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)                            
                            MDTextField:
                                id: player_monies
                                hint_text: "Banked Money '30'"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)                            
                            MDTextField:
                                id: player_out
                                hint_text: "Player Out 'Y' - Yes 'N' - No"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)                            
                            MDTextField:
                                id: player_suspended
                                hint_text: "Suspended Enter Date: 'MMDDYY'"
                                pos_hint: {"center_x": .5, 'center_y': .2}
                                size_hint: (1, None)
                    MDRaisedButton:
                        text: "Create Player"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
                        on_press:
                            app.save_create_player(root)
            MDScreen:
                name: "SearchInviteIndividualPlayer"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Search Individual"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: 
                            [
                            #['home', lambda x: app.change_home_screen()],
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
            MDScreen:
                name: "FoundPlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Found 1 Player"
                        elevation: 10
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
            MDScreen:
                name: "FoundEventInvitePlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Event Found Player"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
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
                            
                        
            MDScreen:
                name: "SpecificFoundPlayerScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Edit Player Info"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['face-profile', lambda x: nav_drawer2.set_state('open')]]
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
            MDScreen:
                name: "CurrentEventsPage"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Current Events"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['face-profile', lambda x: nav_drawer2.set_state('open')]]
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: currentevents_md_list
                            padding: '5dp'
                            spacing: '10dp'
            MDScreen:
                name: "CompletedEventsPage"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Completed Events"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['face-profile', lambda x: nav_drawer2.set_state('open')]]
                    Widget:
                    ScrollView:
                        scroll_timeout: 100
                        MDList:
                            id: completed_md_list
                    MDRaisedButton:
                        text: "Raised Button"
                        pos_hint: {"center_x": .5}
                        size_hint: (1, None)
            MDScreen:
                name: "SpecificEventPage"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Invited Guests"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                        right_action_items: 
                            [
                            ['account-alert', lambda x: app.display_assigned_dark()],
                            ['account-alert-outline', lambda x: app.change_light_assign()],
                            ['face-profile', lambda x: nav_drawer3.set_state('open')]
                            ]
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDBoxLayout:
                            id: specific_event_page_box_layout
                            orientation: 'vertical'
                            size_hint: (1,.2)
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: specific_event_label
                                spacing: '8dp'
                                padding: '8dp'
                                MDLabel:
                                    text: "Invited Players"
                                    halign: 'center'
                                    spacing: '8dp'
            MDScreen:
                name: "InviteRegularsScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Invite Regulars"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                        right_action_items: [['face-profile', lambda x: nav_drawer3.set_state('open')]]
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
                            on_press:
                                app.inviteregularssendemail()            
            MDScreen:
                name: "InviteIndividualsScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Invite Individuals"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                        right_action_items: [['face-profile', lambda x: nav_drawer3.set_state('open')]]
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
            MDScreen:
                name: "InviteSubsScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Invite Subs"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [['home', lambda x: app.change_home_screen()]]
                        right_action_items: [['face-profile', lambda x: nav_drawer3.set_state('open')]]
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
                            on_press:
                                app.invitesubssendemail()
            MDScreen:
                name: "OrganizeEventScreen"
                BoxLayout:
                    orientation: 'vertical'
                    #spacing: '15dp'
                    MDToolbar:
                        title: "Organize Event"
                        elevation: 10
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
                            ['face-profile', lambda x: nav_drawer3.set_state('open')]
                            ]
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDBoxLayout:
                            id: organize_event_page_box_layout
                            orientation: 'vertical'
                            size_hint: (1,.2)             
                        ScrollView:
                            scroll_timeout: 100
                            #size_hint: (1,.5)
                            #size: (Window.width, Window.height- dp(20))
                            MDList:
                                id: organize_event_label
                                spacing: '15dp'                            
            MDScreen:
                name: "AssignDark"
                BoxLayout:
                    orientation: 'vertical'
                    #spacing: '15dp'
                    MDToolbar:
                        title: "Dark Lines"
                        elevation: 10
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
                            ['face-profile', lambda x: nav_drawer3.set_state('open')]
                            ]                           
                    MDBoxLayout:   
                        orientation: 'vertical'                   
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_dark_line1
                                spacing: '15dp'
                        MDSeparator:
                        MDSeparator:
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_dark_line2
                                spacing: '15dp'
            MDScreen:
                name: "AssignLight"
                BoxLayout:
                    orientation: 'vertical'
                    #spacing: '15dp'
                    MDToolbar:
                        title: "Light Lines"
                        elevation: 10
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
                            ['face-profile', lambda x: nav_drawer3.set_state('open')]
                            ]                           
                    MDBoxLayout:   
                        orientation: 'vertical'                   
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_light_line1
                                spacing: '15dp'
                        MDSeparator:
                        MDSeparator:
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: organize_light_line2
                                spacing: '15dp'     
            MDScreen:
                name: "DisplayTeams"
                BoxLayout:
                    orientation: 'vertical'
                    #spacing: '15dp'
                    MDToolbar:
                        title: "Full Teams"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: 
                            [
                            #['home', lambda x: app.change_home_screen()],
                            ['home-export-outline',lambda x: app.back_to_current_event()]
                            ]
                        right_action_items: 
                            [
                            #['account-alert', lambda x: nav_drawer3.set_state('open')],
                            #['account-alert-outline', lambda x: app.change_light_assign()],
                            ['email-edit-outline', lambda x: app.send_final_email()],
                            ['face-profile', lambda x: nav_drawer3.set_state('open')]
                            ]                           
                    MDBoxLayout:                    
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: display_dark
                                spacing: '15dp'
                        ScrollView:
                            scroll_timeout: 100
                            MDList:
                                id: display_light
                                spacing: '15dp'                   
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
                                #root.ids.screen_manager.current = "HomeScreen"
                                #nav_drawer.set_state('close')
                        MDRaisedButton:
                            text: 'Another Button For Adding'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('Another Drawer Button was pressed')
                                root.ids.screen_manager.current = "HomeScreen"
                                nav_drawer.set_state('close')
                                app.just_testing()
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
                            text: 'Players'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('Players RIGHT Drawer Button was pressed')
                                #root.ids.screen_manager.current = "HomeScreen"
                                nav_drawer2.set_state('close')
                                #nav_drawer.set_state('close')
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
               
"""



class Tab(MDFloatLayout, MDTabsBase):
    # To implement content for a tab
    pass



class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
    event_id = StringProperty()
    orientation: 'vertical'
    type_swipe = 'auto'
    anchor = 'left'
    _no_ripple_effect = True
    # size_hint = 1, .3

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

class TryingButtonLight(MDRaisedButton):
    text = StringProperty()
    player_id = NumericProperty()

class CreateEventScreen(MDScreen):
    pass

class LeftContainer(ILeftBodyTouch, MDBoxLayout):
    adaptive_width = True

class RightContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class OrganizePlayerToTeam(ThreeLineAvatarIconListItem):
    text = StringProperty()
    second_text = StringProperty()
    third_text = StringProperty()
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



class DemoApp(MDApp):
    def __int__(self, **kwargs):
        super(DemoApp, self).__init__(**kwargs)
    showRightDrawerEventsMenu = BooleanProperty(False)
    showLeftDrawerPlayersMenu = BooleanProperty(False)
    showNavDrawer3BLANKMenu = BooleanProperty(False)
    showSpecificEventDrawerPlayersMenu = BooleanProperty(False)
    showSpecificPlayerPosition = BooleanProperty(False)

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
            # print("*" * 50 )
            # print(self.players_assigned_to_teams)
            # print("Trying to print the table")
            # print(self.table_to_insert)
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
                self.root.ids.display_dark.add_widget(MDLabel(text=f"Dark Goalie: {len(all_current_events[self.current_event_identify]['Dark']['Goalie'])} / 1", halign='center'))
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
                self.root.ids.display_dark.add_widget(MDLabel(text=f"Dark Line 1 Forwards: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Forward'])} / 3 ", halign='center'))
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
                self.root.ids.display_dark.add_widget(MDLabel(text=f"Dark Line 1 Defense: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Defense'])} / 2", halign='center'))
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
                    MDLabel(text=f"Dark Line 2 Forwards: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Forward'])} / 3 ", halign='center'))
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
                    MDLabel(text=f"Dark Line 2 Defense: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Defense'])} / 2", halign='center'))
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
                self.root.ids.display_light.add_widget(MDLabel(text=f"Light Goalie: {len(all_current_events[self.current_event_identify]['Light']['Goalie'])} / 1", halign='center'))
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
                self.root.ids.display_light.add_widget(MDLabel(text=f"Light Line 1 Forwards: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Forward'])} / 3", halign='center'))
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
                self.root.ids.display_light.add_widget(MDLabel(text=f"Light Line 1 Defense: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Defense'])} / 2", halign='center'))
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
                    MDLabel(text=f"Light Line 2 Forwards: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Forward'])} / 3", halign='center'))
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
                    MDLabel(text=f"Light Line 2 Defense: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Defense'])} / 2", halign='center'))
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
        self.root.ids.organize_dark_line2.add_widget(MDLabel(text="Dark Line 2:", halign='center'))
        dark = True
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            if len(all_current_events[self.current_event_identify]["Dark"]["Goalie"]) != 0:
                self.root.ids.organize_dark_line1.add_widget(MDLabel(text=f"Dark Goalie: {len(all_current_events[self.current_event_identify]['Dark']['Goalie'])} / 1", halign='center'))
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
                self.root.ids.organize_dark_line1.add_widget(MDLabel(text=f"Dark Line 1 Forwards: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Forward'])} / 3 ", halign='center'))
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
                self.root.ids.organize_dark_line1.add_widget(MDLabel(text=f"Dark Line 1 Defense: {len(all_current_events[self.current_event_identify]['Dark']['Line1']['Defense'])} / 2", halign='center'))
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
                    MDLabel(text=f"Dark Line 2 Forwards: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Forward'])} / 3 ", halign='center'))
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
                self.root.ids.organize_dark_line2.add_widget(MDLabel(text=f"Dark Line 2 Defense: {len(all_current_events[self.current_event_identify]['Dark']['Line2']['Defense'])} / 2", halign='center'))
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


                        # self.player_card = OrganizeD2Line(text=name, player_id=all_contact_info[single_player - 1].get("playerid"))
                        # self.root.ids.organize_d2_event.add_widget(self.player_card)
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
                self.root.ids.organize_light_line1.add_widget(MDLabel(text=f"Light Goalie: {len(all_current_events[self.current_event_identify]['Light']['Goalie'])} / 1", halign='center'))
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
                self.root.ids.organize_light_line1.add_widget(MDLabel(text=f"Light Line 1 Forwards: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Forward'])} / 3", halign='center'))
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
                self.root.ids.organize_light_line1.add_widget(MDLabel(text=f"Light Line 1 Defense: {len(all_current_events[self.current_event_identify]['Light']['Line1']['Defense'])} / 2", halign='center'))
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
                    MDLabel(text=f"Light Line 2 Forwards: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Forward'])} / 3", halign='center'))
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
                    MDLabel(text=f"Light Line 2 Defense: {len(all_current_events[self.current_event_identify]['Light']['Line2']['Defense'])} / 2", halign='center'))
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

    def showSpecificEventDrawerPlayersMenuModule(self, root):
        print("*")
        print("showSpecificEventDrawerPlayersMenuModule")
        print("*" * 250)
        if self.showSpecificEventDrawerPlayersMenu:
            self.invite = MDRaisedButton(font_style = 'Subtitle2', text='Invite Regulars', on_press= self.inviteregularsbutton, size_hint = (1, None), padding = '10dp',   anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.nav_drawer3_md_list.add_widget(self.invite, 2)
            self.invite2 = MDRaisedButton(font_style = 'Subtitle2', text='Invite Subs', on_press= self.invitesubsbutton, size_hint = (1, None), padding = '10dp',  anchor_x = 'left', md_bg_color = (.2,.53,.733,1))
            root.ids.nav_drawer3_md_list.add_widget(self.invite2, 2)
            self.invite3 = MDRaisedButton(font_style = 'Subtitle2', text='Invite Individual Player', on_press= self.inviteindividualplayer, size_hint = (1, None), padding = '10dp',  anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.nav_drawer3_md_list.add_widget(self.invite3, 2)
            self.secondchild = root.ids.nav_drawer3_md_list.children
        else:
            print(" we are in the showSpecificEventDrawerPlayersMenuModule(self, root): and removing the widgets")
            root.ids.nav_drawer3_md_list.remove_widget(self.invite)
            root.ids.nav_drawer3_md_list.remove_widget(self.invite2)
            root.ids.nav_drawer3_md_list.remove_widget(self.invite3)

    def display_organize_event_screen(self):
        print("*" * 250)
        print("display_oragnize_event_screen")
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
                    self.player_card = OrganizePlayerToTeam(text=name, second_text=positionstring, third_text=randomtext, player_id=a)
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
                        self.dark_forward_line_2 = TryingButtonDark(font_style="Subtitle2", text="Dark Line2 Forward",
                                                                player_id = instance.player_id,
                                                                on_press=self.add_dark_forward_line_2)#TRYING TO ADD instance.player_id
                        self.root.ids.organize_event_label.add_widget(self.dark_forward_line_2, self.button_index)
                        self.light_forward_line_2 = TryingButtonLight(font_style="Subtitle2", text="Light Line2 Forward",
                                                                player_id = instance.player_id,
                                                                on_press=self.add_light_forward_line_2)
                        self.root.ids.organize_event_label.add_widget(self.light_forward_line_2, self.button_index)
                    if "D" in all_contact_info[instance.player_id - 1].get("position F D G"):
                        print("Defense Line 2")
                        self.dark_defense_line_2 = TryingButtonDark(font_style="Subtitle2", text="Dark Line2 Defense",
                                                                player_id=instance.player_id,
                                                                on_press=self.add_dark_defense_line_2)  # TRYING TO ADD instance.player_id
                        self.root.ids.organize_event_label.add_widget(self.dark_defense_line_2, self.button_index)
                        self.light_defense_line_2 = TryingButtonLight(font_style="Subtitle2", text="Light Line2 Defense",
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
        self.display_organize_event_screen()


    # def organize_event_add_to_d1(self, instance):
    #     print("now add to dark id:organize_dark_event")
    #     self.root.ids.organize_event_label.remove_widget(instance)
    #     with open('myevents.json') as allcurrentevents:
    #         all_current_events = json.load(allcurrentevents)
    #         all_current_events[self.current_event_identify]["PlayersIn"].remove(instance.player_id)
    #         all_current_events[self.current_event_identify]["D1"].append(instance.player_id)
    #         with open('myevents.json', 'w') as json_file:
    #             json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
    #         with open('ContactInfo.json') as allcontactinfo:
    #             all_contact_info = json.load(allcontactinfo)
    #             name = all_contact_info[instance.player_id - 1].get("Player First")
    #             name += " " + all_contact_info[instance.player_id - 1].get("Player Last")
    #             self.player_card = OrganizeD1Line(text=name, player_id=instance.player_id)
    #             self.root.ids.organize_d1_event.add_widget(self.player_card)
    # def organize_event_add_to_d2(self, instance):
    #     print("now add to dark id2:organize_dark_event")
    #     self.root.ids.organize_event_label.remove_widget(instance)
    #     with open('myevents.json') as allcurrentevents:
    #         all_current_events = json.load(allcurrentevents)
    #         all_current_events[int(self.current_event_identify)]["PlayersIn"].remove(instance.player_id)
    #         all_current_events[int(self.current_event_identify)]["D2"].append(instance.player_id)
    #         with open('myevents.json', 'w') as json_file:
    #             json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
    #         with open('ContactInfo.json') as allcontactinfo:
    #             all_contact_info = json.load(allcontactinfo)
    #             name = all_contact_info[instance.player_id - 1].get("Player First")
    #             name += " " + all_contact_info[instance.player_id - 1].get("Player Last")
    #             self.player_card = OrganizeD2Line(text=name, player_id=instance.player_id)
    #             self.root.ids.organize_d2_event.add_widget(self.player_card)
    # def organize_event_add_to_l1(self, instance):
    #     print("now add to light id:organize_light_event")
    #     self.root.ids.organize_event_label.remove_widget(instance)
    #     with open('myevents.json') as allcurrentevents:
    #         all_current_events = json.load(allcurrentevents)
    #         all_current_events[int(self.current_event_identify)]["PlayersIn"].remove(instance.player_id)
    #         all_current_events[int(self.current_event_identify)]["L1"].append(instance.player_id)
    #         with open('myevents.json', 'w') as json_file:
    #             json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
    #         with open('ContactInfo.json') as allcontactinfo:
    #             all_contact_info = json.load(allcontactinfo)
    #             name = all_contact_info[instance.player_id - 1].get("Player First")
    #             name += " " + all_contact_info[instance.player_id- 1].get("Player Last")
    #             self.player_card = OrganizeL1Line(text=name, player_id=instance.player_id)
    #             self.root.ids.organize_l1_event.add_widget(self.player_card)
    # def organize_event_add_to_l2(self, instance):
    #     print("now add to light id:organize_light_event")
    #     self.root.ids.organize_event_label.remove_widget(instance)
    #     with open('myevents.json') as allcurrentevents:
    #         all_current_events = json.load(allcurrentevents)
    #         all_current_events[int(self.current_event_identify)]["PlayersIn"].remove(instance.player_id)
    #         all_current_events[int(self.current_event_identify)]["L2"].append(instance.player_id)
    #         with open('myevents.json', 'w') as json_file:
    #             json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
    #         with open('ContactInfo.json') as allcontactinfo:
    #             all_contact_info = json.load(allcontactinfo)
    #             name = all_contact_info[instance.player_id - 1].get("Player First")
    #             name += " " + all_contact_info[instance.player_id- 1].get("Player Last")
    #             self.player_card = OrganizeL2Line(text=name, player_id=instance.player_id)
    #             self.root.ids.organize_l2_event.add_widget(self.player_card)

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
                                                              search_player_id=str(singlecontact['playerid']),
                                                              # search_player_first = str(singlecontact['Player First']),
                                                              # search_player_last = str(singlecontact['Player Last']),
                                                              # search_player_cell_number = str(singlecontact['Cell Number']),
                                                              # search_player_email = str(singlecontact['Email']),
                                                              # search_player_position = str(singlecontact['position F D G']),
                                                              # search_player_line = str(singlecontact['LINE']),
                                                              # search_player_tuesday = str(singlecontact['Tuesday']),
                                                              # search_player_friday = str(singlecontact['Friday']),
                                                              # search_player_sunday = str(singlecontact['Sunday']),
                                                              # search_player_monies = str(singlecontact['Monies']),
                                                              # search_player_out = str(singlecontact['OUT']),
                                                              # search_player_suspended = str(singlecontact['Suspended']),
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
            print("*" * 300)
            specific_message = f'{self.current_event_day}Reg'
            print(specific_message)
            txt = str(all_standard_messages[specific_message])
            print(txt)
            txt = txt.replace("insert_date", str(self.dict_of_event.get("Date")))
            print(txt)
            #print(all_standard_messages[0].get(specific_message))
            print("Printing Specific Message")
            # specific_message = all_standard_messages.get(specific_message)
            self.root.ids.quick_event_text.text = txt
        with open('ContactInfo.json') as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            for a in all_contact_info:
                #print(a)
                if a["playerid"] in self.current_event_players_invited:
                    print("already invited")
                else:
                    if a[self.current_event_day] == 'Z':
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
            specific_message = f'{self.current_event_day}Sub'
            print(specific_message)
            txt = str(all_standard_messages[1].get(specific_message))
            txt = txt.replace("insert_date", str(self.dict_of_event.get("Date")))
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
                    if a[self.current_event_day] == 'Z':
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
    def inviteregularssendemail(self):
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
                    if a not in all_current_events[int(self.current_event_identify)].get("PlayersInvited") \
                            and a not in all_current_events[int(self.current_event_identify)].get("D1") \
                            and a not in all_current_events[int(self.current_event_identify)].get("D2") \
                            and a not in all_current_events[int(self.current_event_identify)].get("L1") \
                            and a not in all_current_events[int(self.current_event_identify)].get("L2") \
                            and a not in all_current_events[int(self.current_event_identify)].get("PlayersIn"):
                        all_current_events[int(self.current_event_identify)].get("PlayersInvited").append(a)
                        TestingIndividualLogicCode.alerts.email_alert(self.email_dict_of_player.get("Email"), "Test Email",
                                                                      self.root.ids.quick_event_text.text)
                        with open('myevents.json', 'w') as json_file:
                            json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                            print("Just dumped the info")
                            print(all_current_events[int(self.current_event_identify)]["PlayersInvited"])
                    else:
                        print("Player Already Invited")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                for a in all_current_events[int(self.current_event_identify)]["PlayersInvited"]:
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
                    if a not in all_current_events[int(self.current_event_identify)].get("PlayersInvited") \
                            and a not in all_current_events[int(self.current_event_identify)].get("D1") \
                            and a not in all_current_events[int(self.current_event_identify)].get("D2") \
                            and a not in all_current_events[int(self.current_event_identify)].get("L1") \
                            and a not in all_current_events[int(self.current_event_identify)].get("L2") \
                            and a not in all_current_events[int(self.current_event_identify)].get("PlayersIn"):
                        all_current_events[int(self.current_event_identify)].get("PlayersInvited").append(a)
                        TestingIndividualLogicCode.alerts.email_alert(self.email_dict_of_player.get("Email"), "Test Email",
                                                                      self.root.ids.quick_event_text.text)
                        with open('myevents.json', 'w') as json_file:
                            json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                            print("Just dumped the info")
                            print(all_current_events[int(self.current_event_identify)]["PlayersInvited"])
                    else:
                        print("Player Already Invited")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                for a in all_current_events[int(self.current_event_identify)]["PlayersInvited"]:
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
                    if a not in all_current_events[int(self.current_event_identify)].get("PlayersInvited") \
                            and a not in all_current_events[int(self.current_event_identify)].get("D1") \
                            and a not in all_current_events[int(self.current_event_identify)].get("D2") \
                            and a not in all_current_events[int(self.current_event_identify)].get("L1") \
                            and a not in all_current_events[int(self.current_event_identify)].get("L2") \
                            and a not in all_current_events[int(self.current_event_identify)].get("PlayersIn"):
                        all_current_events[int(self.current_event_identify)].get("PlayersInvited").append(a)
                        TestingIndividualLogicCode.alerts.email_alert(self.email_dict_of_player.get("Email"),
                                                                     "Test Email",
                                                                      self.root.ids.quick3_event_text.text)
                        with open('myevents.json', 'w') as json_file:
                            json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                            print("Just dumped the info")
                            print(all_current_events[int(self.current_event_identify)]["PlayersInvited"])
                    else:
                        print("Player Already Invited")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            with open('ContactInfo.json') as allcontactinfo:
                all_contact_info = json.load(allcontactinfo)
                for a in all_current_events[int(self.current_event_identify)]["PlayersInvited"]:
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
        self.example = root.ids
        # print(self.example)
        # print('just printed self.example')
        self.add_event_on_submit()
        self.clear_create_event_textfields()
        self.current_events_displayed()

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
        self.fdate = self.date[0:2] + '/' + self.date[2:4] + '/' + self.date[4:6]
        self.AMPM = self.time[4:6]
        self.AMPM = self.AMPM.upper()
        self.ftime = self.time[0:2] + ':' + self.time[2:4] + ' ' + self.AMPM
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
        listobj[self.eventid] = new_event_dict
        # listobj.append({
        #     "EventID": self.eventid,
        #     "Date": self.fdate,
        #     "Day": self.day,
        #     "Time": self.ftime,
        #     "Location": self.flocation,
        #     "Cost": self.cost,
        #     "TotalPlayers": self.totalplayers,
        #     "PlayersIn": [],
        #     "PlayersInvited": [],
        #     "PlayersPaid": [],
        #     "D1": [],
        #     "D2": [],
        #     "L1": [],
        #     "L2": [],
        #     "Status": "Current",
        # }
        # )
        #print(listobj)
        #listobj[0]["TotalEventCount"] += 1
        with open('myevents.json', 'w') as json_file:
            json.dump(listobj, json_file, indent=4, separators=(',', ':'))

    def quickevent(self, id):
        print("quickevent MODULE")
        with open('quickevents.json') as f:
            listobj = json.load(f)
            for quickbutton in listobj:
                # print(quickbutton)
                self.here = (quickbutton.get("ID", "NONE"))
                # print(self.here)
                # print(id)
                if str(self.here) == str(id):
                    print("in the quickevent module")
                    print(self.here)
                    print(id)
                    self.root.ids.time.text = str(quickbutton.get("Time"))
                    self.root.ids.location.text = quickbutton.get("Location")
                    self.root.ids.cost.text = quickbutton.get("Cost")
                    self.root.ids.totalplayers.text = quickbutton.get("TotalPlayers")
                    self.root.ids.day.text = quickbutton.get("Day")
            # listobj[0]['TotalEventCount'] += 1
            # self.eventid = listobj[0]['TotalEventCount']
            # for piece in listobj:
            #     print(len(piece))
            #     print(piece.get('EventID', "None"))
            #     print('just printed piece')
            #     for i in piece:
            #         print(piece[i])
            #         print("Printing i in piece")

    def current_events_displayed(self):
        print("In the current_events_displayed Module")
        with open('myevents.json') as myevents:
            alleventslist = json.load(myevents)
            for allevent in alleventslist:
                if allevent != "TotalEventCount":
                    eventid = allevent
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
                    event_card = SwipeToDeleteItem2(text2=f'{date} {day} {location} {time}',
                                                       second_text2=f'Cost: {cost} ~ Players: {playersin}/{totalplayers}',
                                                       third_text2= f"INV: {len(alleventslist[allevent]['PlayersInvited'])} ~ TO ASSIGN: {len(alleventslist[allevent]['PlayersIn'])}",
                                                        event_id2 = str(eventid))

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

    def on_swipe_complete(self, instance):
        print("on_swipe_complete MODULE")
        print(dir(instance))
        print(instance)
        self.root.ids.md_list.remove_widget(instance)
        self.root.ids.screen_manager.current = 'CurrentEventsPage'

    def clear_specific_event(self):
        print("clear_specific_event MODULE")
        self.root.ids.specific_event_page_box_layout.clear_widgets()
        self.root.ids.specific_event_label.clear_widgets()

    def on_swipe_complete2(self, instance):
        print("on_swipe_complete2 MODULE")
        print("In on swipe 2 complete: " + str(instance.event_id2))
        self.root.ids.currentevents_md_list.clear_widgets()
        self.clear_specific_event()
        self.current_event_identify = instance.event_id2

        with open('myevents.json') as myevents:
            alleventslist = json.load(myevents)
            self.dict_of_event = alleventslist[instance.event_id2]
            self.current_event_players_invited = self.dict_of_event.get("PlayersInvited")
            print("TRYING TO PRINT THE LIST OF CURRENT PLAYERS INVITED")
            print(self.current_event_players_invited)
            #print(self.dict_of_event)
            self.current_event_day = self.dict_of_event.get('Day')
            labeltext = f" {self.dict_of_event.get('Date')}"
            labeltext += f" {self.dict_of_event.get('Day')}"
            labeltext += f" {self.dict_of_event.get('Location')}"
            labeltext += f" {self.dict_of_event.get('Time')}"
            labeltext += f"\nInvited: {len(self.dict_of_event.get('PlayersInvited'))}"
            labeltext += f" ~ To Assign: {len(self.dict_of_event.get('PlayersIn'))}"
            labeltext += f" ~ Goalies: {len(self.dict_of_event['Dark'].get('Goalie')) + len(self.dict_of_event['Light'].get('Goalie'))} \n" \
                         f"Dark: {len(self.dict_of_event['Dark']['Line1'].get('Forward')) + len(self.dict_of_event['Dark']['Line1'].get('Defense')) + len(self.dict_of_event['Dark']['Line2'].get('Forward')) + len(self.dict_of_event['Dark']['Line2'].get('Defense')) }" \
                         f" ~ Light: {len(self.dict_of_event['Light']['Line1'].get('Forward')) + len(self.dict_of_event['Light']['Line1'].get('Defense')) + len(self.dict_of_event['Light']['Line2'].get('Forward')) + len(self.dict_of_event['Light']['Line2'].get('Defense')) }"
            specific_event_heading_label = MDLabel(text=labeltext, halign='center')
            self.root.ids.specific_event_page_box_layout.add_widget(specific_event_heading_label)
        with open('ContactInfo.json') as allcontactinfo:
            all_contact_info = json.load(allcontactinfo)
            for a in self.dict_of_event.get("PlayersInvited"):
                print(all_contact_info[a-1])
                namestring = "Name: "
                namestring += f"{all_contact_info[a-1].get('Player First')}"
                namestring += " " + f"{all_contact_info[a-1].get('Player Last')}"
                positionstring = "Pos: "
                positionstring += f'{all_contact_info[a-1].get("position F D G")}'
                positionstring += "  Line: "
                positionstring += f'{all_contact_info[a-1].get("LINE")}'
                player_id = int(all_contact_info[a-1].get("playerid"))
                print(namestring)
                player_card = SwipeToAddPlayerToInList(text=namestring,
                                                       second_text=positionstring,
                                                       event_id=self.current_event_identify,
                                                       player_id=player_id
                                                       )
                self.root.ids.specific_event_label.add_widget(player_card)
            # for a in str(singleevent.get(["PlayersIn"])):
            #     print(int(a))
        self.root.ids.screen_manager.current = 'SpecificEventPage'

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
                            button = MDLabel(text=textstring, halign='center')
                            self.root.ids.specific_found_player_md_list.add_widget(button)
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
        self.root.ids.list_of_individuals_display.clear_widgets()
        TestingIndividualLogicCode.testingfunctions.remove_nav_drawer_3_widgets(self)
        with open('standardmessages.json') as allstandardmessages:
            all_standard_messages = json.load(allstandardmessages)
            print(all_standard_messages)
            specific_message = f'{self.current_event_day}Sub'
            print(specific_message)
            txt = str(all_standard_messages[1].get(specific_message))
            print(txt)
            txt = txt.replace("insert_date", str(self.dict_of_event.get("Date")))
            print(txt)
            print("Printing Specific Message")
            print(str(self.dict_of_event.get("Date")))
            print("Date of dict of event")
            #print(all_standard_messages[0].get(specific_message))

            # specific_message = all_standard_messages.get(specific_message)
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

    def showRightDrawerEvents(self, root):
        print("showRightDrawerEvents MODULE")
        if self.showRightDrawerEventsMenu:
            self.button = MDRaisedButton(font_style = 'Subtitle2', text='Current Events', on_press= self.showcurrentevent, size_hint = (1, None), padding = '10dp',   anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.right_md_list.add_widget(self.button, 1)
            self.button2 = MDRaisedButton(font_style = 'Subtitle2', text='Completed Events', on_press= self.showcompletedevent, size_hint = (1, None), padding = '10dp',  anchor_x = 'left', md_bg_color = (.87,.36,.24,1))
            root.ids.right_md_list.add_widget(self.button2, 1)
            self.secondchild = root.ids.right_md_list.children
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
        # self.root.ids.right_md_list.remove_widget(self.button)
        # self.root.ids.right_md_list.remove_widget(self.button2)
        # self.root.ids.showRightDrawerEventsMenu = not self.root.showRightDrawerEventsMenu
        #
        # event_card = SwipeToDeleteItem(text=f'Date: {date} Time: {time}',
        #                                             second_text=f'Location: {location}',
        #                                             third_text=f'Cost: {cost} Players: 0/{totalplayers}')
        # root.ids.md_list.add_widget(event_card)
        # id = currentevents_md_list

    def showcompletedevent(self, root):
        print("showcompletedevent MODULE")
        self.root.ids.right_md_list.remove_widget(self.button)
        self.root.ids.right_md_list.remove_widget(self.button2)
        self.showRightDrawerEventsMenu = not self.showRightDrawerEventsMenu
        print("showcompletedevent pressed also")

    def clear_current_events(self):
        print("clear_current_events MODULE")
        self.root.ids.currentevents_md_list.clear_widgets()

    def remove_player_invited_add_player_in(self, file, event_id, player_id):
        print("in the specific event heading label")
        with open('myevents.json') as allcurrentevents:
            all_current_events = json.load(allcurrentevents)
            all_current_events[event_id].get("PlayersInvited").remove(player_id)
            all_current_events[event_id].get("PlayersIn").append(player_id)
            #self.dict_of_event = all_current_events[event_id]
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
        self.showLeftDrawerPlayersMenu = not self.showLeftDrawerPlayersMenu
        print("in the search players module")
        for md_text_field in self.root.ids.search_fields.children:
            md_text_field.text = ""
        self.root.ids.screen_manager.current = 'SearchPlayerScreen'
        self.root.ids.nav_drawer.set_state('close')

    def searchplayers(self):
        print("searchplayers MODULE")
        searchplayerlist = ["Player First", "Player Last", "Cell Number", "Email", "position F D G", "LINE"]
        print("start criteria seach and display player cards")
        textfields = [md_text_field.text for md_text_field in self.root.ids.search_fields.children]
        print(textfields)
        searchdictionary = dict(zip(searchplayerlist,reversed(textfields)))
        print(searchdictionary)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ just printed searchdictionary")
        with open('ContactInfo.json') as contactinfo:
            allcontactinfo = json.load(contactinfo)
            print(allcontactinfo)
            for singlekey in searchdictionary:
                for singlecontact in allcontactinfo:
                    if singlekey != "position F D G" and singlecontact.get(singlekey) != "" and singlecontact.get(singlekey) == searchdictionary.get(singlekey):
                            #singlecontact.get(singlekey).find(searchdictionary.get(singlekey)) != -1:
                        print("IM IN HERE")
                        playerfirst = singlecontact['Player First']
                        playerlast = singlecontact['Player Last']
                        playercell = singlecontact['Cell Number']
                        playeremail = singlecontact['Email']
                        searchhit = singlecontact[str(singlekey)]
                        player_card = SwipeToDeletePlayerCard(text3=f'SEARCH: {searchhit}',
                                                              second_text3=f'{playerfirst} {playerlast}',
                                                              third_text3=f'{playercell} {playeremail}',
                                                              search_player_id = str(singlecontact['playerid']),
                                                              )
                        self.root.ids.found_player_md_list.add_widget(player_card)
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
                            player_card = SwipeToDeletePlayerCard(text3=f'SEARCH: {searchhit}',
                                                                  second_text3=f'{playerfirst} {playerlast}',
                                                                  third_text3=f'{playercell} {playeremail}',
                                                                  search_player_id=str(singlecontact['playerid']),
                                                                  )
                            self.root.ids.found_player_md_list.add_widget(player_card)

        self.root.ids.screen_manager.current = 'FoundPlayerScreen'

    def saveeditfromsearchplayer(self):
        print("saveeditfromsearchplayer MODULE")
        print("here is where the .json save needs to go")
        foundplayerlist = ["playerid", "Player First", "Player Last", "Cell Number", "Email",
                            "position F D G", "LINE", "Tuesday", "Friday", "Sunday", "Monies", "Out", "Suspended"]
        md_text_fields2 = [md_text_field.text for md_text_field in self.root.ids.specific_found_player_md_list.children]
        insertdictionary = dict(zip(foundplayerlist,reversed(md_text_fields2)))
        insertdictionary['playerid'] = int(self.search_player_id)
        print(insertdictionary)
        print("just printed the dictionary to insert")
        with open('ContactInfo.json') as contactinfo:
            self.allcontactinfo = json.load(contactinfo)
            #fileplayersave = self.allcontactinfo[self.index_of_player]
            self.allcontactinfo[self.index_of_player] = insertdictionary
            with open('ContactInfo.json', 'w') as json_file:
                json.dump(self.allcontactinfo, json_file, indent=4, separators=(',', ':'))
        for empty_search_field in self.root.ids.search_fields.children:
            empty_search_field.text = ""
        self.change_home_screen()

    def clear_search_text_fields(self):
        pass

    def createplayer(self, root):
        print("in the create player module")
        print("coming from clicking the player - create player button on left nav menu")
        self.root.ids.left_md_list.remove_widget(self.playerbutton)
        self.root.ids.left_md_list.remove_widget(self.playerbutton2)
        self.showLeftDrawerPlayersMenu = not self.showLeftDrawerPlayersMenu
        for md_text_field in self.root.ids.create_player_fields.children:
            md_text_field.text = ""
        self.root.ids.screen_manager.current = 'CreatePlayerScreen'
        self.root.ids.nav_drawer.set_state('close')

    def save_create_player(self, root):
        print("we just came from the CreatePlayerScreen")
        print("just clicked the CREATE PLAYER button")
        print("in the save_create_player module")
        foundplayerlist = ["Player First", "Player Last", "Cell Number", "Email",
                           "position F D G", "LINE", "Tuesday", "Friday", "Sunday", "Monies", "Out", "Suspended"]
        md_text_fields2 = [md_text_field.text for md_text_field in self.root.ids.create_player_fields.children]
        insertdictionary = dict(zip(foundplayerlist, reversed(md_text_fields2)))
        for a in md_text_fields2:
            print(a)
        with open("ContactInfo.json") as allcontactinfo:
            self.all_contact_info = json.load(allcontactinfo)
            player_id = int(len(self.all_contact_info)) + 1
            print(player_id)
            insertdictionary['playerid'] = player_id
            self.all_contact_info.append(insertdictionary)
            print(self.all_contact_info)
            with open('ContactInfo.json', 'w') as json_file:
                json.dump(self.all_contact_info, json_file, indent=4, separators=(',', ':'))
        for md_text_field in self.root.ids.create_player_fields.children:
            md_text_field.text = ""

    def just_testing(self):
        TestingIndividualLogicCode.makingtable.testing_key_word_args("testing", "self", "printing")

    def clear_search_players(self):
        print("clear_search_players MODULE")
        self.root.ids.player_md_list.clear_widgets()


    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()
