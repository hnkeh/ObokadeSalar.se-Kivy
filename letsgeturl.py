from houselists import *

t_list = bibliotek_g_rooms
r_o_string = "http://schema.oru.se/setup/jsp/Schema.jsp?startDatum=idag&intervallTyp=d&intervallAntal=1&sokMedAND=false&sprak=SV&resurser=l."

for element in t_list:
    r_o_string += element + "%2Cl."
    
print (r_o_string)
