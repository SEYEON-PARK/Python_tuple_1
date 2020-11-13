'''
def circle(r):
    area=3.14*r*r
    circum=2*r*3.14
    return [area, circum]

r=float(input("원의 반지름을 입력하세요. : "))
[area, circum]=circle(r)
print("원의 넓이는 {}이고, 원의 둘레는 {}이다." .format(area, circum))

'''
def circle(r):
    area=3.14*r*r
    circum=2*r*3.14
    return (area, circum)

r=float(input("원의 반지름을 입력하세요. : "))
(area, circum)=circle(r)
print("원의 넓이는 %f이고, 원의 둘레는 %f이다." %(area, circum))

