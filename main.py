#!/usr/bin/python
import kivy
kivy.require('1.8.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import foodthingy
#imports all the stuff



class FoodlrApp(App):

    def api_call(self, instance):
        self.status = foodthingy.main(self.selected_ingredients)
        self.status_label.text=self.status

    def on_checkbox_active(self, checkbox, value):
        if value:
            print 'The checkbox', checkbox.id, 'is active'
            self.selected_ingredients.append(str(checkbox.id))
            print self.selected_ingredients

        else:
            print "The checkbox", checkbox.id, "is inactive"
            self.selected_ingredients.remove(str(checkbox.id))
            print self.selected_ingredients

    def build(self):
        self.selected_ingredients = []
        rootlayout = BoxLayout(orientation="vertical")
        layout = GridLayout(cols=10)

        self.status = "User is selecting..."
        self.status_label = Label(text=self.status, size_hint=(1, 0.135))

        self.submit_button = Button(size_hint=(1, 0.25), text="Submit!", font_size=47)
        self.submit_button.bind(on_press=self.api_call)

        unsorted_ingredients = ['alfredo sauce', 'almonds', 'almond milk', 'apple cider vinegar', 'artichoke', 'bacon', 'broth', 'baking powder', 'baking soda', 'balsamic vinegar', 'barbecue sauce', 'basil', 'beef', 'bell peppers', 'black olives', 'blackberries', 'blueberries', 'brussels sprouts', 'butter', 'carrots',
         'cashews','pecans', 'cauliflower', 'cauliflower', 'cheddar', 'cherries', 'cheese' ,'chicken breasts', 'chili', 'cinnamon', 'cocoa powder', 'coconut oil', 'coffee', 'cottage cheese', 'cream cheese', 'cucumber', 'cumin', 'eggs', 'feta', 'garlic', 'ginger', 'grape', 'green beans', 'green olives', 'ground meat',
         'bread', 'iced tea', 'jalapeno', 'ketchup', 'lemon', 'lettuce', 'lime', 'macadamia nuts', 'maple syrup', 'mayonnaise', 'milk' ,'milled pepper', 'mozzarella', 'mushrooms', 'mustard', 'nut butters', 'nutmeg', 'nuts', 'olive oil', 'onion', 'onion powder', 'oregano', 'beef broth', 'chicken broth', 'parmesan', 'parsley',
          'peanut oil', 'pepperoni', 'pesto', 'pickles', 'pine nuts', 'pasta' ,'pizza sauce', 'protein powder', 'pumpkin', 'pumpkin seeds', 'raspberries', 'red peppers', 'relish', 'wine', 'salami', 'salt', 'seeds', 'shrimp', 'snap peas', 'sour cream', 'soy sauce', 'spinach',  'spray oil', 'steak', 'strawberries', 'sunflower seeds',
           'thyme', 'tomatoes', 'vanilla extract', 'walnuts', 'whip cream', 'heavy cream', 'white vinegar', 'worcestershire sauce', 'yeast', 'yogurt', 'zucchini']
        common_ingredients = sorted(unsorted_ingredients)

        checkboxes = []
        labels = []

        for x in range(len(common_ingredients)):
            labels.append(Label(text=common_ingredients[x]))
            checkboxes.append(CheckBox(id=common_ingredients[x]))
            checkboxes[x].bind(active=self.on_checkbox_active)

        for x in range(len(checkboxes)):
            layout.add_widget(labels[x])
            layout.add_widget(checkboxes[x])

        rootlayout.add_widget(layout)
        rootlayout.add_widget(self.submit_button)
        rootlayout.add_widget(self.status_label)
        return rootlayout

if __name__ == '__main__':
    FoodlrApp().run()
