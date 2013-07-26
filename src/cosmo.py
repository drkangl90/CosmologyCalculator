from tkinter import *
from tkinter import ttk
import math
from decimal import *



def calc_dzage(Z):
    lpz = math.log((1 + 1 * Z)) / math.log(Decimal(10.0))
    dzage = 0
    if lpz > 15.107:
        dzage = 0.214
    elif lpz > 14.081:
        dzage = 0.013 * (lpz - 14.081) + 0.201
    elif lpz > 13.055:
        dzage = 0.013 * (lpz - 13.055) + 0.188
    elif lpz > 12.382:
        dzage = 0.024 * (lpz - 12.382) + 0.171
    elif lpz > 12.258:
        dzage = 0.461 * (lpz - 12.258) + 0.114
    elif lpz > 11.851:
        dzage = 0.069 * (lpz - 11.851) + 0.086
    elif lpz > 10.775:
        dzage = 0.035 * (lpz - 10.775) + 0.048
    elif lpz > 10.000:
        dzage = 0.048
    elif lpz > 9.500:
        dzage = 0.019 * (lpz - 9.500) + 0.039
    elif lpz > 9.000:
        dzage = 0.020 * (lpz - 9.000) + 0.028
    elif lpz > 8.500:
        dzage = 0.040 * (lpz - 8.500) + 0.008
    elif lpz > 8.000:
        dzage = 0.014 * (lpz - 8.000) + 0.001
    elif lpz > 7.500:
        dzage = 0.002 * (lpz - 7.500)
    return dzage

def nurho(mnu, mnurel):
    y = math.pow(Decimal(1 + math.pow(mnurel / mnu, 1.842)), Decimal(1.0 / 1.842))
    return y

def calc_zage(Z, T0, we, wmu, wtau, nurho, Mnue, Mnumu, Mnutau, n, h, WV, WM, WR, Wnu, W, Wp, mnurel):
    WK = Decimal(Decimal(1) - WM - WR - WV)
    WM = WM - Wnu;
    az = 1 / (1 + 1 * Z)
    age = Decimal(0)
    for i in range(n):
        a = az * Decimal(i + 0.5) / n
        rhoV = WV * Decimal(math.pow(a, -3 - 3 * W - 6 * Wp)) * Decimal(math.exp(6 * Wp * (a - 1)))
        Wnu = (we * Decimal(nurho(Mnue, mnurel)) + wmu * Decimal(nurho(Mnumu, mnurel)) + wtau * Decimal(nurho(Mnutau, mnurel))) / (h * h)
        adot = math.sqrt(WK + ((WM + Wnu) / a) + (WR / (a * a)) + (rhoV * a * a))
        age = age + Decimal(1) / Decimal(adot)
    zage = Decimal(az) * age / n
    return zage

def calc_mid(az, n, WV, WM, WR, Wnu, w, wp, nurho, Mnue, Mnumu, Mnutau, mnurel, we, wmu, wtau, h):
    WK = 1 - WM - WR - WV;
    WM = WM - Wnu;
    DTT = 0
    DCMR = 0
    for i in range(n):
        a = az + (1 - az) * Decimal(i + 0.5) / n
        rhoV = WV * Decimal(math.pow(a, -3 - 3 * w - 6 * wp)) * Decimal(math.exp(6 * wp * (a - 1)))
        Wnu = Decimal((we * nurho(Mnue * a, mnurel) + wmu * nurho(Mnumu * a, mnurel) + wtau * nurho(Mnutau * a, mnurel)) / (h * h))
        adot = Decimal(math.sqrt(WK + ((WM + Wnu) / a) + (WR / (a * a)) + (rhoV * a * a)))
        DTT = Decimal(DTT + 1 / adot)
        DCMR = Decimal(DCMR + 1 / (a * adot))
    values = {"DTT": DTT, "DCMR":DCMR}
    return values


