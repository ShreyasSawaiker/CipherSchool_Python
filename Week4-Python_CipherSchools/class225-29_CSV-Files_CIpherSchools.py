from csv import reader,DictReader,writer,DictWriter

with open("file.csv","r") as f:
    # csv_reader = reader(f) for reading
    csv_reader = DictReader(f,delimiter='|') #if there are no comma separated, you have to pass delimeter
    for row in csv_reader:
        print(row['name'])
        # loop can br used only once
        # readeer is an iterator
with open("file1W.csv","w",newline="") as d:
    csv_writer = writer(d)
    csv_writer.writerow(["name","countries"])
    csv_writer.writerow(["Shrey","India"])
    csv_writer.writerow(["Ram","India"])
    csv_writer.writerow(["Gram","UK"])

with open("file1DW.csv","w",newline="") as e:
    csv_writerd = DictWriter(e,fieldnames=['firstname','lastname','age'])
    csv_writerd.writeheader()
    csv_writerd.writerow({
        'firstname':'Harshit',
        'lastname':'Naik',
        'age':18
    })
    csv_writerd.writerow({
        'firstname':'Shrey',
        'lastname':'Bro',
        'age':18
    })

    # csv_writerd.writerows([{}])  writewros function

    # Reading and Writing Simultaniously
    # with open("file.csv","r") as rf:
    #     with open("Cfile.csv","w",newline="") as wf:
    #         csv_reader = DictReader(rf)
    #         csv_writer = DictWriter(wf,fieldnames=['first_name','last_name','age'])
    #         csv_writer.writeheader()
    #         for row in csv_reader:
    #             fname,lname,age = row['firstname'],row['lastname'],row['age']
    #             csv_writer.writerow({
    #                 'firstname':fname.upper()
    #                 'lastname':lname.upper()
    #                 'age':age
    #             })