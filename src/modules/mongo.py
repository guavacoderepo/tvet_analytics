from pymongo import MongoClient
from datetime import datetime
# connect to mongo db
mongo = MongoClient("mongodb://localhost:27017", tls=True, tlsAllowInvalidCertificates=True).tvet 



# function to create dummy 

name = ["Smith English", "Williams Smith", "John Wick", "Peter Paul", "Sam Jummy", "DInner Skiper", "Muna zammani"]
isActive = [True, False]
gender = ["male" , "female" , "other"]
states = {
    "abuja": [
        "Kwali",
        "Kuje",
        "Gwagwalada",
        "Bwari",
        "Abaji",
        "Abuja"
    ],
    "abia": [
        "Aba North",
        "Aba South",
        "Arochukwu",
        "Bende",
        "Ikawuno",
        "Ikwuano",
        "Isiala Ngwa North",
        "Isiala Ngwa South",
        "Isiala",
        "Isuikwuato",
        "Umu Nneochi",
        "Obi Ngwa",
        "Obioma Ngwa",
        "Ohafia",
        "Ohaozara",
        "Osisioma",
        "Ugwunagbo",
        "Ukwa West",
        "Ukwa East",
        "Umuahia North",
        "Umuahia South",
        "Abia"
    ],

    "adamawa": [
        "Demsa",
        "Fufore",
        "Ganye",
        "Girei",
        "Gombi",
        "Guyuk",
        "Hong",
        "Jada",
        "Lamurde",
        "Madagali",
        "Maiha",
        "Mayo Belwa",
        "Michika",
        "Mubi North",
        "Mubi South",
        "Mubi",
        "Numan",
        "Shelleng",
        "Song",
        "Toungo",
        "Yola North",
        "Yola South",
        "Adamawa"
    ],

    "akwa Ibom": [
        "Abak",
        "Eastern Obolo",
        "Eket",
        "Esit Eket",
        "Essien Udim",
        "Etim Ekpo",
        "Etinan",
        "Ibeno",
        "Ibesikpo Asutan",
        "Ibiono Ibom",
        "Ika",
        "Ikono",
        "Ikot Abasi",
        "Ikot Ekpene",
        "Ini",
        "Itu",
        "Mbo",
        "Mkpat-Enin",
        "Nsit Atai",
        "Nsit Ibom",
        "Nsit Ubium",
        "Obot Akara",
        "Nsit",
        "Okobo",
        "Onna",
        "Oron",
        "Oruk Anam",
        "Udung-Uko",
        "Udung Uko",
        "Ukanafun",
        "Urue Offong/Oruko",
        "Uruan",
        "Uyo",
        "Akwa Ibom"
    ],

    "anambra": [
        "Aguata",
        "Anambra East",
        "Anambra West",
        "Anaocha",
        "Awka North",
        "Awka South",
        "Ayamelum",
        "Dunukofia",
        "Ekwusigo",
        "Idemili North",
        "Idemili South",
        "Ihiala",
        "Njikoka",
        "Nnewi-North",
        "Nnewi-South",
        "Ogbaru",
        "Onitsha North",
        "Onitsha South",
        "Orumba North",
        "Orumba South",
        "Orumba",
        "Anambra"
    ],

    "bauchi": [
        "Alkaleri",
        "Bogoro",
        "Damban",
        "Darazo",
        "Dass",
        "Gamawa",
        "Ganjuwa",
        "Giade",
        "Itas Gadau",
        "Jama'Are",
        "Katagum",
        "Kirfi",
        "Misau",
        "Ningi",
        "Shira",
        "Tafawa-Balewa",
        "Tafawa Balewa",
        "Toro",
        "Warji",
        "Zaki",
        "Bauchi"
    ],

    "bayelsa": [
        "Brass",
        "Ekeremor",
        "Kolokuma Opokuma",
        "Nembe",
        "Ogbia",
        "Sagbama",
        "Southern-Ijaw",
        "Southern Ijaw",
        "Yenagoa",
        "Bayelsa"
    ],

    "benue": [
        "Ado",
        "Agatu",
        "Apa",
        "Buruku",
        "Gboko",
        "Guma",
        "Gwer East",
        "Gwer West",
        "Katsina-Ala",
        "Konshisha",
        "Katsina Ala",
        "Kwande",
        "Logo",
        "Makurdi",
        "Ogbadibo",
        "Ohimini",
        "Oju",
        "Okpokwu",
        "Otukpo",
        "Tarka",
        "Ukum",
        "Ushongo",
        "Vandeikya",
        "Benue"
    ],

    "borno": [
        "Abadam",
        "Askira-Uba",
        "Askira Uba",
        "Bama",
        "Bayo",
        "Biu",
        "Chibok",
        "Damboa",
        "Dikwa",
        "Gubio",
        "Guzamala",
        "Gwoza",
        "Hawul",
        "Jere",
        "Kaga",
        "Kala Balge",
        "Konduga",
        "Kukawa",
        "Kwaya-Kusar",
        "Kwaya Kusar",
        "Mafa",
        "Magumeri",
        "Maiduguri",
        "Marte",
        "Mobbar",
        "Monguno",
        "Ngala",
        "Nganzai",
        "Shani",
        "Borno"
    ],

    "cross river": [
        "Abi",
        "Akamkpa",
        "Akpabuyo",
        "Bakassi",
        "Bekwarra",
        "Biase",
        "Boki",
        "Calabar Municipal",
        "Calabar South",
        "Etung",
        "Ikom",
        "Obanliku",
        "Obubra",
        "Obudu",
        "Odukpani",
        "Ogoja",
        "Yakurr",
        "Yala",
        "Calabar",
        "Cross River"
    ],

    "delta": [
        "Aniocha North",
        "Aniocha South",
        "Aniocha",
        "Bomadi",
        "Burutu",
        "Ethiope East",
        "Ethiope West",
        "Ika North-East",
        "Ika South",
        "Isoko North",
        "Isoko South",
        "Ndokwa East",
        "Ndokwa West",
        "Okpe",
        "Oshimili North",
        "Oshimili South",
        "Patani",
        "Sapele",
        "Udu",
        "Ughelli North",
        "Ughelli South",
        "Ukwuani",
        "Uvwie",
        "Warri South-West",
        "Warri North",
        "Warri South",
        "Delta"
    ],

    "ebonyi": [
        "Abakaliki",
        "Afikpo North",
        "Afikpo South",
        "Ezza North",
        "Ezza South",
        "Ikwo",
        "Ishielu",
        "Ivo",
        "Izzi",
        "Ohaukwu",
        "Onicha",
        "Afikpo",
        "Ebonyi"
    ],

    "edo": [
        "Akoko Edo",
        "Egor",
        "Esan Central",
        "Esan North-East",
        "Esan South-East",
        "Esan West",
        "Etsako Central",
        "Etsako East",
        "Etsako West",
        "Igueben",
        "Ikpoba-Okha",
        "Ikpoba Okha",
        "Oredo",
        "Orhionmwon",
        "Ovia North-East",
        "Ovia South-West",
        "Owan East",
        "Owan West",
        "Uhunmwonde",
        "Esan",
        "Edo"
    ],

    "ekiti": [
        "Ado-Ekiti",
        "Ado Ekiti",
        "Efon",
        "Ekiti East",
        "Ekiti South-West",
        "Ekiti West",
        "Emure",
        "Gbonyin",
        "Ido-Osi",
        "Ido Osi",
        "Ijero",
        "Ikere",
        "Ikole",
        "Ilejemeje",
        "Irepodun Ifelodun",
        "Ise-Orun",
        "Ise Orun",
        "Moba",
        "Oye",
        "Ekiti"
    ],

    "enugu": [
        "Aninri",
        "Awgu",
        "Enugu East",
        "Enugu North",
        "Enugu South",
        "Ezeagu",
        "Igbo-Etiti",
        "Igbo Etiti",
        "Igbo-Eze North",
        "Igbo-Eze South",
        "Isi-Uzo",
        "Isi Uzo",
        "Nkanu East",
        "Nkanu West",
        "Nsukka",
        "Oji-River",
        "Udenu",
        "Udi",
        "Uzo-Uwani",
        "Enugu"
    ],

    "gombe": [
        "Akko",
        "Balanga",
        "Billiri",
        "Dukku",
        "Funakaye",
        "Kaltungo",
        "Kwami",
        "Nafada",
        "Shongom",
        "Yamaltu Deba",
        "Gombe"
    ],

    "imo": [
        "Aboh-Mbaise",
        "Ahiazu-Mbaise",
        "Ahiazu Mbaise",
        "Ehime-Mbano",
        "Ehime Mbano",
        "Ezinihitte",
        "Ideato North",
        "Ideato South",
        "Ihitte Uboma",
        "Ikeduru",
        "Isiala-Mbano",
        "Isiala Mbano",
        "Isu",
        "Mbano",
        "Mbaise",
        "Mbaitoli",
        "Ngor-Okpala",
        "Ngor Okpala",
        "Njaba",
        "Nkwerre",
        "Nwangele",
        "Obowo",
        "Oguta",
        "Ohaji-Egbema",
        "Ohaji Egbema",
        "Okigwe",
        "Onuimo",
        "Orlu",
        "Orsu",
        "Oru East",
        "Oru West",
        "Oru"
        "Owerri Municipal",
        "Owerri North",
        "Owerri West",
        "Imo"
    ],

    "jigawa": [
        "Auyo",
        "Babura",
        "Biriniwa",
        "Birnin-Kudu",
        "Birnin Kudu",
        "Buji",
        "Dutse",
        "Gagarawa",
        "Garki",
        "Gumel",
        "Guri",
        "Gwaram",
        "Gwiwa",
        "Hadejia",
        "Jahun",
        "Kafin-Hausa",
        "Kaugama",
        "Kazaure",
        "Kiri kasama",
        "Maigatari",
        "Malam Madori",
        "Miga",
        "Ringim",
        "Roni",
        "Sule-Tankarkar",
        "Taura",
        "Yankwashi",
        "Jigawa"
    ],

    "kaduna": [
        "Birnin-Gwari",
        "Birnin Gwari",
        "Chikun",
        "Giwa",
        "Igabi",
        "Ikara",
        "Jaba",
        "Jema'A",
        "Kachia",
        "Kaduna-North",
        "Kaduna-South",
        "Kaduna South",
        "Kagarko",
        "Kajuru",
        "Kaura",
        "Kauru",
        "Kubau",
        "Kudan",
        "Lere",
        "Makarfi",
        "Sabon-Gari",
        "Sabon Gari",
        "Sanga",
        "Soba",
        "Zangon-Kataf",
        "Zangon Kataf",
        "Zaria",
        "Kaduna"
    ],

    "kano": [
        "Ajingi",
        "Albasu",
        "Bagwai",
        "Bebeji",
        "Bichi",
        "Bunkure",
        "Dala",
        "Dambatta",
        "Dawakin-Kudu",
        "Dawakin-Tofa",
        "Dawakin Tofa",
        "Doguwa",
        "Fagge",
        "Gabasawa",
        "Garko",
        "Garun-Mallam",
        "Garun Mallam",
        "Gaya",
        "Gezawa",
        "Gwale",
        "Gwarzo",
        "Kabo",
        "Kano-Municipal",
        "Kano Municipal",
        "Karaye",
        "Kibiya",
        "Kiru",
        "Kumbotso",
        "Kunchi",
        "Kura",
        "Madobi",
        "Makoda",
        "Minjibir",
        "Nasarawa",
        "Rano",
        "Rimin-Gado",
        "Rimin Gado",
        "Rogo",
        "Shanono",
        "Sumaila",
        "Takai",
        "Tarauni",
        "Tofa",
        "Tsanyawa",
        "Tudun-Wada",
        "Tudun Wada",
        "Ungogo",
        "Warawa",
        "Wudil",
        "Kano"
    ],

    "katsina": [
        "Bakori",
        "Batagarawa",
        "Batsari",
        "Baure",
        "Bindawa",
        "Charanchi",
        "Dan-Musa",
        "Dan Musa",
        "Dandume",
        "Danja",
        "Daura",
        "Dutsi",
        "Dutsin-Ma",
        "Dutsin Ma",
        "Faskari",
        "Funtua",
        "Ingawa",
        "Jibia",
        "Kafur",
        "Kaita",
        "Kankara",
        "Kankia",
        "Kurfi",
        "Kusada",
        "Mai-Adua",
        "Mai Adua",
        "Malumfashi",
        "Mani",
        "Mashi",
        "Matazu",
        "Musawa",
        "Rimi",
        "Sabuwa",
        "Safana",
        "Sandamu",
        "Zango",
        "Katsina"
    ],

    "kebbi": [
        "Aleiro",
        "Arewa-Dandi",
        "Arewa Dandi",
        "Argungu",
        "Augie",
        "Bagudo",
        "Birnin-Kebbi",
        "Birnin Kebbi",
        "Bunza",
        "Dandi",
        "Fakai",
        "Gwandu",
        "Jega",
        "Kalgo",
        "Koko-Besse",
        "Maiyama",
        "Ngaski",
        "Sakaba",
        "Shanga",
        "Suru",
        "Wasagu/Danko",
        "Danko",
        "Wasagu",
        "Yauri",
        "Zuru",
        "Kebbi"
    ],

    "kogi": [
        "Adavi",
        "Ajaokuta",
        "Ankpa",
        "Dekina",
        "Ibaji",
        "Idah",
        "Igalamela-Odolu",
        "Igalamela Odolu",
        "Ijumu",
        "Kabba Bunu",
        "Lokoja",
        "Mopa-Muro",
        "Mopa Muro",
        "Ofu",
        "Ogori Magongo",
        "Okehi",
        "Okene",
        "Olamaboro",
        "Omala",
        "Oyi",
        "Yagba East",
        "Yagba West",
        "Kogi"
    ],

    "kwara": [
        "Asa",
        "Baruten",
        "Edu",
        "Ekiti",
        "Araromi/Opin",
        "Ilorin East",
        "Ilorin South",
        "Ilorin West",
        "Isin",
        "Kaiama",
        "Moro",
        "Offa",
        "Oke-Ero",
        "Oke Ero",
        "Oyun",
        "Pategi",
        "Kwara"
    ],

    "lagos": [
        "Agege",
        "Ajeromi-Ifelodun",
        "Ajeromi Ifelodun",
        "Alimosho",
        "Amuwo-Odofin",
        "Amuwo Odofin",
        "Apapa",
        "Badagry",
        "Epe",
        "Eti-Osa",
        "Ibeju-Lekki",
        "Ibeju Lekki",
        "Ifako-Ijaiye",
        "Ikeja",
        "Ikorodu",
        "Kosofe",
        "Lagos-Island",
        "Lagos Island",
        "Lagos-Mainland",
        "Lagos Mainland",
        "Mushin",
        "Ojo",
        "Oshodi-Isolo",
        "OshodiIsolo",
        "Shomolu",
        "Surulere",
        "Yewa-South",
        "Lagos"
    ],

    "nasarawa": [
        "Akwanga",
        "Awe",
        "Doma",
        "Karu",
        "Keana",
        "Keffi",
        "Kokona",
        "Lafia",
        "Nasarawa",
        "Nasarawa-Eggon",
        "Nasarawa Eggon",
        "Obi",
        "Wamba",
        "Toto",
        "Nasarawa"
    ],

    "ogun": [
        "Abeokuta North",
        "Abeokuta South",
        "Abeokuta",
        "Ado Odo Ota",
        "Ado Odo",
        "Ewekoro",
        "Ifo",
        "Ijebu East",
        "Ijebu North",
        "Ijebu North-East",
        "Ijebu-Ode",
        "Ijebu Ode",
        "Ikenne",
        "Imeko-Afon",
        "Imeko Afon",
        "Ipokia",
        "Obafemi-Owode",
        "Obafemi Owode",
        "Odeda",
        "Odogbolu",
        "Ogun-Waterside",
        "Ogun Waterside",
        "Remo North",
        "Shagamu",
        "Yewa North",
        "Ogun"
    ],

    "ondo": [
        "Akoko North-East",
        "Akoko North-West",
        "Akoko South-West",
        "Akoko South-East",
        "Akoko",
        "Akure North",
        "Akure South",
        "Ese-Odo",
        "Ese Odo",
        "Idanre",
        "Ifedore",
        "Ilaje",
        "Ile Oluji Okeigbo",
        "Irele",
        "Ile Oluji",
        "Odigbo",
        "Okitipupa",
        "Ondo West",
        "Ondo East",
        "Ose",
        "Owo",
        "Ondo"
    ],

    "osun": [
        "Atakumosa West",
        "Atakumosa East",
        "Ayedaade",
        "Ayedire",
        "Boluwaduro",
        "Boripe",
        "Ede South",
        "Ede North",
        "Egbedore",
        "Ejigbo",
        "Ife North",
        "Ife South",
        "Ife Central",
        "Ife East",
        "Ife",
        "Ifelodun",
        "Ila",
        "Ilesa East",
        "Ilesa West",
        "Ilesa",
        "Irepodun",
        "Irewole",
        "Isokan",
        "Iwo",
        "Obokun",
        "Odo-Otin",
        "Odo Otin",
        "Ola Oluwa",
        "Olorunda",
        "Oriade",
        "Orolu",
        "Osogbo",
        "Osun"
    ],

    "oyo": [
        "Afijio",
        "Akinyele",
        "Atiba",
        "Atisbo",
        "Egbeda",
        "Ibadan North",
        "Ibadan North-East",
        "Ibadan North-West",
        "Ibadan South-East",
        "Ibadan South-West",
        "Ibarapa Central",
        "Ibarapa East",
        "Ibarapa North",
        "Ido",
        "Ifedayo",
        "Irepo",
        "Iseyin",
        "Itesiwaju",
        "Iwajowa",
        "Kajola",
        "Lagelu",
        "Ogo-Oluwa",
        "Ogo Oluwa",
        "Ogbomosho North",
        "Ogbomosho South",
        "Olorunsogo",
        "Oluyole",
        "Ona-Ara",
        "Ona Ara",
        "Orelope",
        "Ori-Ire",
        "Ori Ire",
        "Oyo West",
        "Oyo East",
        "Saki East",
        "Saki West",
        "Saki"
        "Surulere",
        "Ibadan",
        "Ibarapa",
        "Oyo"
    ],

    "plateau": [
        "Barkin-Ladi",
        "Barkin Ladi",
        "Bassa",
        "Bokkos",
        "Jos East",
        "Jos North",
        "Jos South",
        "Kanam",
        "Kanke",
        "Langtang North",
        "Langtang South",
        "Mangu",
        "Mikang",
        "Pankshin",
        "Qua'an Pan",
        "Riyom",
        "Shendam",
        "Wase",
        "Jos",
        "Plateau"
    ],

    "rivers": [
        "Abua Odual",
        "Ahoada East",
        "Ahoada West",
        "Akuku Toru",
        "Andoni",
        "Asari-Toru",
        "Asari Toru",
        "Bonny",
        "Degema",
        "Eleme",
        "Emuoha",
        "Etche",
        "Gokana",
        "Ikwerre",
        "Khana",
        "Obio Akpor",
        "Ogba-Egbema-Ndoni",
        "Ogba Egbema Ndoni",
        "Ogu Bolo",
        "Okrika",
        "Omuma",
        "Opobo Nkoro",
        "Oyigbo",
        "Port-Harcourt",
        "port harcourt",
        "Tai",
        "Ogba"
        "Rivers"
    ],

    "sokoto": [
        "Binji",
        "Bodinga",
        "Dange",
        "Gada",
        "Goronyo",
        "Gudu",
        "Gwadabawa",
        "Illela",
        "Kebbe",
        "Kware",
        "Rabah",
        "Sabon Birni",
        "Shagari",
        "Silame",
        "Sokoto North",
        "Sokoto South",
        "Tambuwal",
        "Tangaza",
        "Tureta",
        "Wamako",
        "Wurno",
        "Yabo",
        "Sokoto"
    ],

    "taraba": [
        "Ardo-Kola",
        "Bali",
        "Donga",
        "Gashaka",
        "Gassol",
        "Ibi",
        "Jalingo",
        "Karim Lamido",
        "Kurmi",
        "Lau",
        "Sardauna",
        "Takum",
        "Ussa",
        "Wukari",
        "Yorro",
        "Zing",
        "Taraba"
    ],

    "Yobe": [
        "Bade",
        "Bursari",
        "Damaturu",
        "Fika",
        "Fune",
        "Geidam",
        "Gujba",
        "Gulani",
        "Jakusko",
        "Karasuwa",
        "Machina",
        "Nangere",
        "Nguru",
        "Potiskum",
        "Tarmuwa",
        "Yunusari",
        "Yusufari",
        "Yobe"
    ],

    "zamfara": [
        "Anka",
        "Bakura",
        "Birnin Magaji/Kiyaw",
        "Bukkuyum",
        "Bungudu",
        "Gummi",
        "Gusau",
        "Isa",
        "Kaura Namoda",
        "Kiyawa",
        "Maradun",
        "Kaura",
        "Maru",
        "Shinkafi",
        "Talata Mafara",
        "Tsafe",
        "Zurmi",
        "Zamfara"
    ],

    "niger": [
        "Agaie",
        "Agwara",
        "Bida",
        "Borgu",
        "Bosso",
        "Chanchaga",
        "Edati",
        "Gbako",
        "Gurara",
        "Katcha",
        "Kontagora",
        "Lapai",
        "Lavun",
        "Magama",
        "Mariga",
        "Mashegu",
        "Mokwa",
        "Moya",
        "Paikoro",
        "Rafi",
        "Rijau",
        "Shiroro",
        "Suleja",
        "Tafa",
        "Wushishi",
        "Niger"
    ]
}
registered = ["institution" , "staff" , "mentor" , "employer" ]
certificate = ["waec" , "neco" , "nabteb"]


