import os

class Company:
    def __init__(self, name='', integrity=0, heart=0, courage=0, ingenuity=0, service=0):
        self.name = name
        self.integrity = integrity
        self.heart = heart
        self.courage = courage
        self.ingenuity = ingenuity
        self.service = service

        self.employee_roster = []

    def roster(self):
        if len(self.employee_roster) > 0:
            for x in self.employee_roster:
                print(x.name.title())
        else:
            print('\nno employees, hire someone first')
        return self.employee_roster

    def hire(self):
        new_hire = input('\nWhat is new emplyee name? ').strip().lower()
        self.employee = Employee(name=new_hire)

        if len(self.employee_roster) == 0:
            pass
        else:
            for employee_name in self.employee_roster:
                if employee_name == new_hire:
                    print(f'\n{new_hire} has already been hired')
                    return

        self.employee_roster.append(self.employee)

        self.employee.name = new_hire
        self.employee.integrity += 5
        self.employee.heart += 5
        self.employee.courage += 5
        self.employee.ingenuity += 5
        self.employee.service += 5

    def locate(self):
        my_company.roster()
        search = input('\nwhich employee? ').strip().lower()
        for x in my_company.employee_roster:
            if search == x.name:
                return x

    def billable(self):
        billable = self.locate()

        billable.integrity += 50
        billable.heart += 50
        billable.courage += 50
        billable.ingenuity += 50
        billable.service += 50

    def overtime(self):
        overtime = self.locate()

        overtime.integrity += 150
        overtime.heart += 150
        overtime.courage += 150
        overtime.ingenuity += 150
        overtime.service += 150

    def volunteer(self):
        volunteer = self.locate()

        volunteer.integrity += 25
        volunteer.heart += 25
        volunteer.courage += 25
        volunteer.ingenuity += 25
        volunteer.service += 25

    def fso(self):
        fso = self.locate()

        fso.integrity += 1000
        fso.heart += 1000
        fso.courage += 1000
        fso.ingenuity += 1000
        fso.service += 1000

    def bench(self):
        bench = self.locate()

        bench.integrity -= 50
        bench.heart -= 50
        bench.courage -= 50
        bench.ingenuity -= 50
        bench.service -= 50

    def terminate(self):
        terminate = self.locate()

        terminate.integrity = 0
        terminate.heart = 0
        terminate.courage = 0
        terminate.ingenuity = 0
        terminate.service = 0

    def __str__(self):
        return self.name

class Employee(Company):
    def __init__(self, name='', integrity=0, heart=0, courage=0, ingenuity=0, service=0):
        super().__init__(name)
        super().__init__(integrity)
        super().__init__(heart)
        super().__init__(courage)
        super().__init__(ingenuity)
        super().__init__(service)

    def info(self):
        my_company.roster()

        search = input('\nwhich employee? ').strip().lower()
        for x in my_company.employee_roster:
            if search == x.name:
                print('\nEMPLOYEE INFO')
                print('\nEmployee:', x.name)
                print('\nFerocious Integrity:', x.integrity)
                print('Champions Heart:', x.heart)
                print('Unflinching Courage:', x.courage)
                print('Collective Ingenuity:', x.ingenuity)
                print('Passionate Service:', x.service)
                x_sum = int(x.integrity) + int(x.heart) + int(x.courage) + int(x.ingenuity) + int(x.service)
                print('\nTotal Purpose and Values:', x_sum)
            else:
                print('\nnot found')
        # else:
        #     print('something else')

    def __str__(self):
        return my_company.name

def clear_screen():
    os.system("clear")

def run():
    menu = "\nCompany Game\n\n\
  1) Hire\n\
  2) Billable hours\n\
  3) Overtime\n\
  4) Volunteer\n\
  5) FSO\n\
  6) Bench\n\
  7) Fire/Resign\n\
\n\
  R) Employee Roster\n\
  P) Employee Purpose and Values Score\n\
\n\
  X) EXIT\n\
  >>  "

    try:
        while True:
            clear_screen()
            usr_input = input(menu).strip().lower()
            if usr_input == '1':
                print('\nhiring employee')
                my_company.hire()
            elif usr_input == '2':
                print('\nmaintain billable hours')
                my_company.billable()
            elif usr_input == '3':
                print('\nworking unpaid overtime')
                my_company.employee.overtime()
            elif usr_input == '4':
                print('\nvolunteering')
                my_company.employee.volunteer()
            elif usr_input == '5':
                print('\nvoluntold to be fso')
                my_company.employee.fso()
            elif usr_input == '6':
                print('\non the bench')
                my_company.employee.bench()
            elif usr_input == '7':
                print('\nbye-bye')
                my_company.employee.terminate()

            elif usr_input == 'r':
                print('\nemployee roster')
                my_company.roster()
            elif usr_input == 'p':
                print('\npurpose and values')
                my_company.employee.info()

            elif usr_input == 'x':
                print('\nThanks for playing!')
                break
            else:
                print('\ncommand not recognized')
            input('\npress enter to continue')
    except KeyboardInterrupt:
        print('\nctrl+c')

if __name__ == '__main__':
    my_company = Company()
    run()

print('\nGoodbye!')
