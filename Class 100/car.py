class Car(object):
    def __init__(self,Model,Color,Brand,Speedlimit):
        self.model = Model
        self.brand = Brand
        self.color = Color
        self.speedlimit = Speedlimit

    def start(self):
        print("CAR HAS STARTED")

    def stop(self):
        print("CAR HAS STOPPED!!")

    def acccelarate(self):
        print("ACCELARATING")

Ferrari = Car("A1","Yellow","Ferrari",200)
Bugati = Car("B1","Blue","BUGATI",250)

Ferrari.start()
Ferrari.stop()
        