def calculate(*args):
    try:
        # constants
        i = 0  # index
        n = 1000  # number of points in integrals
        nda = 1  # number of digits in angular size distance
        value = Decimal(H0.get())  # H0 = 71  # Hubble constant
        WM = Decimal(wm.get())  # 0.27  Omega(matter)
        WV = Decimal(0.73)  # Omega(vacuum) or lambda
        WR = Decimal(0)  # Omega(radiation)
        # WK = 0  # Omega curvaturve = 1-Omega(total)
        Wnu = Decimal(0)  # Omega from massive neutrinos
        Z = Decimal(z.get())  # z = 3.0 redshift of the object
        h = Decimal(0.71)  # H0/100
        Mnue = Decimal(mnue.get())  # 0.001   mass of electron neutrino in eV
        if (Mnue < 0.00001):
            Mnue = Decimal(0.00001)
        Mnumu = Decimal(mnumu.get())  # 0.009   mass of muon neutrino in eV
        if (Mnumu < 0.00001):
            Mnumu = Decimal(0.00001)
        Mnutau = Decimal(mnutau.get())  # 0.049   mass of tau neutrino in eV
        if (Mnutau < 0.00001):
            Mnutau = Decimal(0.00001)
        # we = Mnue / 93  # Omega(nu(e))h^2
        # wmu = Mnumu / 93  # Omega(nu(mu))h^2
        # wtau = Mnutau / 93  # Omega(nu(tau))h^2
        # mnurel = 0.0005  # mass of neutrino that is just now relativistic in eV
        T0 = Decimal(t0.get())  # 2.72528  CMB temperature in K
        mnurel = Decimal(6.13) * (T0 / Decimal(2.72528)) / Decimal(11604.5)
        c = Decimal(299792.458)  # velocity of light in km/sec
        Tyr = 977.8  # coefficent for converting 1/H into Gyr
        DTT = 0.5  # time from z to now in units of 1/H0
        DTT_Gyr = 0.0  # value of DTT in Gyr
        age = 0.5  # age of Universe in units of 1/H0
        age_Gyr = 0.0  # value of age in Gyr
        dzage = calc_dzage(Z)
        zage = 0.1  # age of Universe at redshift z in units of 1/H0
        zage_Gyr = 0.0  # value of zage in Gyr
        DCMR = 0.0  # comoving radial distance in units of c/H0
        DCMR_Mpc = 0.0
        DCMR_Gyr = 0.0
        DA = 0.0  # angular size distance
        DA_Mpc = 0.0
        DA_Gyr = 0.0
        kpc_DA = 0.0
        DL = 0.0  # luminosity distance
        DL_Mpc = 0.0
        DL_Gyr = 0.0  # DL in units of billions of light years
        V_Gpc = 0.0
        a = 1.0  # 1/(1+z), the scale factor of the Universe
        # az = 0.5  # 1/(1+z(object))
        W = Decimal(w.get())  # -1  # equation of state, w = P/(rno*c^2)
        Wp = Decimal(wp.get())  # 0  # rate of change of equation of state, w(a) = w+2*wp*(1-a)

        # Caculations
        we = (Mnue / Decimal(93.64)) * Decimal(math.pow(T0 / Decimal(2.72528), Decimal(3)))
        wmu = (Mnumu / Decimal(93.90)) * Decimal(math.pow(T0 / Decimal(2.72528), Decimal(3)))
        wtau = (Mnutau / Decimal(93.90)) * Decimal(math.pow(T0 / Decimal(2.72528), Decimal(3)))

        az = 1 / (1 + 1 * Z)
        W1 = Decimal(1 / (2.477e10))
        W2 = Decimal(math.pow(T0 / Decimal(2.72528), Decimal(4)))
        W3 = Decimal(h * h)
        WR = W1 * (W2 / W3)
        T1 = calc_zage(Z, T0, we, wmu, wtau, nurho, Mnue, Mnumu, Mnutau, n, h, WV, WM, WR, Wnu, W, Wp, mnurel)
        T2 = Decimal(math.pow(10.0, dzage))
        zage = T1 * T2
        values = calc_mid(az, n, WV, WM, WR, Wnu, w, wp, nurho, Mnue, Mnumu, Mnutau, mnurel, we, wmu, wtau, h)
        DTT = (1 - az) * values["DTT"] / n
        DCMR = (1 - az) * values["DCMR"] / n
        age = DTT + zage  # constant (age of universe in units of 1/H0)
        age_Gyr = age * (Tyr / value)
        DTT_Gyr = (Tyr / H0) * DTT
        DCMR_Gyr = (Tyr / H0) * DCMR
        DCMR_Mpc = (c / H0) * DCMR
        Gyr.set(age_Gyr)
    except ValueError:
        pass

