
import logging 
import os
from datetime import datetime

file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
file_path = os.path.join(os.getcwd(),"pavan",file_name)
os.makedirs(file_path,exist_ok=True)
path = os.path.join(file_path,file_name)

logging.basicConfig(
    filename = path,
    format="[%(asctime)s] : %(lineno)d : %(level)s : %(levelname)s : %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("The excetion is satred")