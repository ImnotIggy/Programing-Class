# You take the spesific heat mass and change in temperture to find the heat added by the heat gained and the lost of heat with the mass and temperture to get the heat added
# Example inputs specfic heat:4  mass:7  change in tempreture:3 = heat added:333333
specific_heat= input("What is the specific heat")
mass = input ("What is mass?")
change_in_temperture=input ("What is change in tempuerture") 
specific_heat= int (specific_heat)
mass=int(mass)
change_in_tempertur=int(change_in_temperture)
result= specific_heat*mass*change_in_temperture
#your mutiplying all the elemtns in the fomrula in line 9
print (result)
