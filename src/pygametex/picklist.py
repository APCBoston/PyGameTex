#!/bin/env python3

'''
Copyright (C) 2022 Andy Piltser-Cowan <awc34@cornell.edu>.

Released under Creative Commons Attribution-Sharealike License 4.0
Available at https://creativecommons.org/licenses/by-sa/4.0/
Contact the author if a different license is desired.

This should be considered alpha-quality software, the author makes no warranty
as to its quality.  Expect bugs.
'''

import PySimpleGUI as sg

def draw_window(char_dict: dict) -> sg.Window:
    '''
    Draw a simple window with a listbox to select which character(s) to render
    '''

    sg.theme("SystemDefault")
    charList = char_dict_to_list(char_dict)
    layout = [
                [sg.Text("Pick one or more characters to render.")]
                [sg.Listbox(charList,select_mode="LISTBOX_SELECT_MODE_MULTIPLE",bind_return_key=True,justification="left",key="charpicker")]
                [sg.Button("Go"), sg.Button("Exit") ]
            ]

def char_dict_to_list(char_dict: dict) -> list[str]

