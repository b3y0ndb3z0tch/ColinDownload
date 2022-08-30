def remove_nav_drawer_3_widgets(self):
    print("*")
    print( " in the remove_nav_drawer_3_widgets(self) of the inviteindividualplayer(self, root) function")
    self.root.ids.nav_drawer3_md_list.remove_widget(self.invite)
    self.root.ids.nav_drawer3_md_list.remove_widget(self.invite2)
    self.root.ids.nav_drawer3_md_list.remove_widget(self.invite3)
