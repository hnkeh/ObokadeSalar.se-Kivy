# coding=utf-8
import kivy
kivy.require('1.0.5')
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from timescraper import *
from houselists import *
from kivy.uix.screenmanager import ScreenManager, Screen

class PopupBox(Popup):
    pop_up_text = ObjectProperty()
    def update_pop_up_text(self, p_message):
        self.pop_up_text.text = p_message

class Controller(FloatLayout):

    # Object properties.
    btn_1_r = ObjectProperty()
    lbl_1_c = ObjectProperty()
    sp_1_l = ObjectProperty()

    # String properties.
    search_results = StringProperty()

    def do_action(self):
        #self.show_popup()
        self.houseSwitch(self.sp_1_l.text)
        #self.pop_up.dismiss()

    # Spinner switch
    def houseSwitch(self, house):
        if house == "Välj hus":
            self.lbl_1_c.text = "Vänligen välj ett hus."
        elif house == 'Novahuset':
            self.lbl_1_c.text = getOutputListReturn(novahuset_rooms, novahuset_rooms_url)
        elif house == 'Långhuset':
            self.lbl_1_c.text = getOutputListReturn(langhuset_rooms, langhuset_rooms_url)
        elif house == 'Teknikhuset':
            self.lbl_1_c.text = getOutputListReturn(teknikhuset_rooms, teknikhuset_rooms_url)
        elif house == 'Forumhuset':
            self.lbl_1_c.text = getOutputListReturn(forumhuset_rooms, forumhuset_rooms_url)
        elif house == 'Prismahuset P103-P219':
            self.lbl_1_c.text = getOutputListReturn(prismahuset_rooms, prismahuset_rooms_url)
        elif house == 'Prismahuset P220-P276':
            self.lbl_1_c.text = getOutputListReturn(prismahuset_2_rooms, prismahuset_2_rooms_url)
        elif house == 'Prismahuset Grupprum':
            self.lbl_1_c.text = getOutputListReturn(prismahuset_g_rooms, prismahuset_g_rooms_url)
        elif house == 'Gymnastikhuset':
            self.lbl_1_c.text = getOutputListReturn(gymnastikhuset_rooms, gymnastikhuset_rooms_url)
        elif house == 'Bilbergskahuset':
            self.lbl_1_c.text = getOutputListReturn(bilbergskahuset_rooms, bilbergskahuset_rooms_url)
        elif house == 'CampusUSÖ':
            self.lbl_1_c.text = getOutputListReturn(campus_uso_rooms, campus_uso_rooms_url)
        elif house == 'Musikskolan':
            self.lbl_1_c.text = getOutputListReturn(musikskolan_rooms, musikskolan_rooms_url)
        elif house == 'Biblioteks grupprum':
            self.lbl_1_c.text = getOutputListReturn(bibliotek_g_rooms, bibliotek_g_rooms_url)
        else:
            self.lbl_1_c.text = "Något gick fel, vänligen försök igen."

    def show_popup(self):
        self.pop_up = Factory.PopupBox()
        self.pop_up.update_pop_up_text('Obokade tider hämtas...')
        self.pop_up.open()

class ControllerApp(App):

    def build(self):
        return Controller()


if __name__ == '__main__':
    ControllerApp().run()
