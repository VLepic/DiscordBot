import time
import math

class Timer:
    Timer = 0
    def tstart(self):
        Timer.Timer = time.time_ns()
        
    def tend(self):
        Timer.Timer =(time.time_ns() - Timer.Timer)/1000000000
        if Timer.Timer < 60:
            return "Čas: " + str(Timer.Timer) + " s."
        elif Timer.Timer < 3600:
            return "Čas: " + str(math.floor(Timer.Timer/60)) + " m, " + str(math.floor(Timer.Timer % 60)) + " s."
        elif Timer.Timer >= 3600:
            hodin = math.floor(Timer.Timer / 3600)
            Timer.Timer = Timer.Timer - (math.floor(Timer.Timer / 3600) * 3600)
            minut = math.floor(Timer.Timer / 60)
            Timer.Timer = Timer.Timer - (math.floor(Timer.Timer / 60) * 60)
            sekund = math.floor(Timer.Timer % 60)
            return "Čas: " + str(hodin) + " h, " + str(minut) + " m, " + str(sekund) + " s."

