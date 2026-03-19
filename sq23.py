
import logging
logging.basicConfig(level=logging.DEBUG)
def process_data(data):
    result = []
    for item in data:
        value = item['value']
        result.append(value * 2)
        y=len(result)
        try:
            x=sum(result) / len(result)
            logging.info(f"Final average: {x}")
            
        except ZeroDivisionError:
            logging.error("division by zero error came")
            
    return  x

data = [{'value': 0}, {'value': 0}, {'value': 0}]
x=process_data(data)
print(x)