import pandas as pd

df = pd.read_excel('Employee Data 2.xlsx')

nombres = df['Full Name']
puestos = df['Job Title']
salarios = df['Annual Salary']
paises = df['Country']

data = {'Nombre Completo': nombres, 'Puesto': puestos, 'Salario': salarios, 'País': paises}
tabla = pd.DataFrame(data)

primeros5 = tabla.head(5)
print(primeros5)
