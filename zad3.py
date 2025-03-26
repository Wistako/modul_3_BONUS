
# ZAD 3

models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}
    


for car in models:
    brand = car.split(' - ')[0]
    model = car.split(' - ')[1]
    index = models.index(car)
    
    if cars.get(brand) is None:
        cars[brand] = {}
    if cars[brand].get(model) is None:
        cars[brand][model] = {}


    sale = [sales2016[index], sales2017[index], sales2018[index]]
    for sal in sale:
        ind = sale.index(sal)
        if sal == 'NA':
            sale[ind] = 0
        else:
            sale[ind] = int(sal.replace(',',''))
        
        if ind == 0:
            cars[brand][model]['2016'] = sale[ind]
        elif ind == 1:
            cars[brand][model]['2017'] = sale[ind]
        elif ind == 2:
            cars[brand][model]['2018'] = sale[ind]
    
print(cars)

val = 0
index = 0
for sal in sales2017:
    prepare_value = 0
    if sal == 'NA':
        prepare_value = 0
    else:
        prepare_value = int(sal.replace(',',''))
    if prepare_value > val:
        val = prepare_value
        index = sales2017.index(sal)
answer1 = models[index]
print('Odp 1: ', answer1)

best_sales = 0
answer2 = ''
for company in cars:
    count = 0
    for model in cars[company]:
        val = cars[company][model].get('2018')
        if val:
            count += val
    if count > best_sales:
        answer2 = company

print('Odp 2: ', company)

answer3 =[]

for company in cars:    
    for model in cars[company]:
        val_2016 = cars[company][model]['2016']
        val_2017 = cars[company][model]['2017']
        if val_2016 == 0 and val_2017 > 0:
            answer3.append(f'{company} - {model}')


print('Odp 3: ', answer3)
answer4 = ''
lowest = None
for company in cars:    
    for model in cars[company]:
        count = 0
        for year in cars[company][model]:
            sales = cars[company][model][year]
            count += sales
        if lowest is None or count < lowest:
            answer4 = model

print('Odp 4: ', answer4)

sales_2018 = 0
sales_2017 = 0

for model in cars['Ford']:
    for year in cars['Ford'][model]:
        if year == '2018':
            sales_2018 += cars['Ford'][model][year]
        elif year == '2017':
            sales_2017 += cars['Ford'][model][year]

diff = sales_2018 - sales_2017 
answer5 = str(int((diff / sales_2017) * 100)) + '%'


print('Odp 5: ', answer5)