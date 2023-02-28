# 120884 치킨 쿠폰

def solution(chicken):
    coupon = chicken
    service = 0

    while coupon > 9:
        service += coupon // 10
        service_coupon = coupon // 10
        coupon %= 10
        coupon += service_coupon
        service_coupon = 0

    return service
    
def solution2(chicken):
    return chicken // 10 + solution2(chicken // 10 + chicken % 10) if chicken >= 10 else 0
