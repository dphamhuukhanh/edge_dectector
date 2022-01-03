from posixpath import splitext
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from processing import smoothing_processing
import cv2
import os

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.8, 0.8))
        self._popup.open()

    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])):
                self.ids.image1.source = filename[0]
        except:
            pass
        self.dismiss_popup()

    def clear_image(self):
        try:
            os.remove(self.ids.image1.source)
            os.remove(self.ids.image2.source)
            self.ids.image1.source = ''
            self.ids.image1.reload()
            self.ids.image2.source = ''
            self.ids.image2.reload()
        except:
            pass

    def edge_detect(self):
        try:
            os.remove(self.ids.image2.source)
            self.ids.image2.source = ''
            self.ids.image2.reload()
        except:
            pass
        try:
            img_path = self.ids.image1.source
            img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED) 
            img_fix = smoothing_processing.image_CannyDectectEdge1(img, 100, 200)
    
            path = self.ids.image1.source
            path, filename = os.path.splitdrive(path)[:2]
            filename = splitext(filename)[0] + '1.jpg'
            saved_path = os.path.join(path, filename)
       
            cv2.imwrite(saved_path, img_fix)
            cv2.destroyAllWindows()
            self.ids.image2.source = saved_path
        except:
            self._popup = Popup(title="No image found!", size_hint=(0.2, 0.2))
            self._popup.open()

    def Gray_transform(self):
        try:
            os.remove(self.ids.image2.source)
            self.ids.image2.source = ''
            self.ids.image2.reload()
        except:
            pass
        try:
            img_path = self.ids.image1.source
            img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED) 
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            path = self.ids.image1.source
            path, filename = os.path.splitdrive(path)[:2]
            filename = splitext(filename)[0] + '2.jpg'
            saved_path = os.path.join(path, filename)
        
            cv2.imwrite(saved_path, img_gray)
            cv2.destroyAllWindows()
            self.ids.image2.source = saved_path
        except:
            self._popup = Popup(title="No image found!", size_hint=(0.2, 0.2))
            self._popup.open()
        
class Editor(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    Editor().run()