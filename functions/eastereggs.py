from sympy import *

def hook(keyinput):
    if "hilfe" in keyinput or "help" in keyinput or "wiki" in keyinput or keyinput is "":
        print("\nGib eine Aufgabe ein!\n\nBeispiele:\n2. Ableitung von x^2\nGleichung lösen: x^3=21*x\nKurvendiskussion 2*x^3+x^2")
        return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/html/mobile/functions.html'>"
    if "chicago" in keyinput:
        print("Ich komm immer klar auf n Chicago!")
        return "<h3>Ich komm immer klar auf n Chicago!</h3>"
    if "hello there" in keyinput:
        print("General Kenobi!")
        return "<h3>General Kenobi!</h3>"
    if "exit" in keyinput or "tschüss" in keyinput or "tschau" in keyinput:
        print("Tschau Kakao!")
        return "<h3>Du kommst hier nicht raus!</h3><br>Trotzdem:<br><h3>Tschau Kakao</h3>"
    if "moped" in keyinput:
        print("SOOS!")
        return "<h2>SOOS!</h2>"
    if "benedikt" in keyinput or "ceo" in keyinput or "programmier" in keyinput or "erfinder" in keyinput or "erfunden" in keyinput or "entwickelt" in keyinput:
        print("Benedikt Schwering\n")
        return "<h3>Benedikt Schwering<br>CEO von Schwering Software und SToftware<br>Lead Programmer von SToftware0<br>Technischer Informatiker</h3>"
    if "florian" in keyinput:
        print("Florian Tünte\n")
        return "<h3>Florian T&uuml;nte<br>CFO von SToftware<br>Programmer von SToftware0<br>Informatiker</h3>"
    if "bratwurst" in keyinput or "coburg" in keyinput:
        print("Coburg!\nBRATWURST!\n")
        return "<h1>Coburg!<br>BRATWURST!!!</h1>"
    return ""
