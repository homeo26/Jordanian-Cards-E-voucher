# Made By Homam Manasra
# Sep / 2021

newline = lambda: print()
space = lambda: print("_" * 30, end="\n\n")


def show_cards(CardsType):
    for i in CardsType:
        for j in i:
            if j.Quantity > 0:
                j.DisplayQuantities()


class Cards:
    def __init__(self, unit, BuyingPrice, SellingPrice, Quantity):
        self.unit = unit
        self.BuyingPrice = BuyingPrice
        self.SellingPrice = SellingPrice
        self.Quantity = Quantity

    def DisplayQuantities(self):
        if len(self.unit) <= 6:  # and len(self.unit) < 10  :
            print(self.unit, "\t\t = ", self.Quantity)
        elif len(self.unit) > 6 or len(self.unit) == 10:
            print(self.unit, "\t = ", self.Quantity)


# ZAIN MOBILE
z05 = Cards("Zain0.5", 0.84, 1.0, 1)
z1 = Cards("Zain1", 1.61, 1.75, 1)
z3 = Cards("Zain3", 4.51, 4.75, 0)
z5 = Cards("Zain5", 7.50, 7.75, 0)
z6 = Cards("Zain6", 8.95, 9.50, 0)
z9 = Cards("Zain9", 13.47, 14.00, 0)
z12 = Cards("Zain12", 17.94, 19.00, 0)

# ZAIN MIX
mix5 = Cards("Mix5", 6.80, 7.00, 0)
mix6 = Cards("Mix6", 8.20, 8.50, 10)
mix7 = Cards("Mix7", 9.55, 10.00, 5)
mix8 = Cards("Mix8", 11.00, 11.50, 1)
mix10 = Cards("Mix10", 13.36, 14.00, 1)
mix11 = Cards("Mix11", 14.69, 15.50, 1)
mix15 = Cards("Mix15", 20.11, 21.00, 1)

# ZAIN DATA
zd1 = Cards("Zain DATA 1 ", 1.22, 1.50, 0)
zd2 = Cards("Zain DATA 2 ", 2.41, 3.00, 0)
zd3 = Cards("Zain DATA 3 ", 3.61, 4.00, 0)
zd4 = Cards("Zain DATA 4 ", 4.81, 5.50, 0)
zd6 = Cards("Zain DATA 6 ", 7.15, 8.00, 0)
zd8 = Cards("Zain DATA 8 ", 9.15, 10.00, 1)
zd9 = Cards("Zain DATA 9 ", 10.73, 12.00, 0)
zd10 = Cards("Zain DATA 10 ", 11.78, 13.00, 0)

# UMNIAH MOBILE
u1 = Cards("Umniah1", 1.57, 1.75, 1)
u3 = Cards("Umniah3", 4.50, 4.75, 0)
u5 = Cards("Umniah5", 7.50, 7.75, 0)
u10 = Cards("Umniah10", 14.60, 15.25, 1)

# UMNIAH SMART
s1 = Cards("Smart1", 1.39, 1.50, 0)
s3 = Cards("Smart3", 4.10, 4.50, 0)
s4 = Cards("Smart4", 5.46, 6.00, 0)
s5 = Cards("Smart5", 6.80, 7.00, 0)
s6 = Cards("Smart6", 8.20, 8.50, 1)
s7 = Cards("Smart7", 9.55, 10.00, 5)
s8 = Cards("Smart8", 11.00, 11.50, 1)
s9 = Cards("Smart9", 12.20, 13.00, 1)
s10 = Cards("Smart10", 13.49, 15.00, 1)
s12 = Cards("Smart12", 16.20, 17.50, 1)

