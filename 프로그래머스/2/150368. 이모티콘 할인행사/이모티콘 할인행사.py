from itertools import product

def solution(users, emoticons):
    answer = []
    max_sign, max_total = 0, 0
    
    # 이모티콘 할인율은 10%, 20%, 30%, 40% 중 하나
    # 이모티콘 최대 7개여도 4**7 = 16384
    sales_perc = [10,20,30,40]

    # 중복순열로 이모티콘 할인률 리스트 순회
    for emo_perc in product(sales_perc, repeat=len(emoticons)):
        temp_sign, temp_total = 0,0 
        
        # 각 사용자와 이모티콘 할인률 비교
        for user_perc, user_price in users:
            total = 0
            for i in range(len(emoticons)):
                if emo_perc[i] >= user_perc:
                    total += emoticons[i] * (100-emo_perc[i]) / 100
            
            if total >= user_price:
                temp_sign += 1
            else:
                temp_total += total
        
        # 우선순위 지키기        
        if temp_sign > max_sign:
            max_sign, max_total = temp_sign, temp_total
        elif temp_sign == max_sign:
            max_total = max(max_total, temp_total)
        
        
    return [max_sign, max_total]