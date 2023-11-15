import os
import requests
import zipfile
from urllib.parse import urlparse
from tqdm import tqdm
from pathlib import Path

from wafer_fault_detection.utils import get_size
from wafer_fault_detection.logging import logger
from wafer_fault_detection.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # def download_file(self):
    #     logger.info("Trying to download file...")
    #     if not os.path.exists(self.config.local_data_file):
    #         logger.info("Download started...")
    #         filename, headers = request.urlretrieve(
    #             url=self.config.source_URL,
    #             filename=self.config.local_data_file
    #         )
    #         logger.info(f"{filename} download! with following info: \n{headers}")
    #     else:
    #         logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")       
    
    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            url = self.config.source_URL
            response = requests.get(url)

            if response.status_code == 200:
                url_path = urlparse(url).path
                file_name = url_path.split("/")[-1]

                with open(file_name, "wb") as file:
                    file.write(response.content)
            else:
                logger.info(f"Failed to download. Status code: {response.status_code}")

            logger.info(f"Downloaded {file_name} successfully")

            # Unzip the downloaded file
            with zipfile.ZipFile(file_name, "r") as zip_ref:
                for member in zip_ref.infolist():
                    extract_folder = self.config.unzip_dir
                    if "__MACOSX" not in member.filename:
                        zip_ref.extract(member, extract_folder)
            
            logger.info(f"Unzipped {file_name} successfully to {self.config.local_data_file}")

            os.remove(file_name)
                
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")