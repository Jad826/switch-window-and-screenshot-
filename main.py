file_name = input("Enter The Name Of The Screenshot : ")
file_type = ".png"
fileNameAndType = file_name+file_type
import pyautogui as agui
agui.confirm('Do You Want To Sreenshot The Next Window?')
agui.keyDown("alt")
agui.keyDown("tab")
agui.keyUp("tab")
agui.keyUp("alt")
agui.screenshot(fileNameAndType)
