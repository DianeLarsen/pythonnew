import unittest
from unittest.mock import patch, PropertyMock, Mock
from tkinter import StringVar, Tk, Button
from project import open1, open2
import project

class TestProjectFunctions(unittest.TestCase):

    def test_upDateNumClicks(self):
        root = Tk()
        # Set up a mock value for numClicks
        open1.numClicks = 0
        # Set up the initial state of dispClicks
        project.upDateNumClicks(open1.numClicks)

        open1.numClicks = 1
        # Call the function being tested
        project.upDateNumClicks(open1.numClicks)
        

        # After calling upDateNumClicks, dispClicks should be updated
        self.assertEqual(project.dispClicks.get(), "Num of Clicks\n1")
        root.destroy()
    def test_gameStatusUpdate(self):
        root = Tk()
        # Set up the initial state of gameStatusStr
        # Call the function being tested with a sample game status
        project.gameStatusUpdate("Game in progress")
            # After calling gameStatusUpdate, gameStatusStr should be updated
        self.assertEqual(project.gameStatusStr.get(), "Game in progress")
        root.destroy()

    def test_open2_structure(self):
        # Test if the main structure of open2 is created successfully
        with patch('tkinter.Toplevel.geometry'), \
            patch('tkinter.Toplevel.title'), \
            patch('tkinter.Toplevel.configure'), \
            patch('tkinter.Frame.grid'), \
            patch('tkinter.Label.grid'), \
            patch('tkinter.Entry.grid'), \
            patch('tkinter.Button.grid'), \
            patch('tkinter.messagebox.showinfo'):
            
            open2()

    def test_checker_x_click(self):
        # Create a real tkinter.Button for testing
        root = Tk()
        buttons = Button(root, text=" ")

        # Simulate a button click when click is True
        open2.click = True
        project.checker(buttons)

        # Check if the button text is updated to "X" and click is set to False
        self.assertEqual(buttons["text"], "X")
        self.assertFalse(open2.click)
        root.destroy()

    # def test_checker_o_click(self):
    #     # Simulate a button click when click is False
    #     open2.click = False
    #     project.checker(self.buttons_mock)

    #     # Check if the button text is updated to "O" and click is set to True
    #     self.assertEqual(self.buttons_mock.text, "O")
    #     self.assertTrue(open2.click)

    # def test_checker_already_marked(self):
    #     # Simulate a button click on an already marked button
    #     self.buttons_mock.configure_mock(text="X")
    #     open2.click = True
    #     project.checker(self.buttons_mock)

    #     # Check that the button text and click are not changed
    #     self.assertEqual(self.buttons_mock.text, "X")
    #     self.assertTrue(open2.click)


if __name__ == '__main__':
    unittest.main()
