def to_days(date):
    year, month, day = map(int, date.split("."))
    return year*12*28 + month*28 + day

def solution(today, terms, privacies):
    answer = []
    today = to_days(today)
    
    terms_days = {t[0]: int(t[2:])*28 for t in terms}
    
    for i,p in enumerate(privacies):
        date, categ = p.split(" ")
        expire_date = to_days(date) + terms_days[categ]
        if expire_date<=today:
            answer.append(i+1)
        print(expire_date, today)
            
    return answer