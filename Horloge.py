import time

class Horloge:
    def __init__(self):
        self.heure_actuelle = time.localtime()

    def afficher_heure(self):
        return time.strftime("%H:%M:%S", self.heure_actuelle)

    def regler_heure(self, nouvelle_heure):
        self.heure_actuelle = time.struct_time((self.heure_actuelle.tm_year, self.heure_actuelle.tm_mon, self.heure_actuelle.tm_mday,
                                                nouvelle_heure[0], nouvelle_heure[1], nouvelle_heure[2],
                                                self.heure_actuelle.tm_wday, self.heure_actuelle.tm_yday, self.heure_actuelle.tm_isdst))
        print("L'heure réglée à:", self.afficher_heure())

    def regler_alarme(self, heure_alarme):
        print("L'alarme est réglée à:", self.afficher_heure())
        self.heure_alarme = time.struct_time((0, 0, 0, heure_alarme[0], heure_alarme[1], heure_alarme[2], 0, 0, -1))

    def programme_horloge(self):
        while True:
            self.heure_actuelle = time.localtime()
            print("Heure actuelle:", self.afficher_heure())

            if hasattr(self, 'heure_alarme') and self.heure_actuelle.tm_hour == self.heure_alarme.tm_hour and self.heure_actuelle.tm_min == self.heure_alarme.tm_min and self.heure_actuelle.tm_sec == self.heure_alarme.tm_sec:
                print("Alarme !")

            time.sleep(1)


horloge = Horloge()
horloge.regler_heure((11, 20, 0))
horloge.regler_alarme((11, 21, 0))
horloge.programme_horloge()