root = Tk()
root.title("H0 to Gyr")

mainframe = ttk.Frame(root, padding = "4 4 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

# input boxes
H0 = StringVar()
Z = StringVar()
Wm = StringVar()
Mnue = StringVar()
Mnumu = StringVar()
Mnutau = StringVar()
w = StringVar()
Wp = StringVar()
T0 = StringVar()

# output lables
Gyr = StringVar()
red = StringVar()

# Grid input set up
H0_entry = ttk.Entry(mainframe, width = 7, textvariable = H0)
H0_entry.grid(column = 3, row = 1, sticky = (W, E))
z_entry = ttk.Entry(mainframe, width = 7, textvariable = Z)
z_entry.grid(column = 3, row = 2, sticky = (W, E))
wm_entry = ttk.Entry(mainframe, width = 7, textvariable = Wm)
wm_entry.grid(column = 3, row = 3, sticky = (W, E))
mnue_entry = ttk.Entry(mainframe, width = 7, textvariable = Mnue)
mnue_entry.grid(column = 3, row = 4, sticky = (W, E))
mnumu_entry = ttk.Entry(mainframe, width = 7, textvariable = Mnumu)
mnumu_entry.grid(column = 3, row = 5, sticky = (W, E))
mnutau_entry = ttk.Entry(mainframe, width = 7, textvariable = Mnutau)
mnutau_entry.grid(column = 3, row = 6, sticky = (W, E))
w_entry = ttk.Entry(mainframe, width = 7, textvariable = W)
w_entry.grid(column = 3, row = 7, sticky = (W, E))
wp_entry = ttk.Entry(mainframe, width = 7, textvariable = Wp)
wp_entry.grid(column = 3, row = 8, sticky = (W, E))
t0_entry = ttk.Entry(mainframe, width = 7, textvariable = T0)
t0_entry.grid(column = 3, row = 9, sticky = (W, E))

# Grid output set up
ttk.Label(mainframe, textvariable = Gyr).grid(column = 6, row = 1, sticky = (W, E))
ttk.Label(mainframe, textvariable = red).grid(column = 6, row = 2, sticky = (W, E))
ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 4, row = 10, sticky = W)

# Text set up
ttk.Label(mainframe, text = "H0").grid(column = 2, row = 1, sticky = W)
ttk.Label(mainframe, text = "Z").grid(column = 2, row = 2, sticky = W)
ttk.Label(mainframe, text = "O_m").grid(column = 2, row = 3, sticky = W)
ttk.Label(mainframe, text = "M_nu(e)").grid(column = 2, row = 4, sticky = W)
ttk.Label(mainframe, text = "M_nu(mu)").grid(column = 2, row = 5, sticky = W)
ttk.Label(mainframe, text = "M_nu(tau)").grid(column = 2, row = 6, sticky = W)
ttk.Label(mainframe, text = "w").grid(column = 2, row = 7, sticky = W)
ttk.Label(mainframe, text = "w'").grid(column = 2, row = 8, sticky = W)
ttk.Label(mainframe, text = "T0").grid(column = 2, row = 9, sticky = W)
# ttk.Label(mainframe, text = "is equivalent to").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "Gyr").grid(column = 5, row = 1, sticky = W)
ttk.Label(mainframe, text = "redshift").grid(column = 5, row = 2, sticky = W)

for child in mainframe.winfo_children(): child.grid_configure(padx = 5, pady = 5)

H0_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
