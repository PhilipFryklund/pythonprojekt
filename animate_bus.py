import curses
import time

# Bussens design
BUS = [
    "     ______",
    "  __/  |_ \\_",
    " |  _     _``-.",
    "-'-(_)---(_)--'"
]

def animate_bus(screen):
    curses.curs_set(0)  # Dölj markören
    screen.nodelay(True)
    screen.timeout(100)  # Uppdateringstid (ms)

    height, width = screen.getmaxyx()
    bus_x = width

    while True:
        screen.clear()

        # Kolla om "q" har tryckts
        key = screen.getch()
        if key == ord('q'):
            break

        # Rita bussen
        for i, line in enumerate(BUS):
            if height // 2 + i < height:  # Kontrollera gränser
                screen.addstr(height // 2 + i, bus_x, line)

        # Flytta bussen åt vänster
        bus_x -= 1
        if bus_x < -len(BUS[0]):  # Återställ om bussen lämnar skärmen
            bus_x = width

        screen.refresh()
        time.sleep(0.05)  # Kontrollera hastigheten på animationen

# Starta curses-applikationen
curses.wrapper(animate_bus)
