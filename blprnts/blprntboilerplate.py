from flask import Flask, render_template, Blueprint, request, flash
from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from utils.username_val import username_val


def setup(name:str)->list:
    return Blueprint(name, __name__)