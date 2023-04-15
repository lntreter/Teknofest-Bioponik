from kivymd.app import MDApp    
from kivy.lang  import Builder  
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screen import MDScreen
import time

# with open('Uygulama\deneme.txt', 'r') as f:
#     global ilk_satir
#     ilk_satir = f.readline()

class CircularElevationButton(
    CommonElevationBehavior,
    CircularRippleBehavior,
    ButtonBehavior,
    MDFloatLayout,
):
    pass

class Content(BoxLayout):
    pass

class DEMO(ScreenManager):
    pass

class Main(MDApp):
    title = StringProperty("")  
    
    def close_dialog(self, obj):
        
        my_dialog.dismiss()
    
    def show_sysinfo_dialog(self):
        global my_dialog
        my_dialog = MDDialog(title="Sistem Durumu", text="Sistem şu anda domates yetiştirecek şekilde ayarlanmış durumda.", 
                             size_hint=(0.5, .5),elevation=0,md_bg_color=(.85, 1, 0.8, 1),buttons=[MDFlatButton(text="Tamam",on_release=self.close_dialog)])
        my_dialog.open()
    
    def build(self):

        Window.size = (1024, 600)
        self.check_file()
        Builder.load_string('''
    
<CircularElevationButton>
    size_hint: None, None
    size: "500dp", "55dp"
    radius: self.size[0] / 18
    shadow_radius: self.radius[0]
    # md_bg_color: (.539,.929,.539,1)
    md_bg_color: (0,1,.506,1)    #(.036,1,.32,1)

<Content>:
    ScrollView:
        scroll_type: ['bars']
        bar_color: [0,1,0,1]
        MDList:
                
            OneLineIconListItem:
                text: "Ana Ekran"
                on_release: 
                    app.root.ids.screen_manager.current = "screen 1"
                IconLeftWidget:
                    icon: "home"
            OneLineIconListItem:
                text: "Isı ve Nem"
                on_release: 
                    root.ids.screen_manager.current = "screen 2"
                IconLeftWidget:
                    icon: "thermometer-water"
                
<DEMO>:
    MDScreen:
        md_bg_color: (.95, 1, 0.9, 1)

        MDTopAppBar:
            title: app.title
            elevation: 3
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            md_bg_color: (0,1,.506,1) #(.036,1,.32,1)
            pos_hint: {"top": 1}
        
        MDLabel:
            text: "EKOKAKT - M1"
            color:"white"
            pos_hint: {"center_x": .57  , "center_y": .943}
            font_size: 30     
        
        MDNavigationLayout:
            ScreenManager:
                id: screen_manager
                Screen:
                    name: "screen 1"
                    
                    FloatLayout:
                    
                    
                        MDCard:
                            id: card3
                            md_bg_color: [.78, .91, .78, 1]
                            size_hint: 0.25, 0.32
                            pos_hint: {'center_x': 0.8,'center_y': 0.435}
                            elevation: 1.3
                            
                            Image:
                                id: info
                                source: "logo1.png"
                                size_hint: 1,1
                                pos_hint: {'center_x': 0.5,'center_y': 0.5}
                  
                        MDCard:
                            id: card1
                            md_bg_color: [.78, .91, .78, 1]
                            size_hint: 0.15, 0.15
                            pos_hint: {'center_x': 0.7,'center_y': 0.72}
                            elevation: 1.5
                            
                            FloatLayout:
                                
                                Label:
                                    text: "SICAKLIK"
                                    color: (.67, 0.38, 0.407, 1)
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                                
                                MDRectangleFlatIconButton:
                                    icon: "thermometer"
                                    text: '98°'
                                    font_size: 35
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.35}
                                    line_color: (0, 0, 0, 0)
                                    icon_color: (.67, 0.38, 0.407, 1)
                                    text_color: (.67, 0.38, 0.407, 1)
                        MDCard:
                            id: card2
                            md_bg_color: [.78, .91, .78, 1]
                            size_hint: 0.15, 0.15
                            pos_hint: {'center_x': 0.89,'center_y': 0.72}
                            elevation: 1.5
                            
                            FloatLayout:
                                
                                Label:
                                    text: "NEM"
                                    color: (.4, 0.595, 0.94, 1)
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                                    
                                MDRectangleFlatIconButton:
                                    icon: "water"
                                    text: '%50'
                                    font_size: 35
                                    pos_hint: {'center_x': 0.5  , 'center_y': 0.35}
                                    line_color: (0, 0, 0, 0)
                                    icon_color: (.4, 0.595, 0.94, 1)
                                    text_color: (.4, 0.595, 0.94, 1)
                                       
                        CircularElevationButton:
                            id: button1
                            pos_hint: {'center_x': 0.33, 'center_y': 0.75}
                            elevation: 2
                            shadow_offset: 0, 6
                            on_press: print("Button 1 pressed")
                            on_release:
                                app.root.ids.info.source = "tomato.png"
                                app.root.ids.screen_manager.current = "screen 3"

                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: None, None
                                size: dp(150), dp(80)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: 'D o m a t e s'
                                    halign: 'center'
                                    font_size: 30
                                    theme_text_color: 'Custom'
                                    text_color: "white"      
                                                       
                        # MDRoundFlatButton:
                        #     id: button1
                        #     text: 'Domates'
                        #     elevation: 20
                        #     text_color: (.018,.482,.42,1)
                        #     line_color: (.018,.482,.42,1)
                        #     md_bg_color: (0, 0, 0, 0)
                        #     on_press: print("Button 1 pressed")
                        #     on_release: app.root.ids.screen_manager.current = "screen 3"
                        #     size_hint: 0.5, 0.1
                        #     pos_hint: {'center_x': 0.33, 'center_y': 0.75}
                        
                        CircularElevationButton:
                            id: button2
                            pos_hint: {'center_x': 0.33, 'center_y': 0.6}
                            elevation: 2
                            shadow_offset: 0, 6
                            on_press: print("Button 2 pressed")
                            on_release: 
                                app.root.ids.screen_manager.current = "screen 4"
                                app.root.ids.info.source = "may.png"

                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: None, None
                                size: dp(150), dp(80)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: 'B i b e r'
                                    halign: 'center'
                                    font_size: 30
                                    theme_text_color: 'Custom'
                                    text_color: "white"
                            
                        # MDRoundFlatButton:
                        #     id: button2
                        #     text: '2'
                        #     text_color: (.018,.482,.42,1)
                        #     line_color: (.018,.482,.42,1)
                        #     color: (0, 1, 0.4, 1)
                        #     on_press: print("Button 2 pressed")
                        #     on_release: app.root.ids.screen_manager.current = "screen 4"
                        #     size_hint: 0.5, 0.1
                        #     pos_hint: {'center_x': 0.33, 'center_y': 0.6}
                        
                        CircularElevationButton:
                            id: button3
                            pos_hint: {'center_x': 0.33, 'center_y': 0.45}
                            elevation: 2
                            shadow_offset: 0, 6
                            on_press: print("Button 3 pressed")
                            on_release: app.root.ids.screen_manager.current = "screen 5"

                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: None, None
                                size: dp(150), dp(80)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: 'S o ğ a n'
                                    halign: 'center'
                                    font_size: 30
                                    theme_text_color: 'Custom'
                                    text_color: "white"
                
                        # MDRoundFlatButton:
                        #     id: button3
                        #     text: '3'
                        #     text_color: (.018,.482,.42,1)
                        #     line_color: (.018,.482,.42,1)
                        #     on_press: print("Button 3 pressed")
                        #     on_release: app.root.ids.screen_manager.current = "screen 5"
                        #     background_color: (0, 1, 0, 1)
                        #     size_hint: 0.5, 0.1
                        #     pos_hint: {'center_x': 0.33, 'center_y': 0.45}
                        
                        CircularElevationButton:
                            id: button4
                            pos_hint: {'center_x': 0.33, 'center_y': 0.3}
                            elevation: 2
                            shadow_offset: 0, 6
                            on_press: print("Button 4 pressed")
                            on_release: app.root.ids.screen_manager.current = "screen 6"

                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: None, None
                                size: dp(150), dp(80)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: 'S o ğ a n'
                                    halign: 'center'
                                    font_size: 30
                                    theme_text_color: 'Custom'
                                    text_color: "white"
                            
                        # MDRoundFlatButton:
                        #     id: button3
                        #     text: '4'
                        #     text_color: (.018,.482,.42,1)
                        #     line_color: (.018,.482,.42,1)
                        #     on_press: print("Button 4 pressed")
                        #     on_release: app.root.ids.screen_manager.current = "screen 6"
                        #     background_color: (0, 1, 0, 1)
                        #     size_hint: 0.5, 0.1
                        #     pos_hint: {'center_x': 0.33, 'center_y': 0.3}
                        
                        CircularElevationButton:
                            id: button5
                            pos_hint: {'center_x': 0.33, 'center_y': 0.15}
                            elevation: 2
                            shadow_offset: 0, 6
                            on_press: print("Button 5 pressed")
                            on_release: app.root.ids.screen_manager.current = "screen 7"

                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: None, None
                                size: dp(150), dp(80)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: 'S o ğ a n'
                                    halign: 'center'
                                    font_size: 30
                                    theme_text_color: 'Custom'
                                    text_color: "white"
                            
                        # MDRoundFlatButton:
                        #     id: button3
                        #     text: '5'
                        #     text_color: (.018,.482,.42,1)
                        #     line_color: (.018,.482,.42,1)
                        #     on_press: print("Button 5 pressed")
                        #     on_release: app.root.ids.screen_manager.current = "screen 7"
                        #     background_color: (0, 1, 0, 1)
                        #     size_hint: 0.5, 0.1
                        #     pos_hint: {'center_x': 0.33, 'center_y': 0.15}
                            
                    MDIconButton:
                        icon: "information"
                        theme_icon_color: "Custom"
                        icon_color: (.018,.482,.42,1)
                        on_release: app.show_sysinfo_dialog()
                        pos_hint: {'center_x': 0.7,'center_y': 0.553}
                            
                Screen:
                    name: "screen 2"
                    MDLabel:
                        text: "screen 2"
                        color:
                        halign: "center"
                        
                Screen:
                    name: "screen 3"
                    MDLabel:
                        text: "screen 3"
                        color:
                        halign: "center"
                       
                    MDIconButton:
                        id: back1
                        icon: "arrow-left"
                        theme_icon_color: "Custom"
                        on_press: print("back1 pressed")
                        on_release: app.root.ids.screen_manager.current = "screen 1"
                        md_bg_color: (0,1,.506,1) 
                        size_hint: .075, .1
                        pos_hint: {'center_x': 0.08, 'center_y': 0.1}
                        
                Screen:
                    name: "screen 4"
                    MDLabel:
                        text: "screen 4"
                        color:
                        halign: "center"
                        
                    MDIconButton:
                        id: back2
                        icon: "arrow-left"
                        icon_color: "white"
                        on_press: print("back2 pressed")
                        on_release: app.root.ids.screen_manager.current = "screen 1"
                        md_bg_color: (0,1,.506,1) 
                        size_hint: .075, .1
                        pos_hint: {'center_x': 0.08, 'center_y': 0.1}
                
                Screen:
                    name: "screen 5"
                    MDLabel:
                        text: "screen 5"
                        color:
                        halign: "center"
                        
                    MDIconButton:
                        id: back3
                        icon: "arrow-left"
                        icon_color: "white"
                        on_press: print("back3 pressed")
                        on_release: app.root.ids.screen_manager.current = "screen 1"
                        md_bg_color: (0,1,.506,1) 
                        size_hint: .075, .1
                        pos_hint: {'center_x': 0.08, 'center_y': 0.1}
                        
                Screen:
                    name: "screen 6"
                    MDLabel:
                        text: "screen 6"
                        color:
                        halign: "center"
                        
                    MDIconButton:
                        id: back4
                        icon: "arrow-left"
                        icon_color: "white"
                        on_press: print("back4 pressed")
                        on_release: app.root.ids.screen_manager.current = "screen 1"
                        md_bg_color: (0,1,.506,1) 
                        size_hint: .075, .1
                        pos_hint: {'center_x': 0.08, 'center_y': 0.1}
                        
                Screen:
                    name: "screen 7"
                    MDLabel:
                        text: "screen 7"
                        color:
                        halign: "center"
                        
                    MDIconButton:
                        id: back5
                        icon: "arrow-left"
                        icon_color: "white"
                        on_press: print("back5 pressed")
                        on_release: app.root.ids.screen_manager.current = "screen 1"
                        md_bg_color: (0,1,.506,1) 
                        size_hint: .075, .1
                        pos_hint: {'center_x': 0.08, 'center_y': 0.1}
                    
                    
                
                
            MDNavigationDrawer:
                id: nav_drawer
                md_bg_color: (0.8, 1, 0.8, 1)
                Content:
            
            ''')
                          
        Clock.schedule_interval(self.update_title, 5)  
        
        return DEMO()
    
    def check_file(self):
        with open('Uygulama/deneme.txt', 'r') as f:
            self.title = f.readline().strip()
            
    def update_title(self, *args):
        with open('Uygulama/deneme.txt', 'r') as f:
            new_title = f.readline().strip()
            if self.title != new_title:
                self.title = new_title
    
    
if __name__ == '__main__':
    Main().run()