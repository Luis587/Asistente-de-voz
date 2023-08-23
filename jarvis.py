import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

name = 'jarvis' 
escu = sr.Recognizer() #reconoce la voz
inicio = pyttsx3.init()

voices = inicio.getProperty('voices')
inicio.setProperty('voices', voices[0].id)

inicio.say("Hola me llamo jarvis, En que te puedo ayudar?")
inicio.runAndWait()

def talk(text):
    inicio.say(text)
    inicio.runAndWait()

def listen():
    try:
        with sr.Microphone() as micro: #microfono
            print("Escuchando....") # te escucha el asistente
            voz = escu.listen(micro)
            rec = escu.recognize_google(voz)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print (rec)
        
    except:
        pass
    return rec

def ejecu():

    rec = listen()
   
    if 'reproduce' in rec:    # reproduce musica en yt
        music = rec.replace('reproduce', '')
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)
    
    elif 'hora' in rec:    # me dice la hora
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("son las" + hora)
    
    elif 'busca' in rec:   #busca en wikipedia
        order = rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)
    
    elif 'chistes' in rec:
        jok = pyjokes.get_joke("es")
        talk(jok)

    else:
        talk("vuelve a intentarlo")

while True:
    ejecu()
