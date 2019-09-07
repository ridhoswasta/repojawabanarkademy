import json

def datadiri():
    name = "M Ridho Swasta" #jenis string
    age = 23 #jenis number
    address = "Jl. H. Moh. Kuru No.15, Kukusan, Kecamatan Beji, Kota Depok, Jawa Barat 16425" #jenis string
    hobbies = ["Reading","Watching Movie"] #jenis array
    is_married = False # jenis boolean
    list_school =  [{
        "name": "Politeknik Caltex Riau",
        "year_in": 2014,
        "year_out": 2018,
        "major": "Teknik Elektronika Telekomunikasi"
    },{
        "name": "SMK Labor Pekanbaru",
        "year_in": 2011,
        "year_out": 2014,
        "major": "Teknik Komputer dan Jaringan"
    },{
        "name": "SMP Al - Ulum Pekanbaru",
        "year_in": 2008,
        "year_out": 2011,
        "major": None
    },{
        "name": "SDN 12 Pangkal Pinang",
        "year_in": 2002,
        "year_out": 2008,
        "major": None
    }
    ] #jenis array of object
    skills = [{
        "name":"Python",
        "level":"Advanced"
    },{
        "name":"Linux OS",
        "level":"Expert"
    },{
        "name":"Cloud Engineering ( AWS / Azure )",
        "level":"Advanced"
    }] #jenis array of object

    interest_in_coding = True #jenis boolean

    return print(json.dumps(
        {'name': name,
         'age': age,
         'hobbies': hobbies,
         'is_married' : is_married,
         'list_school' : list_school,
         'skills' : skills,
         'interest_in_coding' : interest_in_coding
         }))

datadiri()
