# object_detection_cv


### Project description：
Given an input image, find the positions of multiple objects in the image as well as their
class label.
1. Dataset construction：Replace one of 20 classes of objects in PASCAL VOC 2007
with another class of objects (you can replace a class from other datasets, or
build a new object class data by yourself) to form a dataset with 20
classes that is slightly different from PASCAL VOC 2007 and used for
training/testing. If you would like to try more, you can build a larger dataset (but you
cannot directly use the existing data set, you need to replace some classes of objects.)
2. Method implementation：You can adapt from the existing methods in Tensorflow/
Pytorch, etc., but you must retrain the network structure with the new dataset
mentioned above. Moreover, any improvement for the algorithm is highly expected.
Please highlight the improvement part in your report, if any.
3. Experiment： Refer to the papers about object detection, and list the mAP on
the above dataset in the table, including the results of each object class.
4. Visualization：Show the detection result with a box, and annotate the object class with
text on the box.


## Ideas

Fine tune our own YOLO model using the guide here - https://docs.ultralytics.com/modes/train/

### **Pipeline Overview**

This pipeline automates the "Data Engine." Instead of manually collecting and drawing boxes on images, you use one AI model to *dream* the images and a second AI model to *annotate* them. This creates a closed loop where you can generate infinite training data for your YOLO11 model with minimal human intervention.

---

### **Phase 1: Environment & Logic Setup**

**Summary:** Establish the coding foundation to generate diverse scenarios automatically.

* **The Goal:** Prevent the "repetitive data" problem. If all your synthetic images look the same, your model learns nothing.
* **The Action:** Create a "Prompt Generator" script. Instead of writing prompts by hand, you define lists of variables (e.g., Objects, Lighting, Weather, Backgrounds, Camera Angles) and write logic to combine them randomly.
* **Outcome:** A text file containing thousands of unique, complex descriptions ready for image generation.

### **Phase 2: Synthetic Image Generation**

**Summary:** Use a generative text-to-image model to turn your text prompts into pixels.

* **The Goal:** Create photorealistic images that match the scenarios defined in Phase 1.
* **The Action:** Feed your generated prompts into a high-speed diffusion model. You prioritize *throughput* (images per minute) and *prompt adherence* (does the image actually contain what I asked for?) over artistic flair.
* **Outcome:** A folder filled with thousands of raw, unlabelled images (JPEGs/PNGs).

### **Phase 3: Zero-Shot Auto-Labeling**

**Summary:** Use a large, pre-trained "Open Vocabulary" detector to create bounding boxes for your raw images.

* **The Goal:** Get accurate bounding boxes without drawing them yourself.
* **The Action:** Pass the raw images into a "Zero-Shot" detector. You give this detector a text list of objects to find (e.g., "helmet", "vest", "boots"). It scans the image and returns coordinates for every match it finds.
* **Outcome:** A set of label files (in standard YOLO `.txt` format) corresponding to each image.

### **Phase 4: Automated Quality Control (Filtering)**

**Summary:** Clean the data using statistical rules to remove "hallucinations" and bad samples.

* **The Goal:** Ensure your model doesn't train on garbage data (e.g., a car with 10 wheels or an empty image).
* **The Action:** Run a script to delete images that don't meet quality standards.
* *Rule 1:* Delete images with **zero detections** (empty).
* *Rule 2:* Delete images with **low confidence scores** (ambiguous objects).
* *Rule 3:* Delete images with **excessive clutter** (e.g., >50 bounding boxes, which usually indicates noise).


* **Outcome:** A clean, high-quality synthetic dataset ready for training.

### **Phase 5: Training Integration**

**Summary:** Carefully mix this new synthetic data with your real-world data to train YOLO11.

* **The Goal:** Improve the model's robustness without overfitting to the "fake" look of synthetic data.
* **The Action:**
1. **Mosaic Mixing:** Combine real and synthetic images in your training batches.
2. **Ratio Control:** Start with a conservative ratio (e.g., 80% Real, 20% Synthetic).
3. **Validation Safety:** **Never** use synthetic data in your validation or test sets. You must evaluate performance on real-world images only.


* **Outcome:** A fine-tuned YOLO11 model that generalizes better to rare scenarios (like "snowy weather" or "nighttime") that were hard to collect manually.

### **Next Step**

Would you like to start **Phase 1** by brainstorming the specific **variables** (Objects, Environments, Lighting) relevant to your project?