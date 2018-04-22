massiv = []

















all_massiv = []

istochniki = ["only", "95c", "ateliesaun", "saunnex"]

# dicto = {
#     "95c": Tovar()??,
#     "ateliesaun": Tovar()??
# }
#
# dicto["ateliesaun"] # !!

for mass in massiv:
    alli = {}
    for mas in massiv:
        if mass.full_name == mas.full_name:
            alli[mass.site] = mass
    all_massiv.append(alli)

def save_compound(tovary):
    import csv
    with open('all.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        rows = ['brand', 'name']
        for ist in istochniki:
            rows.append('price' + ist)
        writer.writerow(rows)
        for qqq in all_massiv:
            row = [qqq["only"].brand, qqq["only"].name]
            for ist in istochniki:
                tovar = qqq[ist]
                if tovar:
                    row.append(www.price)
                else:
                    row.append(0)

            writer.writerow(row)
            # for qqq1 in qqq:
            #     writer.writerow([qqq1.brand, qqq1.name, qqq1.price])

        # for tovar in tovary:
        #     writer.writerow([tovar.brand, tovar.name, tovar.price])

save_to_csv(all_massiv)
