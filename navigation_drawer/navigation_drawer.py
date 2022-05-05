navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [['face-profile', lambda x: nav_drawer2.set_state('open')]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'BAHimages/BAHlogo.jpeg'
                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                        MDRaisedButton:               
                            text: 'Create Event'
                            font_style: 'Subtitle1'
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            height: '75dp'
                            on_press:
                                print('button was pressed')
                        MDRaisedButton:
                            text: 'Create Player'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('button was pressed')
                        MDRaisedButton:
                            text: 'Another Button For Adding'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('button was pressed')
        MDNavigationDrawer:
            id: nav_drawer2
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'BAHimages/BAHlogo.jpeg'
                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                        MDRaisedButton:               
                            text: 'My Events'
                            font_style: 'Subtitle1'
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            height: '75dp'
                            on_press:
                                print('button was pressed')
                        MDRaisedButton:
                            text: 'My Contacts'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('button was pressed')
                        MDRaisedButton:
                            text: 'Another Button For Adding'
                            font_style: 'Subtitle1'
                            size_hint_x: None
                            size_x: self.parent.width
                            pos_hint: {"center_x": .5}
                            size_hint: (1, None)
                            on_press:
                                print('button was pressed')                      
"""