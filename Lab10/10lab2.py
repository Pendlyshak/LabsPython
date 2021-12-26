class Address:

    def __init__(self, country, region, city_village, street, house_number, date_of_completion, length_of_stay):
        self.country = country
        self.region = region
        self.city_village = city_village
        self.street = street
        self.house_number = house_number
        self.date_of_completion = date_of_completion
        self.length_of_stay = length_of_stay


    def Over(self, number_of_days_of_stay):  #чи не закінчився термін перебування
        self.number_of_days_of_stay = number_of_days_of_stay
        if self.length_of_stay - self.number_of_days_of_stay == 0:
            print('Термін перебування закінчився')
        else:
            print('Кільксть днів до закінчення терміну: {0}'.format(self.length_of_stay - self.number_of_days_of_stay))


a = Address('Ukraine', 'Zakarpattya', 'Uzhhorod', 'Zagorska', '26', '21.12.2021', '48')
print(a.country, a.region, a.city_village, a.street, a.house_number, a.date_of_completion, a.length_of_stay)
a.Over('self.number_of_days_of_stay')










#class InformationAboutTheTraveler():
 #   def __init__(self, surname_and_initials, profession, date_of_birth):
         #self.information_about_the_traveler = information_about_the_traveler
  #      self.surname_and_initials = surname_and_initials
   #     self.profession = profession
    #    self.date_of_birth = date_of_birth