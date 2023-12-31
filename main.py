import modules.big_screen as screen
import modules.office as office
import modules.registration as registration
import modules.functions as m_func

screen.city1 = None
screen.flag1 = False
registration.run_reg = True

while registration.run_reg == True or registration.run_off == True or office.run_screen == True:
    print(
        "registration.run_reg =", registration.run_reg, "\n",
        "registration.run_off =", registration.run_off, "\n",
        "office.run_screen =", office.run_screen, "\n"
        )
    if registration.run_reg == True:
        registration.run_registration()
    elif registration.run_off == True:
        office.run_office()
    elif office.run_screen == True:
        screen.run_big_screen(city = screen.city1, flag = screen.flag1)

m_func.db.close()