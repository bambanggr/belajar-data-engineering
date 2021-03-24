from datetime import date

dict_tahun_kabisat = {
    1:31,
    2:29,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

dict_tahun_nonkabisat = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

def fnc_check_valid_date(year_from, month_from, date_from,year_to, month_to, date_to):
    # year_from, month_from, date_from = str.split(dt_from,"-")
    # year_to, month_to, date_to = str.split(dt_to,"-")
    if(year_from > year_to):
        print("Tahun FROM tidak boleh lebih besar dari Tahun TO")
    elif(int(month_from) > 12 or month_to > 12):
        print("Bulan maksimal adalah 12")
    elif(year_from == year_to and month_from > month_to):
        print("Bulan FROM tidak boleh lebih besar dari Bulan TO")
    elif(year_from <= year_to and month_from == month_to and date_from>date_to):
        print("Tanggal FROM tidak boleh lebih besar dari Tanggal TO")
    elif(year_from % 4 != 0 and date_from>dict_tahun_nonkabisat[month_from]):
        print("Date From  {}-{}-{} Tidak Valid Maksimum Tanggal {}".format(date_from,month_from,year_from,dict_tahun_nonkabisat[month_from]))
    elif(year_from % 4 == 0 and date_from>dict_tahun_kabisat[month_from]):
        print("Date From {}-{}-{} Tidak Valid Maksimum Tanggal {}".format(date_from,month_from,year_from,dict_tahun_kabisat[month_from]))
    elif(year_to % 4 != 0 and date_to>dict_tahun_nonkabisat[month_to]):
        print("Date To  {}-{}-{} Tidak Valid Maksimum Tanggal {}".format(date_to,month_to,year_to,dict_tahun_nonkabisat[month_to]))
    elif(year_to % 4 == 0 and date_to>dict_tahun_kabisat[month_to]):
        print("Date To {}-{}-{} Tidak Valid Maksimum Tanggal {}".format(date_to,month_to,year_to,dict_tahun_kabisat[month_to]))
    else:        
        fnc_count_days(year_from, month_from, date_from,year_to, month_to, date_to)

def fnc_count_days(from_year, from_month, from_day,to_year, to_month, to_day):
    cnt_days=0 #Define cnt_days = 0 for init


    while(from_year <= to_year):
        if(from_year==to_year):
            if(from_month==to_month):
                cnt_days = cnt_days+(to_day-from_day)
                print("Jumlah Hari Manual : {}".format(cnt_days))
                break
            else:
                while(from_month<to_month):
                    if(from_year%4==0):
                        max_day=dict_tahun_kabisat[from_month]
                    else:
                        max_day=dict_tahun_nonkabisat[from_month]
                    cnt_days=cnt_days+(max_day-from_day)+1
                    if(from_month< 13):
                        from_month=from_month+1
                        from_day=1
                    else:
                        from_month=1
                        from_year=from_year+1
                        from_day=1
        else:
            while(from_month<13):
                if(from_year%4==0):
                    max_day=dict_tahun_kabisat[from_month]
                else:
                    max_day=dict_tahun_nonkabisat[from_month]
                cnt_days=cnt_days+max_day
                if(from_month<13):
                    from_month=from_month+1
            from_month=1
            from_year=from_year+1



# cnt_days=0 #Define cnt_days = 0 for init
date_from=input(str("Input Date From : "))
date_to=input(str("Input Date : "))

from_year = int(str.split(date_from,"-")[0])
from_month=int(str.split(date_from,"-")[1])
from_day = int(str.split(date_from,"-")[2])

to_year = int(str.split(date_to,"-")[0])
to_month=int(str.split(date_to,"-")[1])
to_day = int(str.split(date_to,"-")[2])
fnc_check_valid_date(from_year, from_month,from_day,to_year,to_month,to_day)

"""Testing using library to compare the data"""
d0 = date(from_year, from_month, from_day)
d1 = date(to_year, to_month, to_day)
delta = d1 - d0
# print(d1)
# print(d0)
print("Jumlah Hari Pakai Library : {}".format(delta.days))
