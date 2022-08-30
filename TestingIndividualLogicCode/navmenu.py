def closeLeftDrawerQuickButtons(self, root):
    self.root.ids.nav_drawer.set_state('close')
    self.root.ids.left_md_list.remove_widget(self.addquickeventbutton)
    self.root.ids.left_md_list.remove_widget(self.addquickeventbutton2)
    self.root.ids.left_md_list.remove_widget(self.addquickeventbutton3)