def rand(list):
    
    


def create_dummy():
    data = {
    
    "user_id": {
        "_id": "0xff2345",
        "user_type": "graduate",
        "name": string,
        "is_email_verified": True,
        "email": string,
        "username": string,
        "address": "address {}".format(),

        "phone": "+234908474644",
        "avatar": {
            "_id": "0xff344455",
            "url": "photo.png.url",
            "mimetype": "jpg/png",
        },
        "is_active": True,
        "createdAt": datetime.now(),
        "updatedAt": datetime.now(),
    },
    "gender":  c,
    "state": string,
    "lga": string,
    "nationality": "Nigeria",
    "nin": "234242344",
    "registered_by": string | null,
    "current_occupation": "null for now",
    "is_employed": boolean | null,
    "resume_id": {
        "_id": "0xff33i4",
        "url": "photo.png.url",
        "mimetype": "jpeg/png",
    },
    "skills_acquired": ["skill", "skill", "skill"],

    "date_of_birth": datetime.now(),

    "school_id": {
        "_id": "0xff33i4",
        "url": "photo.png.url",
        "mimetype": "jpeg/png",
    } ,
    "matric_number": "4555423424",
    "o_level_certifications": {
        "certification_type": "waec" | "neco" | "nabteb",
        "number_of_sittings": 343434334345,
    },
    "createdAt": datetime.now(),
    "updatedAt": datetime.now(),
    }