def setup(name:str)->list:
    from flask import Flask, render_template, Blueprint
    return Blueprint(name, __name__)