# TFGAerialDisaster
Bachelor Thesis about Detection of Disaster Areas from Aerial Images

This paper develops a system for detection of disaster areas from an Unmanned Aerial Vehicle in disaster environments, specifically, debris, fire and flooded areas.

This objective is achieved through deep learning techniques, so a study on neural networks and YOLOv5 architecture is carried out prior to the work, as well as a study on object detection. It is also shown the hyperparameters with which this architecture works and a short introduction about them.

Subsequently, the original datasets from which the dataset for this case of study was obtained, the techniques and tools used for data augmentation and image labeling are presented.

The processes followed in order to arrive at the final result are described as well. This project was divided into two different phases. A first phase where the network is adapted to the aerial vision and a second phase where the network has already been adapted to the aerial vision, it will be adapted to the disaster environments for our case study. These phases are based on the deep learning technique of Transfer Learning.

Finally, all the training results are studied, analyzing all the metrics and images used to test the network. Several possible scenarios are studied in the environment in which the model will work and the different results are compared.

FILES OF THE REPOSITORY
→ train_data.rar: Origial dataset
→ train_data_augmented.rar: Augmeted Dataset
→ convert.py: Script to convert images from *.png to *.jpg
→ renombrar.py: Script to rename files
→ data_augmentation_v4.py: Data Augmetation Script
→ best.pt: Weigths for Disaster Areas
→ bestVD.pt: Weigths for Aerial Images
→ TFG__Ruben_Gonzalez.pdf: Bachelors thesis
→ PresentaciónTFG_v4.ppt: PowerPoint of Bachelors Thesis