rate = input ("Оцените работу оператора от1 до 5")
rate_as_number = int(rate)
if(rate_as_number<1):
    rate_as_number = 1

if(rate_as_number>5):
    rate_as_number =5

feedbeck = ''

if rate_as_number == 1:
    feedbeck = input("расскажите, что не так:")
elif rate_as_number == 2:
    feedbeck = input("расскажите, что вас смутило:")
elif rate_as_number == 3:
    feedbeck = input("почему не 4:") 
elif rate_as_number == 4:
    feedbeck = input("почему не 5:")
else:
    feedbeck = input("спасибо за оценку:")

print(feedbeck)

