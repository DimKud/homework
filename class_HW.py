class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age 


    def my_pasport(self, nomer_ps, kem_vd, kogda_vd ):
        self.namer_ps = nomer_ps
        self.kem_vd = kem_vd
        self.kogda_vd = kogda_vd
        if self.age >= 14:
            self.pasport = ('номер: {}. кем выдан: {}. когда выдан: {}'.format(self.namer_ps, self.kem_vd, self.kogda_vd))  
            print(self.pasport)

    def my_car(self):
        if self.age >= 18:
            self.car = 'покупай машину'
        else:
            self.car = 'еще не можешь ездить на машине'

    def doki_na_car(self):
        if self.age >= 18:
            self.doki = 'razresheno upravlyat'
        else:
            self.doki = 'no doki na car'


    def work_hu(self, name_work, time_work):
        self.name_work = name_work
        self.time_work = time_work
        if self.age >= 18:
            self.w = 'do you work'

    def otpusk(self):
        if self.time_work >= 365:
            self.otpusk = 'time for you to go on otpusk'

    
    