# UMNIAH DATA
ud1 = Cards("Umniah DATA 1 ", 1.20, 1.50, 0)
ud3 = Cards("Umniah DATA 3 ", 3.65, 4.00, 0)
ud6 = Cards("Umniah DATA 6 ", 7.15, 8.00, 0)
ud7 = Cards("Umniah DATA 7 ", 8.45, 9.00, 0)
ud8 = Cards("Umniah DATA 8 ", 9.15, 10.00, 0)
ud10 = Cards("Umniah DATA 10 ", 11.94, 13.00, 1)

# ORANGE MOBILE
o05 = Cards("Orange0.5", 0.82, 1.0, 0)
o1 = Cards("Orange1", 1.58, 1.75, 1)
o3 = Cards("Orange3", 4.51, 4.75, 0)
o5 = Cards("Orange5", 7.60, 7.75, 0)
o6 = Cards("Orange6", 9.12, 9.50, 0)
o7 = Cards("Orange7", 10.65, 11.25, 0)
o8 = Cards("Orange8", 12.15, 13.00, 0)
o10 = Cards("Orange10", 15.20, 16.00, 0)
o12 = Cards("Orange12", 18.20, 19.50, 0)

# ORANGE NOS B NOS
nos2 = Cards("Nos2", 2.80, 3.00, 0)
nos5 = Cards("Nos5", 6.87, 7.00, 10)
nos505 = Cards("Nos5.5", 7.6, 8.00, 5)
nos6 = Cards("Nos6", 8.25, 8.50, 1)
nos605 = Cards("Nos6.5", 8.98, 9.50, 1)
nos7 = Cards("Nos7", 9.60, 10.00, 1)
nos8 = Cards("Nos8", 11.05, 11.50, 1)
nos9 = Cards("Nos9", 12.30, 13.00, 0)
nos10 = Cards("Nos10", 13.75, 14.50, 10)
nos11 = Cards("Nos11", 15.1, 16.50, 5)
nos12 = Cards("Nos12", 16.55, 18.00, 1)

# ORANGE DATA
od05 = Cards("Orange DATA 0.5", 0.65, 1.0, 0)
od1 = Cards("Orange DATA 1", 1.24, 1.50, 0)
od3 = Cards("Orange DATA 3", 3.65, 4.00, 0)
od6 = Cards("Orange DATA 6", 7.16, 8.00, 0)
od7 = Cards("Orange DATA 7", 4.81, 5.50, 0)
od8 = Cards("Orange DATA 8", 9.60, 10.00, 0)
od9 = Cards("Orange DATA 9", 10.80, 12.00, 1)
od11 = Cards("Orange DATA 11", 13.15, 14.50, 0)
od12 = Cards("Orange DATA 12", 14.35, 16.00, 0)
od16 = Cards("Orange DATA 16", 19.15, 21.00, 0)

zain_mobile = [z05, z1, z3, z5, z6, z9, z12]
zain_mix = [mix5, mix6, mix7, mix8, mix10, mix11, mix15]
zain_data = [zd1, zd2, zd3, zd4, zd6, zd8, zd9, zd10]
zain_all_types = [zain_mobile, zain_mix, zain_data]

umniah_mobile = [u1, u3, u5, u10]
umniah_smart = [s1, s3, s4, s5, s6, s7, s8, s9, s10, s12]
umniah_data = [ud1, ud3, ud6, ud6, ud7, ud8, ud10]
uminah_all_types = [umniah_mobile, umniah_smart, umniah_data]

orange_mobile = [o05, o1, o3, o5, o6, o7, o8, o10, o12]
orange_nos = [nos2, nos5, nos505, nos6, nos605, nos7, nos8, nos9, nos10, nos11, nos12]
orange_data = [od05, od1, od3, od6, od7, od8, od9, od11, od12, od16]
orange_all_types = [orange_mobile, orange_nos, orange_data]


def show_all_cards():
    show_cards(zain_all_types)
    show_cards(orange_all_types)
    show_cards(uminah_all_types)


"""
You can add your own Functions after this comment 
"""

print("Card quantites are : \n")
show_all_cards()
space()
